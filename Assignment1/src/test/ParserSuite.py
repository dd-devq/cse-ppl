import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):

        self.assertTrue(TestParser.test("delta, alpha: integer = 3,6;", "successful", 201))

        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))


        self.assertTrue(TestParser.test("""
        x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }
        """, "successful" ,203))

        input = """4*43; main: function void() {}"""
        expect = "Error on line 1 col 0: 4"
        self.assertTrue(TestParser.test(input, expect, 204))
        
        input = """
        main: function void() {
            for (i = n + 1, i < 10, i + 1) {
                writeInt(i);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

        input = """
        main: function void() {
        i: integer = 0; 
            while (i != 10) {
                writeInt(i);
                i = i + 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

        input = """
        main: function void() {
            i: integer = 0; 
            do {
                writeInt(i);
                i = i + 1;

                {
                    a:integer = 0;
                    a = a + 1;
                }

            } while (i != 10)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

        input = """main: function integer(n: false, s: string) {
            return s[n];
        }"""
        expect = "Error on line 1 col 26: false"
        self.assertTrue(TestParser.test(input, expect, 208))

        input = """b: boolean = 10 > 5 ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

        input = """func: function integer(a: integer, b: integer) {
            return a + b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

        input = """x: integer = 5 + 2 * 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

        input = """y: boolean = 3 > 5 ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

        input = """main: function void() {
                    if (5 < 3) {
                        return;
                    }
                    else {
                        print("5 is not less than 3");
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

        input = """s: string = "Hello world!";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

        input = """a: array[5] of string = {"a", "b", "c", "d", "e"};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

        input = """arr: array[3] of boolean = {true, false, !(3 > 5)};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

        input = """func: function boolean(a: boolean, b: boolean, c: boolean) {
            return (a && b) || c;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

        input = """flag: boolean = true && false;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

        input = """x: integer = 5 - -2;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

        input = """b: boolean = !(true && false) || (false && true);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))


        input = """a: integer = 10 / 2 * 3 - 5;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

        input = """main: function void() {
            print("Hello, world!");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

        input = """bar: function void(x: integer, y: float) {
                    print("x = ", x, " y = ", y);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))


        input = """baz: function boolean () {
                    return true;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

        input = """qux: function string(x: integer, y: float) {
            return "x = " + str(x) + ", y = " + str(y);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

        input = """quux: function void(z: integer , w: float ) {
                    print(\"z = \", z, \" w = \", w);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

        input = """corge: function void(args: integer) {
                    for (i = 0, i < 10, i + 1) {
                        print(args[i], " ");                    
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))


        input = """garply: function integer(x: integer, y: integer) {
                    a: integer = x + y;
                    b: float = x / y;
                    return a + b;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))


        input = """waldo: function boolean(x: integer, y: integer) {
                    if ( x < y ) {
                        return x - y;                    
                    }
                    else {
                        return x + y;                    
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))





