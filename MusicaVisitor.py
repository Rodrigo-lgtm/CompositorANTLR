# Generated from Musica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MusicaParser import MusicaParser
else:
    from MusicaParser import MusicaParser

# This class defines a complete generic visitor for a parse tree produced by MusicaParser.

class MusicaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MusicaParser#programa.
    def visitPrograma(self, ctx:MusicaParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicaParser#instruccion.
    def visitInstruccion(self, ctx:MusicaParser.InstruccionContext):
        return self.visitChildren(ctx)



del MusicaParser