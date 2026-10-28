# Generated from Musica.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,50,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,
        4,1,5,1,5,3,5,33,8,5,1,6,1,6,5,6,37,8,6,10,6,12,6,40,9,6,1,6,1,6,
        1,7,4,7,45,8,7,11,7,12,7,46,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,1,0,4,1,0,65,71,1,0,51,53,2,0,10,10,13,13,3,0,9,10,13,
        13,32,32,52,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,22,
        1,0,0,0,5,24,1,0,0,0,7,26,1,0,0,0,9,28,1,0,0,0,11,30,1,0,0,0,13,
        34,1,0,0,0,15,44,1,0,0,0,17,18,5,77,0,0,18,19,5,97,0,0,19,20,5,105,
        0,0,20,21,5,110,0,0,21,2,1,0,0,0,22,23,5,124,0,0,23,4,1,0,0,0,24,
        25,5,58,0,0,25,6,1,0,0,0,26,27,5,40,0,0,27,8,1,0,0,0,28,29,5,41,
        0,0,29,10,1,0,0,0,30,32,7,0,0,0,31,33,7,1,0,0,32,31,1,0,0,0,32,33,
        1,0,0,0,33,12,1,0,0,0,34,38,5,35,0,0,35,37,8,2,0,0,36,35,1,0,0,0,
        37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,38,1,
        0,0,0,41,42,6,6,0,0,42,14,1,0,0,0,43,45,7,3,0,0,44,43,1,0,0,0,45,
        46,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,49,6,7,0,
        0,49,16,1,0,0,0,4,0,32,38,46,1,6,0,0
    ]

class MusicaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MAIN = 1
    BARRA = 2
    DOSPUNTOS = 3
    PAREN_IZQ = 4
    PAREN_DER = 5
    NOTA = 6
    COMENTARIO = 7
    ESPACIOS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Main'", "'|'", "':'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "MAIN", "BARRA", "DOSPUNTOS", "PAREN_IZQ", "PAREN_DER", "NOTA", 
            "COMENTARIO", "ESPACIOS" ]

    ruleNames = [ "MAIN", "BARRA", "DOSPUNTOS", "PAREN_IZQ", "PAREN_DER", 
                  "NOTA", "COMENTARIO", "ESPACIOS" ]

    grammarFileName = "Musica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


