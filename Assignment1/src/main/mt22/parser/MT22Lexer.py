# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01df\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\7\2\u008e\n\2\f\2\16\2\u0091\13")
        buf.write("\2\3\2\3\2\6\2\u0095\n\2\r\2\16\2\u0096\7\2\u0099\n\2")
        buf.write("\f\2\16\2\u009c\13\2\3\2\5\2\u009f\n\2\3\2\3\2\3\3\3\3")
        buf.write("\5\3\u00a5\n\3\3\3\6\3\u00a8\n\3\r\3\16\3\u00a9\3\3\3")
        buf.write("\3\5\3\u00ae\n\3\3\3\3\3\3\4\3\4\5\4\u00b4\n\4\3\5\3\5")
        buf.write("\7\5\u00b8\n\5\f\5\16\5\u00bb\13\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)")
        buf.write("\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3")
        buf.write("\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\69\u017f\n9\r9\169\u0180\39\3")
        buf.write("9\79\u0185\n9\f9\169\u0188\139\3:\3:\5:\u018c\n:\3:\6")
        buf.write(":\u018f\n:\r:\16:\u0190\3;\3;\3<\3<\5<\u0197\n<\3=\3=")
        buf.write("\3=\3>\3>\3>\3?\3?\3?\7?\u01a2\n?\f?\16?\u01a5\13?\3@")
        buf.write("\6@\u01a8\n@\r@\16@\u01a9\3@\3@\3A\3A\3A\3A\7A\u01b2\n")
        buf.write("A\fA\16A\u01b5\13A\3A\3A\3B\3B\3B\3B\7B\u01bd\nB\fB\16")
        buf.write("B\u01c0\13B\3B\3B\3B\3B\3B\3C\3C\3C\3D\3D\7D\u01cc\nD")
        buf.write("\fD\16D\u01cf\13D\3D\5D\u01d2\nD\3D\3D\3E\3E\7E\u01d8")
        buf.write("\nE\fE\16E\u01db\13E\3E\3E\3E\3\u01be\2F\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\2m\2o\2q\2s\2u\2w\2y\2{\2}\67")
        buf.write("\1778\u00819\u0083:\u0085;\u0087<\u0089=\3\2\16\3\2\62")
        buf.write("\62\3\2\62;\3\2\63;\5\2C\\aac|\4\2GGgg\4\2--//\6\2\n\f")
        buf.write("\16\17$$^^\n\2$$))^^ddhhppttvv\t\2))^^ddhhppttvv\5\2\13")
        buf.write("\f\16\17\"\"\4\2\f\f\17\17\6\3\n\f\16\17$$^^\2\u01ea\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2")
        buf.write("\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2")
        buf.write("\u0089\3\2\2\2\3\u009e\3\2\2\2\5\u00ad\3\2\2\2\7\u00b3")
        buf.write("\3\2\2\2\t\u00b5\3\2\2\2\13\u00bf\3\2\2\2\r\u00c2\3\2")
        buf.write("\2\2\17\u00cb\3\2\2\2\21\u00ce\3\2\2\2\23\u00d3\3\2\2")
        buf.write("\2\25\u00dc\3\2\2\2\27\u00e1\3\2\2\2\31\u00e7\3\2\2\2")
        buf.write("\33\u00eb\3\2\2\2\35\u00f2\3\2\2\2\37\u00f8\3\2\2\2!\u00fc")
        buf.write("\3\2\2\2#\u00ff\3\2\2\2%\u0107\3\2\2\2\'\u010d\3\2\2\2")
        buf.write(")\u0112\3\2\2\2+\u011a\3\2\2\2-\u0120\3\2\2\2/\u0128\3")
        buf.write("\2\2\2\61\u012f\3\2\2\2\63\u0134\3\2\2\2\65\u013a\3\2")
        buf.write("\2\2\67\u013d\3\2\2\29\u0140\3\2\2\2;\u0142\3\2\2\2=\u0144")
        buf.write("\3\2\2\2?\u0147\3\2\2\2A\u014a\3\2\2\2C\u014d\3\2\2\2")
        buf.write("E\u0150\3\2\2\2G\u0152\3\2\2\2I\u0154\3\2\2\2K\u0156\3")
        buf.write("\2\2\2M\u0158\3\2\2\2O\u015a\3\2\2\2Q\u015c\3\2\2\2S\u015e")
        buf.write("\3\2\2\2U\u0161\3\2\2\2W\u0163\3\2\2\2Y\u0165\3\2\2\2")
        buf.write("[\u0167\3\2\2\2]\u0169\3\2\2\2_\u016b\3\2\2\2a\u016d\3")
        buf.write("\2\2\2c\u016f\3\2\2\2e\u0171\3\2\2\2g\u0173\3\2\2\2i\u0175")
        buf.write("\3\2\2\2k\u0177\3\2\2\2m\u0179\3\2\2\2o\u017b\3\2\2\2")
        buf.write("q\u017e\3\2\2\2s\u0189\3\2\2\2u\u0192\3\2\2\2w\u0196\3")
        buf.write("\2\2\2y\u0198\3\2\2\2{\u019b\3\2\2\2}\u019e\3\2\2\2\177")
        buf.write("\u01a7\3\2\2\2\u0081\u01ad\3\2\2\2\u0083\u01b8\3\2\2\2")
        buf.write("\u0085\u01c6\3\2\2\2\u0087\u01c9\3\2\2\2\u0089\u01d5\3")
        buf.write("\2\2\2\u008b\u008f\5m\67\2\u008c\u008e\5k\66\2\u008d\u008c")
        buf.write("\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f")
        buf.write("\u0090\3\2\2\2\u0090\u009a\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0092\u0094\5i\65\2\u0093\u0095\5k\66\2\u0094\u0093\3")
        buf.write("\2\2\2\u0095\u0096\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\u0099\3\2\2\2\u0098\u0092\3\2\2\2\u0099")
        buf.write("\u009c\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\u009f\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009f\t")
        buf.write("\2\2\2\u009e\u008b\3\2\2\2\u009e\u009d\3\2\2\2\u009f\u00a0")
        buf.write("\3\2\2\2\u00a0\u00a1\b\2\2\2\u00a1\4\3\2\2\2\u00a2\u00a4")
        buf.write("\5q9\2\u00a3\u00a5\5s:\2\u00a4\u00a3\3\2\2\2\u00a4\u00a5")
        buf.write("\3\2\2\2\u00a5\u00ae\3\2\2\2\u00a6\u00a8\5k\66\2\u00a7")
        buf.write("\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00a7\3\2\2\2")
        buf.write("\u00a9\u00aa\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\5")
        buf.write("s:\2\u00ac\u00ae\3\2\2\2\u00ad\u00a2\3\2\2\2\u00ad\u00a7")
        buf.write("\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0\b\3\3\2\u00b0")
        buf.write("\6\3\2\2\2\u00b1\u00b4\5\61\31\2\u00b2\u00b4\5\63\32\2")
        buf.write("\u00b3\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\b\3\2\2")
        buf.write("\2\u00b5\u00b9\5u;\2\u00b6\u00b8\5w<\2\u00b7\u00b6\3\2")
        buf.write("\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba")
        buf.write("\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc")
        buf.write("\u00bd\5u;\2\u00bd\u00be\b\5\4\2\u00be\n\3\2\2\2\u00bf")
        buf.write("\u00c0\7f\2\2\u00c0\u00c1\7q\2\2\u00c1\f\3\2\2\2\u00c2")
        buf.write("\u00c3\7h\2\2\u00c3\u00c4\7w\2\2\u00c4\u00c5\7p\2\2\u00c5")
        buf.write("\u00c6\7e\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8\7k\2\2\u00c8")
        buf.write("\u00c9\7q\2\2\u00c9\u00ca\7p\2\2\u00ca\16\3\2\2\2\u00cb")
        buf.write("\u00cc\7k\2\2\u00cc\u00cd\7h\2\2\u00cd\20\3\2\2\2\u00ce")
        buf.write("\u00cf\7g\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7u\2\2\u00d1")
        buf.write("\u00d2\7g\2\2\u00d2\22\3\2\2\2\u00d3\u00d4\7e\2\2\u00d4")
        buf.write("\u00d5\7q\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7\7v\2\2\u00d7")
        buf.write("\u00d8\7k\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da\7w\2\2\u00da")
        buf.write("\u00db\7g\2\2\u00db\24\3\2\2\2\u00dc\u00dd\7c\2\2\u00dd")
        buf.write("\u00de\7w\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7q\2\2\u00e0")
        buf.write("\26\3\2\2\2\u00e1\u00e2\7d\2\2\u00e2\u00e3\7t\2\2\u00e3")
        buf.write("\u00e4\7g\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7m\2\2\u00e6")
        buf.write("\30\3\2\2\2\u00e7\u00e8\7h\2\2\u00e8\u00e9\7q\2\2\u00e9")
        buf.write("\u00ea\7t\2\2\u00ea\32\3\2\2\2\u00eb\u00ec\7t\2\2\u00ec")
        buf.write("\u00ed\7g\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef\7w\2\2\u00ef")
        buf.write("\u00f0\7t\2\2\u00f0\u00f1\7p\2\2\u00f1\34\3\2\2\2\u00f2")
        buf.write("\u00f3\7y\2\2\u00f3\u00f4\7j\2\2\u00f4\u00f5\7k\2\2\u00f5")
        buf.write("\u00f6\7n\2\2\u00f6\u00f7\7g\2\2\u00f7\36\3\2\2\2\u00f8")
        buf.write("\u00f9\7q\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb\7v\2\2\u00fb")
        buf.write(" \3\2\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe\7h\2\2\u00fe")
        buf.write("\"\3\2\2\2\u00ff\u0100\7k\2\2\u0100\u0101\7p\2\2\u0101")
        buf.write("\u0102\7j\2\2\u0102\u0103\7g\2\2\u0103\u0104\7t\2\2\u0104")
        buf.write("\u0105\7k\2\2\u0105\u0106\7v\2\2\u0106$\3\2\2\2\u0107")
        buf.write("\u0108\7c\2\2\u0108\u0109\7t\2\2\u0109\u010a\7t\2\2\u010a")
        buf.write("\u010b\7c\2\2\u010b\u010c\7{\2\2\u010c&\3\2\2\2\u010d")
        buf.write("\u010e\7x\2\2\u010e\u010f\7q\2\2\u010f\u0110\7k\2\2\u0110")
        buf.write("\u0111\7f\2\2\u0111(\3\2\2\2\u0112\u0113\7d\2\2\u0113")
        buf.write("\u0114\7q\2\2\u0114\u0115\7q\2\2\u0115\u0116\7n\2\2\u0116")
        buf.write("\u0117\7g\2\2\u0117\u0118\7c\2\2\u0118\u0119\7p\2\2\u0119")
        buf.write("*\3\2\2\2\u011a\u011b\7h\2\2\u011b\u011c\7n\2\2\u011c")
        buf.write("\u011d\7q\2\2\u011d\u011e\7c\2\2\u011e\u011f\7v\2\2\u011f")
        buf.write(",\3\2\2\2\u0120\u0121\7k\2\2\u0121\u0122\7p\2\2\u0122")
        buf.write("\u0123\7v\2\2\u0123\u0124\7g\2\2\u0124\u0125\7i\2\2\u0125")
        buf.write("\u0126\7g\2\2\u0126\u0127\7t\2\2\u0127.\3\2\2\2\u0128")
        buf.write("\u0129\7u\2\2\u0129\u012a\7v\2\2\u012a\u012b\7t\2\2\u012b")
        buf.write("\u012c\7k\2\2\u012c\u012d\7p\2\2\u012d\u012e\7i\2\2\u012e")
        buf.write("\60\3\2\2\2\u012f\u0130\7v\2\2\u0130\u0131\7t\2\2\u0131")
        buf.write("\u0132\7w\2\2\u0132\u0133\7g\2\2\u0133\62\3\2\2\2\u0134")
        buf.write("\u0135\7h\2\2\u0135\u0136\7c\2\2\u0136\u0137\7n\2\2\u0137")
        buf.write("\u0138\7u\2\2\u0138\u0139\7g\2\2\u0139\64\3\2\2\2\u013a")
        buf.write("\u013b\7?\2\2\u013b\u013c\7?\2\2\u013c\66\3\2\2\2\u013d")
        buf.write("\u013e\7#\2\2\u013e\u013f\7?\2\2\u013f8\3\2\2\2\u0140")
        buf.write("\u0141\7@\2\2\u0141:\3\2\2\2\u0142\u0143\7>\2\2\u0143")
        buf.write("<\3\2\2\2\u0144\u0145\7@\2\2\u0145\u0146\7?\2\2\u0146")
        buf.write(">\3\2\2\2\u0147\u0148\7>\2\2\u0148\u0149\7?\2\2\u0149")
        buf.write("@\3\2\2\2\u014a\u014b\7(\2\2\u014b\u014c\7(\2\2\u014c")
        buf.write("B\3\2\2\2\u014d\u014e\7~\2\2\u014e\u014f\7~\2\2\u014f")
        buf.write("D\3\2\2\2\u0150\u0151\7#\2\2\u0151F\3\2\2\2\u0152\u0153")
        buf.write("\7-\2\2\u0153H\3\2\2\2\u0154\u0155\7\61\2\2\u0155J\3\2")
        buf.write("\2\2\u0156\u0157\7/\2\2\u0157L\3\2\2\2\u0158\u0159\7,")
        buf.write("\2\2\u0159N\3\2\2\2\u015a\u015b\7\'\2\2\u015bP\3\2\2\2")
        buf.write("\u015c\u015d\7?\2\2\u015dR\3\2\2\2\u015e\u015f\7<\2\2")
        buf.write("\u015f\u0160\7<\2\2\u0160T\3\2\2\2\u0161\u0162\7*\2\2")
        buf.write("\u0162V\3\2\2\2\u0163\u0164\7+\2\2\u0164X\3\2\2\2\u0165")
        buf.write("\u0166\7}\2\2\u0166Z\3\2\2\2\u0167\u0168\7\177\2\2\u0168")
        buf.write("\\\3\2\2\2\u0169\u016a\7]\2\2\u016a^\3\2\2\2\u016b\u016c")
        buf.write("\7_\2\2\u016c`\3\2\2\2\u016d\u016e\7.\2\2\u016eb\3\2\2")
        buf.write("\2\u016f\u0170\7=\2\2\u0170d\3\2\2\2\u0171\u0172\7\60")
        buf.write("\2\2\u0172f\3\2\2\2\u0173\u0174\7<\2\2\u0174h\3\2\2\2")
        buf.write("\u0175\u0176\7a\2\2\u0176j\3\2\2\2\u0177\u0178\t\3\2\2")
        buf.write("\u0178l\3\2\2\2\u0179\u017a\t\4\2\2\u017an\3\2\2\2\u017b")
        buf.write("\u017c\t\5\2\2\u017cp\3\2\2\2\u017d\u017f\5\3\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u017e\3\2\2\2")
        buf.write("\u0180\u0181\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0186\5")
        buf.write("e\63\2\u0183\u0185\5\3\2\2\u0184\u0183\3\2\2\2\u0185\u0188")
        buf.write("\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("r\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018b\t\6\2\2\u018a")
        buf.write("\u018c\t\7\2\2\u018b\u018a\3\2\2\2\u018b\u018c\3\2\2\2")
        buf.write("\u018c\u018e\3\2\2\2\u018d\u018f\5\3\2\2\u018e\u018d\3")
        buf.write("\2\2\2\u018f\u0190\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191")
        buf.write("\3\2\2\2\u0191t\3\2\2\2\u0192\u0193\7$\2\2\u0193v\3\2")
        buf.write("\2\2\u0194\u0197\n\b\2\2\u0195\u0197\5y=\2\u0196\u0194")
        buf.write("\3\2\2\2\u0196\u0195\3\2\2\2\u0197x\3\2\2\2\u0198\u0199")
        buf.write("\7^\2\2\u0199\u019a\t\t\2\2\u019az\3\2\2\2\u019b\u019c")
        buf.write("\7^\2\2\u019c\u019d\n\n\2\2\u019d|\3\2\2\2\u019e\u01a3")
        buf.write("\5o8\2\u019f\u01a2\5o8\2\u01a0\u01a2\5k\66\2\u01a1\u019f")
        buf.write("\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4~\3\2\2\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a6\u01a8\t\13\2\2\u01a7\u01a6\3\2\2")
        buf.write("\2\u01a8\u01a9\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa")
        buf.write("\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\b@\5\2\u01ac")
        buf.write("\u0080\3\2\2\2\u01ad\u01ae\7\61\2\2\u01ae\u01af\7\61\2")
        buf.write("\2\u01af\u01b3\3\2\2\2\u01b0\u01b2\n\f\2\2\u01b1\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3")
        buf.write("\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b6\u01b7\bA\5\2\u01b7\u0082\3\2\2\2\u01b8\u01b9\7")
        buf.write("\61\2\2\u01b9\u01ba\7,\2\2\u01ba\u01be\3\2\2\2\u01bb\u01bd")
        buf.write("\13\2\2\2\u01bc\u01bb\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be")
        buf.write("\u01bf\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c1\3\2\2\2")
        buf.write("\u01c0\u01be\3\2\2\2\u01c1\u01c2\7,\2\2\u01c2\u01c3\7")
        buf.write("\61\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\bB\5\2\u01c5\u0084")
        buf.write("\3\2\2\2\u01c6\u01c7\13\2\2\2\u01c7\u01c8\bC\6\2\u01c8")
        buf.write("\u0086\3\2\2\2\u01c9\u01cd\5u;\2\u01ca\u01cc\5w<\2\u01cb")
        buf.write("\u01ca\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2")
        buf.write("\u01cd\u01ce\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3")
        buf.write("\2\2\2\u01d0\u01d2\t\r\2\2\u01d1\u01d0\3\2\2\2\u01d2\u01d3")
        buf.write("\3\2\2\2\u01d3\u01d4\bD\7\2\u01d4\u0088\3\2\2\2\u01d5")
        buf.write("\u01d9\5u;\2\u01d6\u01d8\5w<\2\u01d7\u01d6\3\2\2\2\u01d8")
        buf.write("\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2")
        buf.write("\u01da\u01dc\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc\u01dd\5")
        buf.write("{>\2\u01dd\u01de\bE\b\2\u01de\u008a\3\2\2\2\31\2\u008f")
        buf.write("\u0096\u009a\u009e\u00a4\u00a9\u00ad\u00b3\u00b9\u0180")
        buf.write("\u0186\u018b\u0190\u0196\u01a1\u01a3\u01a9\u01b3\u01be")
        buf.write("\u01cd\u01d1\u01d9\t\3\2\2\3\3\3\3\5\4\b\2\2\3C\5\3D\6")
        buf.write("\3E\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTL = 1
    FLOATL = 2
    BOOLL = 3
    STRINGL = 4
    DO = 5
    FUNCTION = 6
    IF = 7
    ELSE = 8
    CONTINUE = 9
    AUTO = 10
    BREAK = 11
    FOR = 12
    RETURN = 13
    WHILE = 14
    OUT = 15
    OF = 16
    INHERIT = 17
    ARRAY = 18
    VOID = 19
    BOOLEAN = 20
    FLOAT = 21
    INTEGER = 22
    STRING = 23
    TRUE = 24
    FALSE = 25
    EQUAL = 26
    NOTEQUAL = 27
    GT = 28
    LT = 29
    GET = 30
    LET = 31
    AND = 32
    OR = 33
    NOT = 34
    ADD = 35
    DIV = 36
    SUB = 37
    MUL = 38
    MOD = 39
    ASSIGN = 40
    CONCATE = 41
    LB = 42
    RB = 43
    LCB = 44
    RCB = 45
    LSB = 46
    RSB = 47
    COMA = 48
    SEMI = 49
    DOT = 50
    COLON = 51
    UNDERSCORE = 52
    ID = 53
    WS = 54
    LINECMT = 55
    BLOCKCMT = 56
    ERROR_CHAR = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'do'", "'function'", "'if'", "'else'", "'continue'", "'auto'", 
            "'break'", "'for'", "'return'", "'while'", "'out'", "'of'", 
            "'inherit'", "'array'", "'void'", "'boolean'", "'float'", "'integer'", 
            "'string'", "'true'", "'false'", "'=='", "'!='", "'>'", "'<'", 
            "'>='", "'<='", "'&&'", "'||'", "'!'", "'+'", "'/'", "'-'", 
            "'*'", "'%'", "'='", "'::'", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "','", "';'", "'.'", "':'", "'_'" ]

    symbolicNames = [ "<INVALID>",
            "INTL", "FLOATL", "BOOLL", "STRINGL", "DO", "FUNCTION", "IF", 
            "ELSE", "CONTINUE", "AUTO", "BREAK", "FOR", "RETURN", "WHILE", 
            "OUT", "OF", "INHERIT", "ARRAY", "VOID", "BOOLEAN", "FLOAT", 
            "INTEGER", "STRING", "TRUE", "FALSE", "EQUAL", "NOTEQUAL", "GT", 
            "LT", "GET", "LET", "AND", "OR", "NOT", "ADD", "DIV", "SUB", 
            "MUL", "MOD", "ASSIGN", "CONCATE", "LB", "RB", "LCB", "RCB", 
            "LSB", "RSB", "COMA", "SEMI", "DOT", "COLON", "UNDERSCORE", 
            "ID", "WS", "LINECMT", "BLOCKCMT", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTL", "FLOATL", "BOOLL", "STRINGL", "DO", "FUNCTION", 
                  "IF", "ELSE", "CONTINUE", "AUTO", "BREAK", "FOR", "RETURN", 
                  "WHILE", "OUT", "OF", "INHERIT", "ARRAY", "VOID", "BOOLEAN", 
                  "FLOAT", "INTEGER", "STRING", "TRUE", "FALSE", "EQUAL", 
                  "NOTEQUAL", "GT", "LT", "GET", "LET", "AND", "OR", "NOT", 
                  "ADD", "DIV", "SUB", "MUL", "MOD", "ASSIGN", "CONCATE", 
                  "LB", "RB", "LCB", "RCB", "LSB", "RSB", "COMA", "SEMI", 
                  "DOT", "COLON", "UNDERSCORE", "Number", "NoZeroNumber", 
                  "Character", "Fragtional", "Exponent", "DoubleQuote", 
                  "StringChar", "EscapeSequence", "InvalidSequence", "ID", 
                  "WS", "LINECMT", "BLOCKCMT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.INTL_action 
            actions[1] = self.FLOATL_action 
            actions[3] = self.STRINGL_action 
            actions[65] = self.ERROR_CHAR_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = self.text.replace('_','') 
            			
     

    def FLOATL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.text = self.text.replace('_','')
     

    def STRINGL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    result = str(self.text)
                    self.text = result[1:-1]
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise ErrorToken(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    unclose_str = str(self.text)
                    possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
                    if unclose_str[-1] in possible:
                        raise UncloseString(unclose_str[1:-1])
                    else:
                        raise UncloseString(unclose_str[1:])
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                    illegal_str = str(self.text)
                    raise IllegalEscape(illegal_str[1:])
                
     


