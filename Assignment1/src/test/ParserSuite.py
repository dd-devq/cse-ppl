import unittest
from TestUtils import TestParser



class ParserSuite(unittest.TestCase):
    def test_simple_program1(self):
        """Simple program"""
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_simple_program2(self):
        """Simple program"""
        input = """4*43; main: function void() {}"""
        expect = "Error on line 1 col 0: 4"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_simple_program3(self):
        """Simple program"""
        input = """a: float = 3.; main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_simple_program4(self):
        """Simple program"""
        input = """a: string = "Hey boyyyyy"; main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_simple_program5(self):
        """Simple program"""
        input = """main: function integer(n: integer, s: string) {
            return s[n];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))


    def test_type6(self):
        """Error on type"""
        input = """main: function integer(n: lmao, s: string) {
            return s[n];
        }"""
        expect = "Error on line 1 col 26: lmao"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_type7(self):
        """Error on type"""
        input = """main: money integer(n: integer, s: string) {
            return s[n];
        }"""
        expect = "Error on line 1 col 6: money"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_type8(self):
        """Error on type"""
        input = """main: function integer(n: array, s: string) {
            foo(r);
        }"""
        expect = "Error on line 1 col 31: ,"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_type9(self):
        """Error on type"""
        input = """x: double = 3.0"""
        expect = "Error on line 1 col 3: double"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_type10(self):
        """Error on type"""
        input = """main: function integer(n: array[3,2] of integer, s: string) {
            foo(r);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_program_structure1(self):
        """Program structure 1"""
        input = """"""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_program_structure2(self):
        """Program structure 2"""
        input = """x: float = 3.;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_program_structure3(self):
        """Program structure 3"""
        input = """r: function integer () {}
        f: string = "For fun"; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_program_structure4(self):
        """Program structure 4"""
        input = """bedge = 1;"""
        expect = "Error on line 1 col 6: ="
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_program_structure5(self):
        """Program structure 5"""
        input = """r: function integer () {} _r_1: function void () {} _____rr: function auto(){}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_program_structure6(self):
        """Program structure 6"""
        input = """continue: function float()"""
        expect = "Error on line 1 col 0: continue"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_program_structure7(self):
        """Program structure 7"""
        input = """deez: function float(inherit out nut: integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_program_structure8(self):
        """Program structure 8"""
        input = """deez: function float(inherdit out nut: integer) {}"""
        expect = "Error on line 1 col 30: out"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_program_structure9(self):
        """Program structure 9"""
        input = """deez: function float(inherit out nut: integer) {return}"""
        expect = "Error on line 1 col 54: }"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_program_structure10(self):
        """Program structure 10"""
        input = """deez: function float(inherit out nut: integer) {return -nut * 4;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_func_params1(self):
        """Function params 1"""
        input = """main: function void(n: integer, arr: array[3,2] of string) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_func_params2(self):
        """Function params 2"""
        input = """main: function void(n: integer, out s: string, inherit f: float, tr: auto) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_func_params3(self):
        """Function params 3"""
        input = """main: function void(n: true) {}"""
        expect = "Error on line 1 col 23: true"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_func_params4(self):
        """Function params 4"""
        input = """main: function void(n: boolean) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_func_params5(self):
        """Function params 5"""
        input = """main: function void(n, s, t) {}"""
        expect = "Error on line 1 col 21: ,"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_func_params6(self):
        """Function params 6"""
        input = """main: function void(n: string,,) {}"""
        expect = "Error on line 1 col 30: ,"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_func_params7(self):
        """Function params 7"""
        input = """main: function void(inherit n) {}"""
        expect = "Error on line 1 col 29: )"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_func_params8(self):
        """Function params 8"""
        input = """main: function void(out n: void) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_func_params9(self):
        """Function params 9"""
        input = """main: function void("s") {}"""
        expect = "Error on line 1 col 20: s"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_func_params10(self):
        """Function params 10"""
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_variable_decl1(self):
        """Variable dec1"""
        input = """main: function void() {
            x: float = 2.3e2;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_variable_decl2(self):
        """Variable dec2"""
        input = """main: function void() {
            x, y: integer = 2, 3;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_variable_decl3(self):
        """Variable dec2"""
        input = """main: function void() {
            x, y: integer = 3;
        }"""
        expect = "Error on line 2 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_variable_decl4(self):
        """Variable dec4"""
        input = """main: function void() {
            x, y, z: string = "","","";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_variable_decl5(self):
        """Variable dec5"""
        input = """main: function void() {
            x, y, z: string;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_variable_decl6(self):
        """Variable dec6"""
        input = """main: function void() {
            x, y, z: string = toString(a), toString(b), toString(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_variable_decl7(self):
        """Variable dec7"""
        input = """main: function void() {
            x, y, z: string = integer,int,int;
        }"""
        expect = "Error on line 2 col 30: integer"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_variable_decl8(self):
        """Variable dec8"""
        input = """main: function void() {
            x, y, z: string = int, int, int;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_variable_decl9(self):
        """Variable dec9"""
        input = """main: function void() {
            arr: array[3, 3] of integer;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_variable_decl10(self):
        """Variable dec10"""
        input = """main: function void() {
            arr: array[3, 3] of integer = {{2,3,4},{5,6,7},{8,9,10}};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_expression1(self):
        """Expression 1"""
        input = """main: function void() {
            a: integer = 3;
            b: integer = 4;
            c: integer = b % a + 4;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_expression2(self):
        """Expression 2"""
        input = """main: function void() {
            a: integer = 3;
            b: integer = 4;
            c: integer = {{2,3}}[3];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_expression3(self):
        """Expression 3"""
        input = """a: float = !true % 5 / 4;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_expression4(self):
        """Expression 4"""
        input = """a: integer = 4; a = str(a)::"af"; """
        expect = "Error on line 1 col 18: ="
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_expression5(self):
        """Expression 5"""
        input = """a: integer = 4;
        main: function void() {
            a = str(a)::"af";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_expression6(self):
        """Expression 6"""
        input = """a: integer = 4;
        main: function void() {
            a = true || false && true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_expression7(self):
        """Expression 7"""
        input = """a: integer = 4;
        main: function void() {
            a = true || false && true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_expression8(self):
        """Expression 8"""
        input = """a: integer = 4;
        main: function void() {
            a = arr[b, c, c::"string"];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_array1(self):
        """Array 1"""
        input = """a: integer = 4;
        main: function void() {
            a: array[3] of float = {{f,g,h},{"M","J","D"},{1+3,3+4,5+7}}[3];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_array2(self):
        """Array 2"""
        input = """a: array[5] of float;
        main: function void() {
            a[4] = {"DF",DSDS,__proto__};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_array3(self):
        """Array 3"""
        input = """a: array[5] of float;
        main: function void() {
            a[4, 4 && 5 + 1] = {"DF",DSDS,__proto__};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_array3(self):
        """Array 3"""
        input = """a: array[5] of float;
        main: function void() {
            a[4, 4 && 5 + 1][44] = {"DF",DSDS,__proto__};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_array4(self):
        """Array 4"""
        input = """a: array[5] of float;
        main: function void() {
            a: array[0] of integer;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_array5(self):
        """Array 5"""
        input = """
        main: function void() {
            a: array[2][3] of integer;
        }"""
        expect = "Error on line 3 col 23: ["
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_array6(self):
        """Array 6"""
        input = """
        main: function void() {
            a: array[2] of integer = {};
        }"""
        expect = "Error on line 3 col 38: }"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_assign_stmt1(self):
        """Assignment statement 1"""
        input = """
        main: function void() {
            a, b, c: array[2] of integer = {1,2,3};
        }"""
        expect = "Error on line 3 col 50: ;"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_assign_stmt2(self):
        """Assignment statement 2"""
        input = """
        main: function void() {
            a, b, c: array[3] of integer = {1,2,3},{1,2,3},{1,2,3};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_assign_stmt3(self):
        """Assignment statement 3"""
        input = """
        main: function void() {
            a, b, c: array[3] of integer, integer, integer;
        }"""
        expect = "Error on line 3 col 40: ,"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_assign_stmt4(self):
        """Assignment statement 4"""
        input = """
        main: function void() {
            a: float = 33;
            b: integer = 43_3e4;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_assign_stmt5(self):
        """Assignment statement 5"""
        input = """
        main: function void() {
            a = foo(24, f);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_assign_stmt6(self):
        """Assignment statement 6"""
        input = """
        main: function void() {
            a[4, 5] = bar(b[4], c[5]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_condition_stmt1(self):
        """Condition statement 1"""
        input = """
        main: function void() {
            if (true) a = a + 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_condition_stmt2(self):
        """Condition statement 2"""
        input = """
        main: function void() {
            if (true) a = a + 1;
            else a = a - 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_condition_stmt2(self):
        """Condition statement 2"""
        input = """
        main: function void() {
            if (a == 1) {
                return a == 1;
            }
            else {
                return a == 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_condition_stmt3(self):
        """Condition statement 3"""
        input = """
        main: function void() {
            if (a + 4 == 5) {
                return a + 1;
            }
            else {
                if (a + 1 == 3) {
                    return a + 1;
                }
                return a + 2;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_condition_stmt4(self):
        """Condition statement 4"""
        input = """
        main: function void() {
            if (a > 4) {
                return a + 1;
            }
            if (a > 3)
                return 12;
            if (a == 1)
                return 5;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_condition_stmt4(self):
        """Condition statement 4"""
        input = """
        main: function void() {
            if (a > 4) {
                return a + 1;
            }
            if (a > 3)
                return 12;
            if (a == 1)
                return 5;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_condition_stmt5(self):
        """Condition statement 5"""
        input = """
        main: function void() {
            if else a = 3 ;
        }"""
        expect = "Error on line 3 col 15: else"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_condition_stmt6(self):
        """Condition statement 6"""
        input = """
        main: function void() {
            if (a <= 1 )
                a = 1;
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_for_stmt1(self):
        """For statement 1"""
        input = """
        main: function void() {
            for (i = 0, i < 10, i + 1) {
                writeLn(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_for_stmt1(self):
        """For statement 1"""
        input = """
        main: function void() {
            for (i = 0, i < 10, i + 1) {
                writeLn(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_for_stmt2(self):
        """For statement 2"""
        input = """
        main: function void() {
            for (i = 0, i + 1) {
                writeLn(i);
            }
        }"""
        expect = "Error on line 3 col 29: )"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_for_stmt3(self):
        """For statement 3"""
        input = """
        main: function void() {
            for (i = 0, i + 1) {
                writeLn(i);
            }
        }"""
        expect = "Error on line 3 col 29: )"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_for_stmt4(self):
        """For statement 4"""
        input = """
        main: function void() {
            for (true = 1, 10, i + 2) {
                writeLn(i);
            }
        }"""
        expect = "Error on line 3 col 17: true"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_for_stmt5(self):
        """For statement 5"""
        input = """
        main: function void() {
            for (i = 0, 10, i + 2) {
                writeLn(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_for_stmt6(self):
        """For statement 6"""
        input = """
        main: function void() {
            for (i = 0, 10, i + 2) 
                writeLn(i);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_while_stmt1(self):
        """While statement 1"""
        input = """
        main: function void() {
            while ( a < 0 ) {
                a = a + 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_while_stmt2(self):
        """While statement 2"""
        input = """
        main: function void() {
            while ( a < 0 ) {
                a + 1 = 3;
            }
        }"""
        expect = "Error on line 4 col 22: ="
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_while_stmt3(self):
        """While statement 3"""
        input = """
        main: function void() {
            while ( a < 0 ) 
                a = a + 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_while_stmt4(self):
        """While statement 4"""
        input = """
        main: function void() {
            while ( a < 0, f == 1 ) 
                a = a + 1;
        }"""
        expect = "Error on line 3 col 25: ,"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_do_while_stmt1(self):
        """Do While statement 1"""
        input = """
        main: function void() {
            do {
                writeLn("A = " :: str(a));
                a = a + 1;
            } while (a <= 10);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_do_while_stmt2(self):
        """Do While statement 2"""
        input = """
        main: function void() {
            do {
                writeLn("A = " :: str(a));
                a = a + 1;
            } while (a <= 10)
        }"""
        expect = "Error on line 7 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_do_while_stmt3(self):
        """Do While statement 3"""
        input = """
        main: function void() {
            do {
                writeLn("A = " :: str(a));
                a = a + 1;
            }
        }"""
        expect = "Error on line 7 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_do_while_stmt4(self):
        """Do While statement 4"""
        input = """
        main: function void() {
            do
                a = a + 1; 
            while (a <= 10);
        }"""
        expect = "Error on line 4 col 16: a"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_break_stmt1(self):
        """Break statement 1"""
        input = """
        main: function void() {
            do {
                writeLn("A = " :: str(a));
                a = a + 1;
                break;
            } while (a <= 10);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_break_stmt1(self):
        """Break statement 1"""
        input = """
        main: function void() {
            do {
                writeLn("A = " :: str(a));
                a = a + 1;
                break a;
            } while (a <= 10);
        }"""
        expect = "Error on line 6 col 22: a"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_break_stmt2(self):
        """Break statement 2"""
        input = """
        main: function void() {
            do {
                writeLn("A = " :: str(a));
                a = a + 1;
                break a;
            } while (a <= 10);
        }"""
        expect = "Error on line 6 col 22: a"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_break_stmt3(self):
        """Break statement 3"""
        input = """
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            for (index = 0, index < 10, index + 1) {
                if (a[index, index + 1] == i)
                    break;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_break_stmt4(self):
        """Break statement 4"""
        input = """
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            for (index = 0, index < 10, index + 1) {
                a[index, index] = 5;
            }
            break;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_continue_stmt1(self):
        """Continue statement 1"""
        input = """
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            for (index = 0, index < 10, index + 1) {
                if (a[index, index + 1] == i)
                    continue;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_continue_stmt2(self):
        """Continue statement 2"""
        input = """
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            for (index = 0, index < 10, index + 1) {
                if (a[index, index + 1] == i)
                    continue gogo;
            }
        }"""
        expect = "Error on line 6 col 29: gogo"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_continue_stmt3(self):
        """Continue statement 3"""
        input = """
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            continue;
            continue;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_continue_stmt4(self):
        """Continue statement 4"""
        input = """
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            do {
                continue;
                break;
            } while(!true);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_return_stmt1(self):
        """Return statement 1"""
        input = """
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            return a;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_return_stmt2(self):
        """Return statement 2"""
        input = """
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            return auto;
        }"""
        expect = "Error on line 4 col 19: auto"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_return_stmt2(self):
        """Return statement 2"""
        input = """
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            return auto;
        }"""
        expect = "Error on line 4 col 19: auto"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_call_stmt1(self):
        """Call statement 1"""
        input = """
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            return foo(3 + x, 4.0 / y);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_call_stmt2(self):
        """Call statement 1"""
        input = """
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            return foo(3 + x, 4.0 / y);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_block_stmt1(self):
        """Block statement 1"""
        input = """
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            {
                test: integer = 1;
                return test;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_block_stmt2(self):
        """Block statement 2"""
        input = """
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        main: function void() {
            {}
            {}
            {}
            {
                test: integer = 1;
                return test;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_leetcode_excercise1(self):
        """Full program 1: simple rail fence encryption"""
        input = """
        railfence_encrypt: function string(plain: string, key: integer) {
            if (key <= 1)
                return plain;
            
            matrix: array[15] of string; // 15 is the maximum number of rows

            row, dir: integer = 0, -1;

            for (i = 0, i < length(plain), i + 1) {
                if ((j == key - 1) || (j == 0))
                    dir = dir * -1;
                matrix[j] = matrix[j]::plain[i];
                if (dir == 1)
                    j = j + 1;
                else
                    j = j - 1;
            }

            ciphertext: string;
            for (i = 0, i < key, i + 1) {
                ciphertext = ciphertext::matrix[i];
            }

            return ciphertext;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_leetcode_excercise2(self):
        """Full program 1: simple rail fence encryption enhance"""
        input = """
        railfence_encrypt: function string(plain: string, key: integer, indent: integer) {
            if (key <= 1)
                return plain;
            
            matrix: array[15] of string; // 15 is the maximum number of rows

            row, dir: integer = 0, -1;

            for (i = 0, i < length(plain), i + 1) {
                if ((j == key - 1) || (j == 0))
                    dir = dir * -1;
                matrix[j] = matrix[j]::plain[i];
                if (dir == 1)
                    j = j + 1;
                else
                    j = j - 1;
            }

            ciphertext: string;
            for (i = 0, i < key, i + 1) {
                ciphertext = ciphertext::matrix[i];
            }

            return ciphertext;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_leetcode_excercise3(self):
        """Full program 1: simple rail fence decryption"""
        input = """
        railfence_decryption: function string(ciphertext: string, key: integer) {
            if (key <= 1)
                return ciphertext;
            
            matrix: array[15, 15] of string;
            /* 
                15 for each row
                maxium 15 rows
            */

            dir: boolean = true;
            // true for down, false for up

            row, col: integer = 0, 0;

            for (i = 0, i < length(ciphertext), i + 1) {
                if (row == 0) dir = true;
                if (row == key - 1) dir = false;
                rail[row][col] = null;
                
                col = col + 1;
                if (dir)
                    row = row + 1;
                else row = row - 1;
            }

            index: integer = 0;
            for (i = 0, i < key, i + 1)
                for (j = 0, j < length(ciphertext), j + 1)
                    if ((matrix[i, j] == null) && (index < length(ciphertext))) {
                        matrix[i, j] = ciphertext[index];
                        index = index + 1;
                    }
            
            row = 0; col = 0;
            result: string;
            for ( i=0, i< length(ciphertext), i + 1 )
            {
                // check the direction of flow
                if (row == 0)
                    dir = true;
                if (row == key - 1)
                    dir = false;
 
                // place the marker
                if (rail[row][col] != "*")
                    result = result::rail[row][col];
                col = col + 1;
 
                // find the next row using direction flag
                if (dir)
                    row = row + 1;
                else row = row - 1;
            }

            return result;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_traded_testcase1(self):
        """Testcase for a testcase"""
        input = """
        jowd: function string() {
            if(true) {
                a[5] = a[1] + 2;
                b[9] = b[5] || false;
            } else;
        }
        """
        expect = "Error on line 6 col 18: ;"
        self.assertTrue(TestParser.test(input, expect, 298))




