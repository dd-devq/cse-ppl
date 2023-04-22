import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test_no_entry(self):
    #     input = """x, y, z: integer;"""
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 407))
        
    # def test_no_entry2(self):
    #     input = Program([VarDecl("a", IntegerType()), VarDecl("c", FloatType())])
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 412))
        
    # def test_full_program(self):    
    #     input = """main: function void() {
    #         // Line comment
    #         /*
    #             Block comment between line comments
    #         */
    #         // Line comment
    #     }"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 408))
        
    # def test_vardecl(self):    
    #     input = """a : float = 1 ;
    #     b : float = a + 2 ;
    #     c : integer = 2.3 ;
    #     """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FloatLit(2.3))"""
    #     self.assertTrue(TestChecker.test(input, expect, 409))
        
    # def test_redecl1(self):
    #     input = Program([VarDecl("x", IntegerType()),VarDecl("y", IntegerType()),VarDecl("x", FloatType())])
    #     expect = """Redeclared Variable: x"""
    #     self.assertTrue(TestChecker.test(input, expect, 410))
        
    # def test_redecl2(self):    
    #     input = """a : float = 1 ;
    #     a : integer = 2 ;
    #     """
    #     expect = """Redeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 411))
        
    # def test_vardecl1(self):    
    #     input = """a : integer = 1 ;
    #     b : integer = a + 2 ;
    #     c : float = 2.3 ;
    #     d : float = c + b + a + 69; 
    #     """
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 412))
        
    # def test_vardecl2(self):    
    #     input = """a : integer = 1 ;
    #     b : integer = a + 2 ;
    #     c : float = 2.3 ;
    #     d : float = c + b + a + 69;
    #     main: function void() {
    #         a : integer = 1 ;
    #         b : integer = a + 2 ;
    #         c : float = 2.3 ;
    #         d : float = c + b + a + 69;
    #     } 
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 413))
        
    # def test_vardecl3(self):    
    #     input = """a : integer = 1 ;
    #     b : integer = a + 2 ;
    #     c : float = 2.3 ;
    #     d : float = c + b + a + 69;
    #     main: function void(a : integer, b : float) {
    #         a : integer = 1 ;
    #         b : integer = a + 2 ;
    #         c : float = 2.3 ;
    #         d : float = c + b + a + 69;
    #     } 
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 414))
        
    # def test_vardecl4(self):    
    #     input = """a : integer = 1 ;
    #     b : integer = a + 2 ;
    #     c : float = 2.3 ;
    #     d : float = c + b + s + 69;
    #     main: function void(a : integer, b : float) {
    #         a : integer = 1 ;
    #         b : integer = a + 2 ;
    #         c : float = 2.3 ;
    #         d : float = c + b + a + 69;
    #     } 
    #     """
    #     expect = """Undeclared Identifier: s"""
    #     self.assertTrue(TestChecker.test(input, expect, 415))
        
    # def test_vardecl5(self):    
    #     input = """a : integer = 1 ;
    #     b : integer = a + 2 ;
    #     c : float = 2.3 ;
    #     d : float = c + b + a + 69;
    #     psum: function integer(a : integer){}
    #     main: function void(){}
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 416))
        
    # def test_vardecl6(self):    
    #     input = """a : integer = 1 ;
    #     b : integer = a + 2 ;
    #     c : float = 2.3 ;
    #     d : float = c + b + a + 69;
    #     main: function void(a : integer, b : float) {
    #         a : integer = 1 ;
    #         b : integer = a + 2 ;
    #         c : float = 2.3 ;
    #         d : float = c + b + a + 69;
    #     }
    #     main1: function void(a : integer, b : float) {
    #         a : integer = 1 ;
    #         b : integer = a + 2 ;
    #         c : float = 2.3 ;
    #         d : float = c + b + a + 69;
    #     }
    #     main2: function void(a : integer, b : float) {
    #         a : integer = 1 ;
    #         b : integer = a + 2 ;
    #         c : float = 2.3 ;
    #         d : float = c + b + a + 69;
    #     }
    #     psum: function integer(a : integer){}   
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 417))
        
    # def test_vardecl7(self):    
    #     input = """a : integer = 1 ;
    #     b : integer = a + 2 ;
    #     c : float = 2.3 ;
    #     d : float = c + b + a + 69;
    #     psum: function integer(a : integer){}
    #     main: function void(a : integer, b : float) {
    #         a : integer = 1 ;
    #         b : integer = a + 2 ;
    #         c : float = 2.3 ;
    #         d : float = c + b + a + 69;
    #         psum(1);
    #         psum(1,2);
    #     } 
    #     """
    #     expect = """Type mismatch in statement: CallStmt(psum, IntegerLit(1), IntegerLit(2))"""
    #     self.assertTrue(TestChecker.test(input, expect, 418))
        
    # def test_vardecl8(self):    
    #     input = """a : integer = 1 ;
    #     b : integer = a + 2 ;
    #     c : float = 2.3 ;
    #     d : float = c + b + a + 69;
    #     psum: function integer(a : float){}
    #     main: function void(a : integer, b : float) {
    #         a : integer = 1 ;
    #         b : integer = a + 2 ;
    #         c : float = 2.3 ;
    #         d : float = c + b + a + 69;
    #         psum(1);
    #         psum(1,2);
    #     } 
    #     """
    #     expect = """Type mismatch in statement: CallStmt(psum, IntegerLit(1), IntegerLit(2))"""
    #     self.assertTrue(TestChecker.test(input, expect, 419))
        
    # def test_vardecl9(self):    
    #     input = """a : integer = 1 ;
    #     b : integer = a + 2 ;
    #     c : float = 2.3 ;
    #     d : float = c + b + a + 69;
    #     psum: function integer(a : integer){}
    #     main: function void(a : integer, b : float) {
    #         a : integer = 1 ;
    #         b : integer = a + 2 ;
    #         c : float = 2.3 ;
    #         d : float = c + b + a + 69;
    #         psum(1);
    #         psum(1.0);
    #     } 
    #     """
    #     expect = """Type mismatch in statement: CallStmt(psum, FloatLit(1.0))"""
    #     self.assertTrue(TestChecker.test(input, expect, 420))
        
    # def test_vardecl10(self):    
    #     input = """a : auto = 10;
    #     b : auto = "hello" ;
    #     c : auto = a < 100;
    #     d : auto;
    #     """
    #     expect = """Invalid Variable: d"""
    #     self.assertTrue(TestChecker.test(input, expect, 421))
        
    # def test_vardecl11(self):    
    #     input = """a : auto = 10;
    #     b : auto = "hello" ;
    #     c : auto = a < 100;
    #     d : auto = 1.0;
    #     e : auto = d + a;
    #     """
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 422))
        
    # def test_vardecl12(self):    
    #     input = """a : auto = 10;
    #     b : auto = "hello" ;
    #     c : auto = a < 100;
    #     d : auto = 1.0;
    #     e : auto = d + a;
    #     foo : function integer (a : integer) {}
    #     g : auto = foo(0) + a;
    #     """
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 423))
        
    # def test_vardecl13(self):    
    #     input = """a : auto = 10;
    #     b : auto = "hello" ;
    #     c : auto = a < 100;
    #     d : auto = 1.0;
    #     e : auto = d + a;
    #     foo : function integer (a : integer, b : float, c : boolean) {}
    #     f : auto = foo(a,d,c) + a;
    #     """
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 424))
        
    # def test_vardecl14(self):    
    #     input = """a : auto = 10;
    #     b : auto = "hello" ;
    #     c : auto = a < 100;
    #     d : auto = 1.0;
    #     e : auto = d + a;
    #     foo : function integer (a : integer, b : float, c : boolean) {}
    #     f : auto = foo(a,d,c) + a;
    #     segg : function void (a : integer){}
    #     g : integer = segg(a) + f;
    #     """
    #     expect = """Type mismatch in expression: BinExpr(+, FuncCall(segg, [Id(a)]), Id(f))"""
    #     self.assertTrue(TestChecker.test(input, expect, 425))
        
    # def test_vardecl15(self):    
    #     input = """a : auto = 10;
    #     b : auto = "hello" ;
    #     c : auto = a < 100;
    #     d : auto = 1.0;
    #     e : auto = d + a;
    #     foo : function integer (a : integer, b : float, c : boolean) {}
    #     segg : function float (a : integer){}
    #     main : function void (){
    #         f : auto = foo(a,d,c) + a;
    #         g : float = segg(a) + f;
    #         {
    #             a : float;
    #             {
    #                 b : auto;
    #             }
    #         }    
    #     }
    #     """
    #     expect = """Invalid Variable: b"""
    #     self.assertTrue(TestChecker.test(input, expect, 426))
        
    # def test_vardecl16(self):    
    #     input = """a : auto = 10;
    #     b : auto = "hello" ;
    #     c : auto = a < 100;
    #     d : auto = 1.0;
    #     e : auto = d + a;
    #     foo : function integer (a : integer, b : float, c : boolean) {}
    #     segg : function float (a : integer){}
    #     main : function void (){
    #         f : auto = foo(a,d,c) + a;
    #         g : float = segg(a) + f;
    #         {
    #             a : float;
    #             {
    #                 b : auto = 2;
    #             }
    #         }    
    #     }
    #     main : function integer (){}
    #     """
    #     expect = """Redeclared Function: main"""
    #     self.assertTrue(TestChecker.test(input, expect, 427))
        
    # def test_vardecl17(self):    
    #     input = """a : auto = 10;
    #     b : auto = "hello" ;
    #     c : auto = a < 100;
    #     d : auto = 1.0;
    #     e : auto = d + a;
    #     foo : function integer (a : integer, b : float, c : boolean) {}
    #     segg : function float (a : integer){}
    #     main : function void (){
    #         f : auto = foo(a,d,c) + a;
    #         g : float = segg(a) + f;
    #         {
    #             a : float;
    #             {
    #                 b : auto = 2;
    #             }
    #         }    
    #     }
    #     mainn : function integer (a : integer, b : boolean, a : integer){}
    #     """
    #     expect = """Redeclared Parameter: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 428))
        
    # def test_vardecl18(self):    
    #     input = """a : auto = 10;
    #     b : auto = "hello" ;
    #     c : auto = a < 100;
    #     d : auto = 1.0;
    #     e : auto = d + a;
    #     foo : function integer (a : integer, b : float, c : boolean) {}
    #     segg : function float (a : integer){}
    #     main : function void (){
    #         f : auto = foo(a,d,c) + a;
    #         g : float = segg(a) + f;
    #         {
    #             a : float;
    #             {
    #                 b : auto = 2;
    #             }
    #         }    
    #     }
    #     mainn : function integer (a : integer, b : boolean, c : integer){
    #         d : auto = e;
    #     }
    #     main2 : function auto ()
    #     {
    #         // main2(); // can we call a function inside itself ??   
    #     }
    #     main3 : function integer()
    #     {
    #         main2();    
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 429))
        
    # def test_vardecl19(self):    
    #     input = """foo : function auto ( a : integer , b : integer ) {}
    #     main : function void (){
    #         a : float = foo(1,2) ;
    #         b : integer = foo(1,2) + 1 ;
    #         foo(1,2);    
    #     }
    #     """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]), IntegerLit(1)))"""
    #     self.assertTrue(TestChecker.test(input, expect, 430))
        
    # def test_vardecl20(self):    
    #     input = """foo : function auto ( a : integer , b : integer ) {}
    #     main : function void (){
    #         b : integer = foo(1,2) + 1 ;
    #         foo(1,2);    
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 431))
        
    # def test_vardecl21(self):    
    #     input = """foo : function auto ( a : integer , b : integer ) {}
    #     main : function void (){
    #         foo(1,2);    
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 432))
        
    # def test_vardecl22(self):    
    #     input = """foo : function auto ( a : integer , b : integer ) {}
    #     main : function void (){
    #         a : integer = foo(1,2) ;
    #         b : float = foo(1,2) + 1 ;
    #         foo(1,2);    
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 433))
    
    # def test_vardecl23(self):    
    #     input = """foo : function auto ( a : integer , b : integer ) {}
    #     args : function void (){}
    #     main : function void (){
    #         a : integer = foo(1,2) ;
    #         b : float = foo(1,2) + 1 ;
    #         foo(1,2);
    #         b = foo(a, a + 2);
    #         c : integer = b + args();    
    #     }
    #     """
    #     expect = """Type mismatch in expression: BinExpr(+, Id(b), FuncCall(args, []))"""
    #     self.assertTrue(TestChecker.test(input, expect, 434))
        
    # def test_vardecl24(self):    
    #     input = """demo : function integer (a : integer){}
    #     kuro: function boolean inherit demo {}
    #     main : function void (){
    #         a : integer = foo(1,2) ;
    #         b : float = foo(1,2) + 1 ;
    #         foo(1,2);
    #         b = foo(a, a + 2);
    #         c : integer = b + args();    
    #     }
    #     """
    #     expect = """Type mismatch in expression: BinExpr(+, Id(b), FuncCall(args, []))"""
    #     self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test_op(self):    
        input = """a : boolean = 2.1 == 3.2;
        main : function void (){
            a : integer = foo(1,2) ;
            b : float = foo(1,2) + 1 ;
            foo(1,2);
            b = foo(a, a + 2);
            c : integer = b + args();    
        }
        """
        expect = """Type mismatch in expression: BinExpr(==, FloatLit(2.1), FloatLit(3.2))"""
        self.assertTrue(TestChecker.test(input, expect, 436))
        
    def test_op1(self):    
        input = """a : boolean = 2.1 >= 3.2;
        b : boolean = a + true;
        main : function void (){
            a : integer = foo(1,2) ;
            b : float = foo(1,2) + 1 ;
            foo(1,2);
            b = foo(a, a + 2);
            c : integer = b + args();    
        }
        """
        expect = """Type mismatch in expression: BinExpr(+, Id(a), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test_op2(self):    
        input = """a : boolean = 2.1 >= 3.2;
        c : boolean = true;
        b : boolean = a + !c;
        main : function void (){
            a : integer = foo(1,2) ;
            b : float = foo(1,2) + 1 ;
            foo(1,2);
            b = foo(a, a + 2);
            c : integer = b + args();    
        }
        """
        expect = """Type mismatch in expression: BinExpr(+, Id(a), UnExpr(!, Id(c)))"""
        self.assertTrue(TestChecker.test(input, expect, 438))
        
    def test_op3(self):    
        input = """arg : function auto (){}
        mai : function string ()
        {
            arg();
        }
        a : boolean = 2.1 >= 3.2;
        c : boolean = true;
        b : boolean = a + arg();
        main : function void (){
            a : integer = foo(1,2) ;
            b : float = foo(1,2) + 1 ;
            foo(1,2);
            b = foo(a, a + 2);
            c : integer = b + args();    
        }
        """
        expect = """Type mismatch in expression: BinExpr(+, Id(a), FuncCall(arg, []))"""
        self.assertTrue(TestChecker.test(input, expect, 439))
        
    def test_op3(self):    
        input = """arg : function auto (){}
        mai : function string ()
        {
            arg();
        }
        a : string = "hey";
        b : string = "dawg";
        c : string = a :: b; 
        d : auto = c :: mai();
        e : boolean = mai() :: "wassup";
        main : function void (){
            a : integer = foo(1,2) ;
            b : float = foo(1,2) + 1 ;
            foo(1,2);
            b = foo(a, a + 2);
            c : integer = b + args();    
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(e, BooleanType, BinExpr(::, FuncCall(mai, []), StringLit(wassup)))"""
        self.assertTrue(TestChecker.test(input, expect, 440))
        
    def test_op4(self):    
        input = """arg : function auto (){}
        mai : function string ()
        {
            arg();
        }
        a : string = "hey";
        b : string = "dawg";
        c : string = a :: b; 
        d : auto = c :: mai();
        e : boolean = mai() :: 1;
        main : function void (){
            a : integer = foo(1,2) ;
            b : float = foo(1,2) + 1 ;
            foo(1,2);
            b = foo(a, a + 2);
            c : integer = b + args();    
        }
        """
        expect = """Type mismatch in expression: BinExpr(::, FuncCall(mai, []), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 441))
    
    def test_op5(self):    
        input = """arg : function auto (){}
        mai : function string ()
        {
            arg();
        }
        a : string = "hey";
        b : string = "dawg";
        c : string = a :: b; 
        d : auto = c :: mai();
        e : boolean = 2 :: 1;
        main : function void (){
            a : integer = foo(1,2) ;
            b : float = foo(1,2) + 1 ;
            foo(1,2);
            b = foo(a, a + 2);
            c : integer = b + args();    
        }
        """
        expect = """Type mismatch in expression: BinExpr(::, IntegerLit(2), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 442))
        
    def test_op6(self):    
        input = """arg : function auto (){}
        mai : function string ()
        {
            arg();
        }
        a : string = "hey";
        b : string = "dawg";
        c : string = a :: b; 
        d : auto = c :: mai();
        e : boolean = 2 :: 1.0;
        main : function void (){
            a : integer = foo(1,2) ;
            b : float = foo(1,2) + 1 ;
            foo(1,2);
            b = foo(a, a + 2);
            c : integer = b + args();    
        }
        """
        expect = """Type mismatch in expression: BinExpr(::, IntegerLit(2), FloatLit(1.0))"""
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test_op7(self):    
        input = """arg : function auto (){}
        mai : function string ()
        {
            arg();
        }
        foo : function string (a: integer, b: integer)
        {
            arg();
        }
        a : string = "hey";
        b : string = "dawg";
        c : string = a :: b; 
        d : auto = c :: mai();
        e : auto = mai() :: foo(1, 2);
        main : function void (){
            a : integer = foo(1,2) ;
            b : float = foo(1,2) + 1 ;
            foo(1,2);
            b = foo(a, a + 2);
            c : integer = b + args();    
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]))"""
        self.assertTrue(TestChecker.test(input, expect, 444))
        
    def test_op8(self):    
        input = """a : integer;
        main : function void()
        {
            a = 2.0;
        }    
        """
        expect = """Type mismatch in statement: AssignStmt(Id(a), FloatLit(2.0))"""
        self.assertTrue(TestChecker.test(input, expect, 445))
        
    def test_op9(self):    
        input = """foo: function void(a: auto, b: integer) {
         a = a + b; // Line cause TypeMismatchInExpression ?
        }  
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 446))
        
    def test_op10(self):    
        input = """foo: function void (a: float, b: integer) {}
        main: function void ()
        {
            foo(1,2);
            fo();
        }
        """
        expect = """Undeclared Function: fo"""
        self.assertTrue(TestChecker.test(input, expect, 447))
        
    def test_op11(self):    
        input = """foo: function void (a: float, b: integer) {}
        main: function void (fang : integer)
        {
            foo(1,2);
        }
        //f: float = true;
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 448))
    
    def test_op12(self):    
        input = """foo: function void (a: float, b: integer) {}
        b: function auto (){}
        main: function void ()
        {
            foo(1,2);
            a : float;
            c : auto = a + b;
        }
        f: float = true;
        """
        expect = """Undeclared Identifier: b"""
        self.assertTrue(TestChecker.test(input, expect, 448))
    
    def test_op13(self):    
        input = """foo: function void (a: float, b: integer) {}
        b: function auto (){}
        main: function void ()
        {
            foo(1,2);
            a : float;
            c : auto = a + b();
        }
        f: float = true;
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(f, FloatType, BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 449))
        
    def test_scope(self):    
        input = """x: integer = foo();
        foo: function integer (){}
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 450))
        
    def test_scope1(self):    
        input = """foo: function void (){
          x = 5;
          x: integer;
        }
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 451))
        
    def test_scope2(self):    
        input = """oo: function void(){
            {
                x = 5;
            }
            x: integer;
        }
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 452))
        
    def test_scope3(self):    
        input = """oo: function integer(){
            x: integer;
        }
        oo: integer = 2;
        """
        expect = """Redeclared Variable: oo"""
        self.assertTrue(TestChecker.test(input, expect, 453))
        
    def test_scope4(self):    
        input = """boo: integer = 2;
        boo: function integer(){
            x: integer;
        }
        coo: auto;
        """
        expect = """Redeclared Function: boo"""
        self.assertTrue(TestChecker.test(input, expect, 454))
        
    def test_scope5(self):    
        input = """a: auto = foo(1, 2);
        foo: function auto() { }
        """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test_scope6(self):    
        input = """a: integer = 23; //1
        b: auto; //2
        foo: function void(a: integer, b: float) {} //3
        bar: function void() inherit foo {} //4
        a: function void() {} //5
        """
        expect = """Invalid Variable: b"""
        self.assertTrue(TestChecker.test(input, expect, 456))
        
    def test_scope7(self):    
        input = """a: integer = 23; //1
        b: auto; //2
        foo: function void(a: integer, b: float) {} //3
        bar: function void() inherit foo {} //4
        a: function integer() {} //5
        a: function void() {} //6
        """
        expect = """Invalid Variable: b"""
        self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test_scope8(self):    
        input = """a: integer = 1;
        foo: function void (b : integer) inherit a {}
        a: function string (inherit c : string) {}
        """
        expect = """Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input, expect, 458))
        
    def test_scope9(self):    
        input = """boom: integer = 2;
        a: integer = boo();
        boo: function integer(){
            x: integer;
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 459))
        
    def test_scope10(self):    
        input = """boo: integer = 2;
        a: integer = boo();
        boo: function integer(){
            x: integer;
        }
        """
        expect = """Redeclared Function: boom"""
        self.assertTrue(TestChecker.test(input, expect, 460))
        
    def test_scope11(self):    
        input = """boo: auto = 2;
        a: auto = boo;
        main: function integer(){
            x: integer;
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 461))
                    
    def test_auto(self):    
        input = """foo: function void(a: auto, b: auto) {
            a = a :: b; // can 2 auto be type-infer by the operators
        }
        main: function void(a : integer)
        {}       
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 489))
             
    def test_invalid_vardecl_1(self):    
        input = Program([VarDecl("a", IntegerType(), IntegerLit(5)), VarDecl("c", AutoType())])
        expect = """Invalid Variable: c"""
        self.assertTrue(TestChecker.test(input, expect, 490))