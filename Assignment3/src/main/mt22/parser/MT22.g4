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

program: decl+ EOF;

decl: vardecl | funcdecl;

vardecl: (noassign | multipleassign) SEMI;
noassign: idlst COLON primitivetype;
multipleassign: ID extassign expr;
extassign: (COMMA ID) extassign (expr COMMA)
	| COLON primitivetype ASSIGN;


funcdecl: ID COLON FUNCTION functype LB paramlist RB funcinherit? body;
funcinherit: INHERIT ID;
paramlist: param (COMMA param)* | ;
param: INHERIT? OUT? ID COLON primitivetype;
body: blockstmt;

stmt:
	assignstmt
	| vardecl
	| forstmt
	| ifstmt
	| returnstmt
	| callstmt
	| breakstmt
	| continuestmt
	| whilestmt
	| dowhilestmt
	| blockstmt;

assignstmt: (expr7 | ID) ASSIGN expr SEMI;

breakstmt: BREAK SEMI;
continuestmt: CONTINUE SEMI;
ifstmt: IF LB expr RB truestmt (ELSE falsestmt)?;
truestmt: stmt;
falsestmt: stmt;
returnstmt: RETURN expr? SEMI;
callstmt: ID LB exprlst? RB SEMI;
forstmt:
	FOR LB (ID ASSIGN expr) COMMA expr COMMA expr RB stmt;
idlst: ID (COMMA ID)*;
blockstmt: LCB stmt* RCB;
dowhilestmt: DO blockstmt WHILE LB expr RB SEMI;
whilestmt: WHILE LB expr RB stmt ;

functype: primitivetype;

primitivetype:
	INTEGER
	| FLOAT
	| STRING
	| BOOLEAN
	| VOID
	| AUTO
	| arrayType;

exprlst: expr (COMMA expr)*;

expr: expr1 strconcate expr1| expr1;
expr1: expr2 relational expr2| expr2;
expr2: expr2 binarylogical expr3 | expr3;
expr3: expr3 adding expr4 | expr4;
expr4: expr4 multiplying expr5 | expr5;
expr5: unarylogical expr5 | expr6;
expr6: sign expr6 | expr7;
expr7: ID LSB exprlst RSB | expr8;
expr8: operands | LB expr RB;

adding: SUB | ADD;
multiplying: DIV | MUL | MOD;
relational: EQUAL | NOTEQUAL | LT | GT | LET | GET;
strconcate: CONCATE;
unarylogical: NOT;
binarylogical: AND | OR;
sign: SUB;
operands: INTL | FLOATL | STRINGL | BOOLL | ID | arrayL | funccall;
funccall: ID LB exprlst? RB;
arrayType: ARRAY LSB dimension RSB OF primitivetype;
dimension: INTL (COMMA INTL)*;

// Literal
INTL: (NoZeroNumber Number* (UNDERSCORE Number+)* | [0]) 
	{
		self.text = self.text.replace('_','') 
	};

FLOATL:
	( Fragtional Exponent? | INTL+ Exponent )
	{
		self.text = self.text.replace('_','')
	};

BOOLL: TRUE | FALSE;
STRINGL:
	DoubleQuote StringChar* DoubleQuote 
	{
        result = str(self.text)
        self.text = result[1:-1]
    };

arrayL: LCB exprlst RCB;

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
COMMA: ',';
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