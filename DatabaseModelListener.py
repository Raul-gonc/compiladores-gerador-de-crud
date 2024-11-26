# Generated from DatabaseModel.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DatabaseModelParser import DatabaseModelParser
else:
    from DatabaseModelParser import DatabaseModelParser

# This class defines a complete listener for a parse tree produced by DatabaseModelParser.
class DatabaseModelListener(ParseTreeListener):

    # Enter a parse tree produced by DatabaseModelParser#database.
    def enterDatabase(self, ctx:DatabaseModelParser.DatabaseContext):
        pass

    # Exit a parse tree produced by DatabaseModelParser#database.
    def exitDatabase(self, ctx:DatabaseModelParser.DatabaseContext):
        pass


    # Enter a parse tree produced by DatabaseModelParser#table.
    def enterTable(self, ctx:DatabaseModelParser.TableContext):
        pass

    # Exit a parse tree produced by DatabaseModelParser#table.
    def exitTable(self, ctx:DatabaseModelParser.TableContext):
        pass


    # Enter a parse tree produced by DatabaseModelParser#column.
    def enterColumn(self, ctx:DatabaseModelParser.ColumnContext):
        pass

    # Exit a parse tree produced by DatabaseModelParser#column.
    def exitColumn(self, ctx:DatabaseModelParser.ColumnContext):
        pass


    # Enter a parse tree produced by DatabaseModelParser#relation.
    def enterRelation(self, ctx:DatabaseModelParser.RelationContext):
        pass

    # Exit a parse tree produced by DatabaseModelParser#relation.
    def exitRelation(self, ctx:DatabaseModelParser.RelationContext):
        pass



del DatabaseModelParser