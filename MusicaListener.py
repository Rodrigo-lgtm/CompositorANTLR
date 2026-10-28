# Generated from Musica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MusicaParser import MusicaParser
else:
    from MusicaParser import MusicaParser

# This class defines a complete listener for a parse tree produced by MusicaParser.
class MusicaListener(ParseTreeListener):

    # Enter a parse tree produced by MusicaParser#programa.
    def enterPrograma(self, ctx:MusicaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by MusicaParser#programa.
    def exitPrograma(self, ctx:MusicaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by MusicaParser#instruccion.
    def enterInstruccion(self, ctx:MusicaParser.InstruccionContext):
        pass

    # Exit a parse tree produced by MusicaParser#instruccion.
    def exitInstruccion(self, ctx:MusicaParser.InstruccionContext):
        pass



del MusicaParser