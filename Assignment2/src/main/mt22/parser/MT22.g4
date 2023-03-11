grammar MT22;

/*
 ID: 2052904
 */

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decls EOF;

decls: decl decls |;
decl: vardecl | funcdecl;

vardecl: (noassigning | multipleassigning) SEMI;
noassigning: ID COLON primitivetype;
multipleassigning: ID multipleassigning1 expr;
multipleassigning1: (COMA ID) multipleassigning1 (expr COMA)
	| COLON primitivetype ASSIGN;
funcdecl: ID COLON FUNCTION functiontype LB paramlists RB body;
paramlists: param paramlist |;
paramlist: COMA param paramlist |;
param: OUT? INHERIT? ID COLON primitivetype;
body: LCB stmt* RCB;
stmt:
	ifstmt
	| vardecl
	| returnstmt
	| callstmt
	| breakstmt
	| continuestmt
	| assignstmt
	| whilestmt
	| dowhilestmt
	| forstmt
	| blockstmt;

assignstmt: (arrayType | ID) ASSIGN expr SEMI;

breakstmt: BREAK SEMI;
continuestmt: CONTINUE SEMI;
ifstmt: IF LB expr RB stmt* (ELSE stmt)?;
returnstmt: RETURN (expr |) SEMI;
callstmt: ID LB exprlst RB SEMI;
forstmt:
	FOR LB (ID ASSIGN expr) COMA expr COMA expr RB LCB stmt* RCB;
idlst: ID (COMA ID)*;
blockstmt: LCB stmt* RCB;
dowhilestmt: DO LCB stmt* RCB WHILE LB expr RB;
whilestmt: WHILE LB expr RB LCB stmt* RCB;

functiontype: primitivetype;

primitivetype:
	INTEGER
	| FLOAT
	| STRING
	| BOOLEAN
	| VOID
	| AUTO
	| arrayType;

exprlst: expr (COMA expr)*;

expr: expr1 (strconcate expr1)*;
expr1: expr2 (relational expr2)?;
expr2: expr3 (binarylogical expr3)*;
expr3: expr4 (adding expr4)*;
expr4: expr5 (multiplying expr5)*;
expr5: unarylogical? expr6;
expr6: sign? expr7;
expr7: expr8 | ID LSB expr RSB;
expr8: operands | ID? LB expr RB;

adding: SUB | ADD;
multiplying: DIV | MUL | MOD;
relational: EQUAL | NOTEQUAL | LT | GT | LET | GET;
strconcate: CONCATE;
unarylogical: NOT;
binarylogical: AND | OR;
sign: SUB;
operands: INTL | FLOATL | STRINGL | BOOLL | ID | arrayl;
arrayType: ARRAY LSB dimensions RSB OF primitivetype;
dimensions: INTL dimension;
dimension: COMA INTL dimension |;

// Literal
INTL: (NoZeroNumber Number* (UNDERSCORE Number+)* | [0]) { self.text = self.text.replace('_','') 
			};
FLOATL:
	(Fragtional Exponent? | Number+ Exponent) { self.text = self.text.replace('_','')};
BOOLL: TRUE | FALSE;
STRINGL:
	DoubleQuote StringChar* DoubleQuote {
        result = str(self.text)
        self.text = result[1:-1]
    };

arrayl: LCB exprlst RCB;

// Keywords
DO: 'do';
FUNCTION: 'function';
IF: 'if';
ELSE: 'else';
CONTINUE: 'continue';
AUTO: 'auto';
BREAK: 'break';
FOR: 'for';
RETURN: 'return';
WHILE: 'while';
OUT: 'out';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';
// Types
VOID: 'void';
BOOLEAN: 'boolean';
FLOAT: 'float';
INTEGER: 'integer';
STRING: 'string';
TRUE: 'true';
FALSE: 'false';

// Relational Operator 
EQUAL: '==';
NOTEQUAL: '!=';
GT: '>';
LT: '<';
GET: '>=';
LET: '<=';

// Logical Operator
AND: '&&';
OR: '||';
NOT: '!';

// Arithmetic Operator
ADD: '+';
DIV: '/';
SUB: '-';
MUL: '*';
MOD: '%';
ASSIGN: '=';

// String Operator
CONCATE: '::';

// Seperator
LB: '(';
RB: ')';
LCB: '{';
RCB: '}';
LSB: '[';
RSB: ']';
COMA: ',';
SEMI: ';';
DOT: '.';
COLON: ':';
UNDERSCORE: '_';

// Fragment
fragment Number: [0-9];
fragment NoZeroNumber: [1-9];
fragment Character: [a-z_A-Z];
fragment Fragtional: INTL+ DOT INTL*;
fragment Exponent: [Ee] [+-]? INTL+;
fragment DoubleQuote: '"';
fragment StringChar: ~[\b\t\f\r\n"\\] | EscapeSequence;
fragment EscapeSequence: '\\' [bfnrt'"\\];
fragment InvalidSequence: '\\' ~[bfrnt\\'];

// Identifiers
ID: Character (Character | Number)*;

// skip spaces, tabs, newlines
WS: [ \t\r\n\f]+ -> skip;

// Comments
LINECMT: '//' ~[\r\n]* -> skip;
BLOCKCMT: '/*' .*? '*/' -> skip;

ERROR_CHAR:
	. {
	raise ErrorToken(self.text)
};
UNCLOSE_STRING:
	DoubleQuote StringChar* ([\b\t\f\n\r"\\] | EOF) {
        unclose_str = str(self.text)
        possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
        if unclose_str[-1] in possible:
            raise UncloseString(unclose_str[1:-1])
        else:
            raise UncloseString(unclose_str[1:])
    };
ILLEGAL_ESCAPE:
	DoubleQuote StringChar* InvalidSequence {
        illegal_str = str(self.text)
        raise IllegalEscape(illegal_str[1:])
    };