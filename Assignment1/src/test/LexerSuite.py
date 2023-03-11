import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc ", "abc,<EOF>", 101))
        self.assertTrue(TestLexer.test("_abc", "_abc,<EOF>", 102))
        self.assertTrue(TestLexer.test("&&&", "&&,Error Token &", 103))
        self.assertTrue(TestLexer.test("|||", "||,Error Token |", 104))
        self.assertTrue(TestLexer.test("!", "!,<EOF>", 105))
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 106))
        self.assertTrue(TestLexer.test("157_23 ", "15723,<EOF>", 107))
        self.assertTrue(TestLexer.test("aa?bb", "aa,Error Token ?", 108))
        self.assertTrue(TestLexer.test("a15723 waaagh // waaaggg \n asd", "a15723,waaagh,asd,<EOF>", 109))
        self.assertTrue(TestLexer.test("130a12", "130,a12,<EOF>", 110))
        self.assertTrue(TestLexer.test("1_2.342", "12.342,<EOF>", 111))
        self.assertTrue(TestLexer.test("12.e234", "12.e234,<EOF>", 112))
        self.assertTrue(TestLexer.test("7e-14", "7e-14,<EOF>", 113))
        self.assertTrue(TestLexer.test("-1.23E-4", "-,1.23E-4,<EOF>", 114))
        self.assertTrue(TestLexer.test("6.02214076e+23", "6.02214076e+23,<EOF>", 115))
        self.assertTrue(TestLexer.test("\"Emperor\"", "Emperor,<EOF>", 116))
        self.assertTrue(TestLexer.test("\"Emperor\\n\"", "Emperor\\n,<EOF>", 117))
        self.assertTrue(TestLexer.test("\"Emperor\'s\"\"Glory", "Emperor\'s,Unclosed String: Glory", 118))
        self.assertTrue(TestLexer.test("0e-14", "0e-14,<EOF>", 119))
        self.assertTrue(TestLexer.test("Emperor /*Comment*/ 40_000", "Emperor,40000,<EOF>", 120))
        self.assertTrue(TestLexer.test("Emperor //GAGAGAG\n1e4", "Emperor,1e4,<EOF>", 121))

        input = """
        x: integer = 65;
        fact: function integer(n: integer) {
            if (n == 0)
                return 1;
            else return n * fact(n - 1);
        }
        """
        expect = "x,:,integer,=,65,;,fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 122))

        input = "\"I am the servant of\\nGod Emperor\""
        expect = "I am the servant of\\nGod Emperor,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 123))

        self.assertTrue(TestLexer.test("<<<>>>", "<,<,<,>,>,>,<EOF>", 124))
        self.assertTrue(TestLexer.test("!!=", "!,!=,<EOF>", 125))
        self.assertTrue(TestLexer.test("<=", "<=,<EOF>", 126))
        self.assertTrue(TestLexer.test("<=>=", "<=,>=,<EOF>", 127))
        self.assertTrue(TestLexer.test("<=>", "<=,>,<EOF>", 128))
        self.assertTrue(TestLexer.test("<>=", "<,>=,<EOF>", 129))
        self.assertTrue(TestLexer.test("6 >= 6", "6,>=,6,<EOF>", 130))
        self.assertTrue(TestLexer.test("6 >= //asdasd\n 6", "6,>=,6,<EOF>", 131))
        self.assertTrue(TestLexer.test("6 != 7", "6,!=,7,<EOF>", 132))
        self.assertTrue(TestLexer.test("||", "||,<EOF>", 133))

        input = "\"Warhammer\"\"40k"
        expect = "Warhammer,Unclosed String: 40k"
        self.assertTrue(TestLexer.test(input, expect, 134))

        input = "\"This is heretic\\g \""
        expect = "Illegal Escape In String: This is heretic\\g"
        self.assertTrue(TestLexer.test(input, expect, 135))

        input = "\"\"\"\"\"\"\"\""
        expect = ",,,,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 136))

        input = "\"\"\"\"\"\"\""
        expect = ",,,Unclosed String: "
        self.assertTrue(TestLexer.test(input, expect, 137))
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 138))
        self.assertTrue(TestLexer.test("arr[5]", "arr,[,5,],<EOF>", 139))
        self.assertTrue(TestLexer.test("arr[5,5]", "arr,[,5,,,5,],<EOF>", 140))
        self.assertTrue(TestLexer.test("{5,5}", "{,5,,,5,},<EOF>", 141))
        self.assertTrue(TestLexer.test("{5,\"Emperor\"}", "{,5,,,Emperor,},<EOF>", 142)) 
        self.assertTrue(TestLexer.test("{\"Humanity\",\"Emperor\"}", "{,Humanity,,,Emperor,},<EOF>", 142)) 

        input = "{\"Robert\" :: \"Primarch\" :: \"Guilliman\"}"
        expect = "{,Robert,::,Primarch,::,Guilliman,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 143))
        self.assertTrue(TestLexer.test("-5 + -3", "-,5,+,-,3,<EOF>", 144))
        self.assertTrue(TestLexer.test("hello_world:", "hello_world,:,<EOF>", 145))
        self.assertTrue(TestLexer.test("=!", "=,!,<EOF>", 146))
        self.assertTrue(TestLexer.test("if (a < b) {", "if,(,a,<,b,),{,<EOF>", 147))
        self.assertTrue(TestLexer.test("arr[5,5,5];", "arr,[,5,,,5,,,5,],;,<EOF>", 148))
        self.assertTrue(TestLexer.test("foo = 42;", "foo,=,42,;,<EOF>", 149))
        self.assertTrue(TestLexer.test("float pi = 3.14;", "float,pi,=,3.14,;,<EOF>", 150))
        self.assertTrue(TestLexer.test("y: string = \"hello\";", "y,:,string,=,hello,;,<EOF>", 151))
        self.assertTrue(TestLexer.test("z: auto = 3 * (4 + 5);", "z,:,auto,=,3,*,(,4,+,5,),;,<EOF>", 152))
        self.assertTrue(TestLexer.test("var: string = \"foo\" + \"bar\";", "var,:,string,=,foo,+,bar,;,<EOF>", 153))
        self.assertTrue(TestLexer.test("flag: bool = true && false;", "flag,:,bool,=,true,&&,false,;,<EOF>", 154))
        self.assertTrue(TestLexer.test("l: string[] = [\"apple\", \"banana\", \"orange\"];", "l,:,string,[,],=,[,apple,,,banana,,,orange,],;,<EOF>", 155))
        self.assertTrue(TestLexer.test("t: int = (2 + 3) * 4;", "t,:,int,=,(,2,+,3,),*,4,;,<EOF>", 156))
        self.assertTrue(TestLexer.test("c: string = \"Hello, World!\";", "c,:,string,=,Hello, World!,;,<EOF>", 157))
        self.assertTrue(TestLexer.test("d: bool = true;", "d,:,bool,=,true,;,<EOF>", 158))
        self.assertTrue(TestLexer.test("e: bool = false;", "e,:,bool,=,false,;,<EOF>", 159))
        self.assertTrue(TestLexer.test("f: int = 2 + 3 * 4;", "f,:,int,=,2,+,3,*,4,;,<EOF>", 160))
        self.assertTrue(TestLexer.test("g: float = 10 / 2.5;", "g,:,float,=,10,/,2.5,;,<EOF>", 161))
        self.assertTrue(TestLexer.test("h: bool = !false || true;", "h,:,bool,=,!,false,||,true,;,<EOF>", 162))
        self.assertTrue(TestLexer.test("n: int = -5;", "n,:,int,=,-,5,;,<EOF>", 163))
        self.assertTrue(TestLexer.test("o: float = 2.5 + 10 / 4.0;", "o,:,float,=,2.5,+,10,/,4.0,;,<EOF>", 164))
        self.assertTrue(TestLexer.test("p: bool = (2 > 3) || (4 < 5);", "p,:,bool,=,(,2,>,3,),||,(,4,<,5,),;,<EOF>", 165))
        self.assertTrue(TestLexer.test("a: int = 100;", "a,:,int,=,100,;,<EOF>", 166))
        self.assertTrue(TestLexer.test("b: float = 3.14;", "b,:,float,=,3.14,;,<EOF>", 167))
        self.assertTrue(TestLexer.test("s: string = \"Hello world!\";", "s,:,string,=,Hello world!,;,<EOF>", 168))
        self.assertTrue(TestLexer.test("a: int = 10 + 20 * 30;", "a,:,int,=,10,+,20,*,30,;,<EOF>", 169))
        self.assertTrue(TestLexer.test("x: float = (10 - 5) / 2;", "x,:,float,=,(,10,-,5,),/,2,;,<EOF>", 170))
        self.assertTrue(TestLexer.test("x: bool = !true;", "x,:,bool,=,!,true,;,<EOF>", 171))
        self.assertTrue(TestLexer.test("b: bool = 10 > 5 || 20 < 15;", "b,:,bool,=,10,>,5,||,20,<,15,;,<EOF>", 172))
        self.assertTrue(TestLexer.test("x: string = \"a\" + \"b\" + \"c\";", "x,:,string,=,a,+,b,+,c,;,<EOF>", 173))
        self.assertTrue(TestLexer.test("x: int = (10 + 5) * 2;", "x,:,int,=,(,10,+,5,),*,2,;,<EOF>", 174))
        self.assertTrue(TestLexer.test("b: bool = true && false || true;", "b,:,bool,=,true,&&,false,||,true,;,<EOF>", 175))
        self.assertTrue(TestLexer.test("x: float = 10.5 - 5.25;", "x,:,float,=,10.5,-,5.25,;,<EOF>", 176))
        self.assertTrue(TestLexer.test("a: int = 10; b: bool = true && false;", "a,:,int,=,10,;,b,:,bool,=,true,&&,false,;,<EOF>", 176))
        self.assertTrue(TestLexer.test("a: string = \"Hello world!\"; b: string = \"Single quote\";", "a,:,string,=,Hello world!,;,b,:,string,=,Single quote,;,<EOF>", 177))
        self.assertTrue(TestLexer.test("a: bool = !true || false && !(5 < 10);", "a,:,bool,=,!,true,||,false,&&,!,(,5,<,10,),;,<EOF>", 179))
        self.assertTrue(TestLexer.test("a: bool = 5 == 5 && 10 > 5 || 20 < 15;", "a,:,bool,=,5,==,5,&&,10,>,5,||,20,<,15,;,<EOF>", 180))
        self.assertTrue(TestLexer.test("a: string = \"Hello\" + \"world\";", "a,:,string,=,Hello,+,world,;,<EOF>", 181))
        self.assertTrue(TestLexer.test("a: int[] = {1, 2, 3}; b: int = a[1];", "a,:,int,[,],=,{,1,,,2,,,3,},;,b,:,int,=,a,[,1,],;,<EOF>", 182))
        self.assertTrue(TestLexer.test("a: int = (5 + 6) * (3 - 2) / (4 % 3);", "a,:,int,=,(,5,+,6,),*,(,3,-,2,),/,(,4,%,3,),;,<EOF>", 183))
        self.assertTrue(TestLexer.test("a: int = 5; b: bool = true; c: string = \"Hello\";", "a,:,int,=,5,;,b,:,bool,=,true,;,c,:,string,=,Hello,;,<EOF>", 184))
        self.assertTrue(TestLexer.test("a: int = 5; // This is a comment\nb: bool = true;", "a,:,int,=,5,;,b,:,bool,=,true,;,<EOF>", 185))
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 186))
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 187))
        self.assertTrue(TestLexer.test("a = 10;", "a,=,10,;,<EOF>", 188))
        self.assertTrue(TestLexer.test("b: bool = 10 > 5 || 20 < 15;", "b,:,bool,=,10,>,5,||,20,<,15,;,<EOF>", 189))
        self.assertTrue(TestLexer.test("a = 10.5e-2;", "a,=,10.5e-2,;,<EOF>", 190))
        self.assertTrue(TestLexer.test("if true then false else true end", "if,true,then,false,else,true,end,<EOF>", 191))
        self.assertTrue(TestLexer.test("d: int = (5 + 2) * 3;", "d,:,int,=,(,5,+,2,),*,3,;,<EOF>", 192))
        self.assertTrue(TestLexer.test("e: bool = !(true && false) && true;", "e,:,bool,=,!,(,true,&&,false,),&&,true,;,<EOF>", 193))
        self.assertTrue(TestLexer.test("f : int = 10 % 3;", "f,:,int,=,10,%,3,;,<EOF>", 194))
        self.assertTrue(TestLexer.test("g : bool = 10.0 >= 9.9;", "g,:,bool,=,10.0,>=,9.9,;,<EOF>", 195))
        self.assertTrue(TestLexer.test("break;", "break,;,<EOF>", 196))
        self.assertTrue(TestLexer.test("continue;", "continue,;,<EOF>", 197))
        self.assertTrue(TestLexer.test("while (i < 10) do i = i + 1;", "while,(,i,<,10,),do,i,=,i,+,1,;,<EOF>", 198))
        self.assertTrue(TestLexer.test("return 1 + 2 * 3 - 4 / 2;", "return,1,+,2,*,3,-,4,/,2,;,<EOF>", 199))
