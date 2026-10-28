# Generated from Musica.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,23,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,5,0,9,8,0,10,0,12,0,12,
        9,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,2,0,2,0,0,21,0,4,
        1,0,0,0,2,17,1,0,0,0,4,5,5,1,0,0,5,6,5,2,0,0,6,10,5,3,0,0,7,9,3,
        2,1,0,8,7,1,0,0,0,9,12,1,0,0,0,10,8,1,0,0,0,10,11,1,0,0,0,11,13,
        1,0,0,0,12,10,1,0,0,0,13,14,5,3,0,0,14,15,5,2,0,0,15,16,5,0,0,1,
        16,1,1,0,0,0,17,18,5,4,0,0,18,19,5,3,0,0,19,20,5,5,0,0,20,21,5,6,
        0,0,21,3,1,0,0,0,1,10
    ]

class MusicaParser ( Parser ):

    grammarFileName = "Musica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Main'", "'|'", "':'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "MAIN", "BARRA", "DOSPUNTOS", "PAREN_IZQ", 
                      "PAREN_DER", "NOTA", "COMENTARIO", "ESPACIOS" ]

    RULE_programa = 0
    RULE_instruccion = 1

    ruleNames =  [ "programa", "instruccion" ]

    EOF = Token.EOF
    MAIN=1
    BARRA=2
    DOSPUNTOS=3
    PAREN_IZQ=4
    PAREN_DER=5
    NOTA=6
    COMENTARIO=7
    ESPACIOS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(MusicaParser.MAIN, 0)

        def BARRA(self, i:int=None):
            if i is None:
                return self.getTokens(MusicaParser.BARRA)
            else:
                return self.getToken(MusicaParser.BARRA, i)

        def DOSPUNTOS(self, i:int=None):
            if i is None:
                return self.getTokens(MusicaParser.DOSPUNTOS)
            else:
                return self.getToken(MusicaParser.DOSPUNTOS, i)

        def EOF(self):
            return self.getToken(MusicaParser.EOF, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MusicaParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(MusicaParser.InstruccionContext,i)


        def getRuleIndex(self):
            return MusicaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = MusicaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(MusicaParser.MAIN)
            self.state = 5
            self.match(MusicaParser.BARRA)
            self.state = 6
            self.match(MusicaParser.DOSPUNTOS)
            self.state = 10
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 7
                self.instruccion()
                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 13
            self.match(MusicaParser.DOSPUNTOS)
            self.state = 14
            self.match(MusicaParser.BARRA)
            self.state = 15
            self.match(MusicaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAREN_IZQ(self):
            return self.getToken(MusicaParser.PAREN_IZQ, 0)

        def DOSPUNTOS(self):
            return self.getToken(MusicaParser.DOSPUNTOS, 0)

        def PAREN_DER(self):
            return self.getToken(MusicaParser.PAREN_DER, 0)

        def NOTA(self):
            return self.getToken(MusicaParser.NOTA, 0)

        def getRuleIndex(self):
            return MusicaParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = MusicaParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(MusicaParser.PAREN_IZQ)
            self.state = 18
            self.match(MusicaParser.DOSPUNTOS)
            self.state = 19
            self.match(MusicaParser.PAREN_DER)
            self.state = 20
            self.match(MusicaParser.NOTA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





