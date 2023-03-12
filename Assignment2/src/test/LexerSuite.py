import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_identifier1(self):
        """test 1"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test_identifier2(self):
        """test 2"""
        self.assertTrue(TestLexer.test("_fa23 hoang123", "_fa23,hoang123,<EOF>", 102))

    def test_identifier3(self):
        """test 3"""
        self.assertTrue(TestLexer.test("aa?bb", "aa,Error Token ?", 103))

    def test_identifier4(self):
        """test 4"""
        self.assertTrue(TestLexer.test("130a12", "130,a12,<EOF>", 104))

    def test_mixed5(self):
        """test 5"""
        self.assertTrue(TestLexer.test("___JohN_C3N4 /*Comment*/ 213_4331", "___JohN_C3N4,2134331,<EOF>", 105))

    def test_indetifier6(self):
        """test 6"""
        self.assertTrue(TestLexer.test("___JohN_C3N4", "___JohN_C3N4,<EOF>", 106))

    def test_mixed7(self):
        """test 7"""
        self.assertTrue(TestLexer.test("___JohN_C3N4 //GAGAGAG\n1e4", "___JohN_C3N4,1e4,<EOF>", 107))
        
    def test_operators8(self):
        """test 8"""
        self.assertTrue(TestLexer.test("&&&", "&&,Error Token &", 108))

    def test_operators9(self):
        """test 9"""
        self.assertTrue(TestLexer.test("!0.1023", "!,0.1023,<EOF>", 109))

    def test_operators10(self):
        """test 10"""
        self.assertTrue(TestLexer.test("[\"fa\",2]", "[,fa,,,2,],<EOF>", 110))
    
    def test_operators11(self):
        """test 11"""
        self.assertTrue(TestLexer.test("0.123a3", "0.123,a3,<EOF>", 111))

    def test_operators12(self):
        """test 12"""
        self.assertTrue(TestLexer.test("!==+!", "!=,=,+,!,<EOF>", 112))
    
    def test_mixed13(self):
        """test 13"""
        self.assertTrue(TestLexer.test("0.123a3 \"Demacia\"", "0.123,a3,Demacia,<EOF>", 113))
    
    def test_separators14(self):
        """test 14"""
        self.assertTrue(TestLexer.test("(((((((af * 3 + p[3_4])))))))", "(,(,(,(,(,(,(,af,*,3,+,p,[,34,],),),),),),),),<EOF>", 114))

    def test_separators15(self):
        """test 16"""
        self.assertTrue(TestLexer.test(":::", "::,:,<EOF>", 115))

    def test_separators16(self):
        """test 17"""
        self.assertTrue(TestLexer.test("<<<<<", "<,<,<,<,<,<EOF>", 116))

    def test_separators17(self):
        """test 17"""
        self.assertTrue(TestLexer.test("{{][#]}}", "{,{,],[,Error Token #", 117))

    def test_separators18(self):
        """test 18"""
        self.assertTrue(TestLexer.test(".,.,....,.", ".,,,.,,,.,.,.,.,,,.,<EOF>", 118))

    def test_separators_mixed19(self):
        """test 19"""
        self.assertTrue(TestLexer.test("aa123 + 12_34 + integer(\"y\") ", "aa123,+,1234,+,integer,(,y,),<EOF>", 119))

    def test_integer_literal20(self):
        """test 20"""
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 120))

    def test_integer_literal21(self):
        """test 21"""
        self.assertTrue(TestLexer.test("01", "0,1,<EOF>", 121))

    def test_integer_literal22(self):
        """test 21"""
        self.assertTrue(TestLexer.test("0_1abcd", "0,_1abcd,<EOF>", 122))

    def test_integer_literal23(self):
        """test 23"""
        self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 123))

    def test_integer_literal24(self):
        """test 24"""
        self.assertTrue(TestLexer.test("123_4", "1234,<EOF>", 124))

    def test_integer_literal25(self):
        """test 25"""
        self.assertTrue(TestLexer.test("76890_1", "768901,<EOF>", 125))

    def test_integer_literal26(self):
        """test 26"""
        self.assertTrue(TestLexer.test("'001'", "Error Token '", 126))

    def test_integer_literal27(self):
        """test 27"""
        self.assertTrue(TestLexer.test("112467_32_3123_", "112467323123,_,<EOF>", 127))

    def test_mixed_28(self):
        """test 28"""
        self.assertTrue(TestLexer.test("2_____223ab___a", "2,_____223ab___a,<EOF>", 128))

    def test_integer_literal29(self):
        """test 29"""
        self.assertTrue(TestLexer.test("4123_ 3231__", "4123,_,3231,__,<EOF>", 129))

    def test_integer_literal30(self):
        """test 30"""
        self.assertTrue(TestLexer.test("122__032", "122,__032,<EOF>", 130))

    def test_float31(self):
        """test 31"""
        self.assertTrue(TestLexer.test("1e2", "1e2,<EOF>", 131))
    
    def test_float32(self):
        """test 31"""
        self.assertTrue(TestLexer.test("1.01", "1.01,<EOF>", 132))

    def test_integer33(self):
        """test 33"""
        self.assertTrue(TestLexer.test("-666_3777_888", "-,6663777888,<EOF>", 133))

    def test_float34(self):
        """test 34"""
        self.assertTrue(TestLexer.test("14e-12", "14e-12,<EOF>", 134))

    def test_float35(self):
        """test 35"""
        self.assertTrue(TestLexer.test("-1.23e2", "-,1.23e2,<EOF>", 135))

    def test_float36(self):
        """test 36"""
        self.assertTrue(TestLexer.test("0.0", "0.0,<EOF>", 136))

    def test_float37(self):
        """test 37"""
        self.assertTrue(TestLexer.test("-1.23E-4", "-,1.23E-4,<EOF>", 137))

    def test_float38(self):
        """test 38"""
        self.assertTrue(TestLexer.test("6.02214076e+23", "6.02214076e+23,<EOF>", 138))

    def test_float39(self):
        """test 39"""
        self.assertTrue(TestLexer.test("1,34", "1,,,34,<EOF>", 139))

    def test_float40(self):
        """test 40"""
        self.assertTrue(TestLexer.test("0.20000000000", "0.20000000000,<EOF>", 140))

    def test_string_literal41(self):
        """test 41"""
        input = "\"I am Le Hoang\""
        expect = "I am Le Hoang,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 141))

    def test_string_literal42(self):
        """test 42"""
        input =  """ "I am Le Hoang" 
        "What about you ?" """
        expect = "I am Le Hoang,What about you ?,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 142))

    def test_string_literal43(self):
        """test 43"""
        input = "\"I am Le Hoang\\nYup I am at newline\""
        expect = "I am Le Hoang\\nYup I am at newline,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 143))

    def test_string_literal44(self):
        """test 44"""
        input = "\"I am Le Hoang\"\"ffff"
        expect = "I am Le Hoang,Unclosed String: ffff"
        self.assertTrue(TestLexer.test(input, expect, 144))

    def test_string_literal45(self):
        """test 45"""
        input = "\"Say this: \'Me skill issue.\'\""
        expect = "Say this: \'Me skill issue.\',<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 145))

    def test_string_literal46(self):
        """test 46"""
        input = "\"This is illegal, dont escape me: \\g \""
        expect = "Illegal Escape In String: This is illegal, dont escape me: \\g"
        self.assertTrue(TestLexer.test(input, expect, 146))

    def test_string_literal47(self):
        """test 47"""
        input = "\"abc \\n \\f 's def"
        expect = "Unclosed String: abc \\n \\f 's def"
        self.assertTrue(TestLexer.test(input, expect, 147))

    def test_string_literal48(self):
        """test 48"""
        input = """ "This is a \\t string \\n containing tab " \n "He asked \\n me: \\"Where \\"is \\" John?" "I am not closed"""
        expect = """This is a \\t string \\n containing tab ,He asked \\n me: \\"Where \\"is \\" John?,Unclosed String: I am not closed"""
        self.assertTrue(TestLexer.test(input, expect, 148))

    def test_string_literal49(self):
        """test 49"""
        input = "\"I have an escape sequence \\\"Here it is \\k\\\"\""
        expect = "Illegal Escape In String: I have an escape sequence \\\"Here it is \k"
        self.assertTrue(TestLexer.test(input, expect, 149))

    def test_string_literal50(self):
        """test 50"""
        input = "\"\\a He is a man\""
        expect = "Illegal Escape In String: \\a"
        self.assertTrue(TestLexer.test(input, expect, 150))

    def test_string_literal51(self):
        """test 51"""
        input = "\"\" + ssrf + 123_442.323e-4"
        expect = ",+,ssrf,+,123442.323e-4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 151))

    def test_string_literal52(self):
        """test 52"""
        input = "\" + ssrf + 123_442.323e-4"
        expect = "Unclosed String:  + ssrf + 123_442.323e-4"
        self.assertTrue(TestLexer.test(input, expect, 152))

    def test_string_literal53(self):
        """test 53"""
        input = "\"\"\"\"\"\"\"\""
        expect = ",,,,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 153))

    def test_string_literal54(self):
        """test 54"""
        input = "\"\"\"\"\"\"\"\"\""
        expect = ",,,,Unclosed String: "
        self.assertTrue(TestLexer.test(input, expect, 154))

    def test_string_literal55(self):
        """test 55"""
        input = "true"
        expect = "true,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 155))

    def test_string_literal56(self):
        """test 56"""
        input = "\"\"\"\"\"\"\"\"\""
        expect = ",,,,Unclosed String: "
        self.assertTrue(TestLexer.test(input, expect, 156))

    def test_string_literal57(self):
        """test 57"""
        input = "\"\"\"\"\"\"\"\"\""
        expect = ",,,,Unclosed String: "
        self.assertTrue(TestLexer.test(input, expect, 157))

    def test_string_literal58(self):
        """test 58"""
        input = "\"\"\"\"\"\"\"\"\""
        expect = ",,,,Unclosed String: "
        self.assertTrue(TestLexer.test(input, expect, 158))

    def test_boolean59(self):
        """test 59"""
        input = "true false true false"
        expect = "true,false,true,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 159))

    def test_boolean60(self):
        """test 60"""
        input = "true31"
        expect = "true31,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 160))

    def test_boolean61(self):
        """test 61"""
        input = "false21"
        expect = "false21,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))

    def test_boolean62(self):
        """test 62"""
        input = "false"
        expect = "false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 162))

    def test_boolean63(self):
        """test 63"""
        input = "true"
        expect = "true,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 163))

    def test_keywords64(self):
        """test 64"""
        input = "inherit"
        expect = "inherit,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 164))

    def test_keywords65(self):
        """test 65"""
        input = "void"
        expect = "void,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 165))
    
    def test_keywords66(self):
        """test 66"""
        input = "array"
        expect = "array,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 166))

    def test_keywords67(self):
        """test 67"""
        input = "out"
        expect = "out,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 167))

    def test_keywords68(self):
        """test 68"""
        input = "continue"
        expect = "continue,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 168))

    def test_keywords69(self):
        """test 69"""
        input = "float"
        expect = "float,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 169))

    def test_keywords70(self):
        """test 70"""
        input = "return"
        expect = "return,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 170))

    def test_keywords71(self):
        """test 71"""
        input = "of"
        expect = "of,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 171))

    def test_array72(self):
        """test 72"""
        input = "of"
        expect = "of,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 172))

    def test_array73(self):
        """test 73"""
        input = "{1,2}"
        expect = "{,1,,,2,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 173))

    def test_array74(self):
        """test 74"""
        input = "{ 1 + 2, 3 + 4 }"
        expect = "{,1,+,2,,,3,+,4,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 174))

    def test_array75(self):
        """test 75"""
        input = "{\"Yasuo\", \"Gangplank\", \"Sett\"}"
        expect = "{,Yasuo,,,Gangplank,,,Sett,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 175))

    def test_array76(self):
        """test 76"""
        input = "{\"Yasuo\" :: \"and\" :: \"Yone\"}"
        expect = "{,Yasuo,::,and,::,Yone,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 176))

    def test_array77(self):
        """test 77"""
        input = "{ -1 * 3 + 5, {a, b, c}}"
        expect = "{,-,1,*,3,+,5,,,{,a,,,b,,,c,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 177)) 

    def test_parser78(self):
        """test 78"""
        input = """
        a : integer;
        b: string;
        """
        expect = "a,:,integer,;,b,:,string,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 178))

    def test_parser79(self):
        """test 79"""
        input = """
        fact: function integer(n: integer) {
            if (n == 0)
                return 1;
            else return n * fact(n - 1);
        }
        """
        expect = "fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 179)) 

    def test_parser80(self):
        """test 80"""
        input = """
        x: integer = 65;
        fact: function integer(n: integer) {
            if (n == 0)
                return 1;
            else return n * fact(n - 1);
        }
        """
        expect = "x,:,integer,=,65,;,fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 180)) 

    def test_parser81(self):
        """test 81"""
        input = """
        x: integer = 65;
        y: float = 1e433333333333333;
        """
        expect = "x,:,integer,=,65,;,y,:,float,=,1e433333333333333,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 181))
    
    def test_parser82(self):
        """test 82"""
        input = """
        rofl: function(inherit out time: integer) {
            return "haha" * time;
        }
        """
        expect = "rofl,:,function,(,inherit,out,time,:,integer,),{,return,haha,*,time,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 182))

    def test_parser83(self):
        """test 83"""
        input = """
        main: function void () {}
        """
        expect = "main,:,function,void,(,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 183))

    def test_parser84(self):
        """test 84"""
        input = """
        a: array[2, 3] of float;
        """
        expect = "a,:,array,[,2,,,3,],of,float,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 184)) 

    def test_parser85(self):
        """test 85"""
        input = """
        x: integer = 65;
        fact: function integer(n: integer) {
            if (n == 0)
                return 1;
            else return n * fact(n - 1);
        }
        """
        expect = "x,:,integer,=,65,;,fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 185)) 

    def test_parser86(self):
        """test 86"""
        input = """
        return -1;
        """
        expect = "return,-,1,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 186)) 

    def test_comment87(self):
        """test 87"""
        input = """
        a = 43_3e4;
        /* Hey hey
        luv u */
        """
        expect = "a,=,433e4,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 187))

    def test_parser88(self):
        """test 88"""
        input = """a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            {}
            {}
            {}
            {
                test: integer = 1;
                return test;
        }
        """
        expect = "a,:,array,[,2,,,3,],of,integer,=,{,{,2,,,3,,,4,},,,{,5,,,6,,,7,},},;,main,:,function,void,(,),{,{,},{,},{,},{,test,:,integer,=,1,;,return,test,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 188))

    def test_parsers89(self):
        """test 89"""
        input = """
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            return foo(3 + x, 4.0 / y);
        }
        """
        expect = "a,:,array,[,2,,,3,],of,integer,=,{,{,2,,,3,,,4,},,,{,5,,,6,,,7,},},;,main,:,function,void,(,),{,return,foo,(,3,+,x,,,4.0,/,y,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 189))
    
    def test_parsers90(self):
        """test 90"""
        input = """ a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            continue;
            continue;
        }
        """
        expect = "a,:,array,[,2,,,3,],of,integer,=,{,{,2,,,3,,,4,},,,{,5,,,6,,,7,},},;,main,:,function,void,(,),{,continue,;,continue,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 190))

    def test_parsers91(self):
        """test 91"""
        input = """a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            for (index = 0, index < 10, index + 1) {
                if (a[index, index + 1] == i)
                    continue gogo;
            }
        }
        """
        expect = "a,:,array,[,2,,,3,],of,integer,=,{,{,2,,,3,,,4,},,,{,5,,,6,,,7,},},;,main,:,function,void,(,),{,for,(,index,=,0,,,index,<,10,,,index,+,1,),{,if,(,a,[,index,,,index,+,1,],==,i,),continue,gogo,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc\t", "abc,<EOF>", 192))

    def test_intlit(self):
        """test integer literal"""
        self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 193))

    def test_floatlit(self):
        """test float literal"""
        self.assertTrue(TestLexer.test("1_234.567", "1234.567,<EOF>", 194))

    def test_stringlit(self):
        """test string literal"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """,
                        """He asked me: \\"Where is John?\\",<EOF>""", 195))

    def test_stringlit(self):
        """test string literal"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """,
                        """He asked me: \\"Where is John?\\",<EOF>""", 196))
