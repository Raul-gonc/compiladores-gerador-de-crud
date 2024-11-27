# Generated from DatabaseModel.g4 by ANTLR 4.13.2
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
        4,1,9,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,4,1,19,8,1,11,1,12,1,20,1,1,1,1,1,2,1,2,
        1,2,5,2,28,8,2,10,2,12,2,31,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        0,0,4,0,2,4,6,0,0,39,0,9,1,0,0,0,2,13,1,0,0,0,4,24,1,0,0,0,6,34,
        1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,
        1,0,0,0,12,1,1,0,0,0,13,14,5,1,0,0,14,15,5,8,0,0,15,18,5,2,0,0,16,
        19,3,4,2,0,17,19,3,6,3,0,18,16,1,0,0,0,18,17,1,0,0,0,19,20,1,0,0,
        0,20,18,1,0,0,0,20,21,1,0,0,0,21,22,1,0,0,0,22,23,5,3,0,0,23,3,1,
        0,0,0,24,25,5,8,0,0,25,29,5,4,0,0,26,28,5,6,0,0,27,26,1,0,0,0,28,
        31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,1,0,0,
        0,32,33,5,5,0,0,33,5,1,0,0,0,34,35,5,8,0,0,35,36,5,7,0,0,36,37,5,
        8,0,0,37,38,5,5,0,0,38,7,1,0,0,0,4,11,18,20,29
    ]

class DatabaseModelParser ( Parser ):

    grammarFileName = "DatabaseModel.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'table'", "'{'", "'}'", "<INVALID>", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TYPE", "PV", "PROP", "REL_TYPE", "ID", "WS" ]

    RULE_database = 0
    RULE_table = 1
    RULE_column = 2
    RULE_relation = 3

    ruleNames =  [ "database", "table", "column", "relation" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    TYPE=4
    PV=5
    PROP=6
    REL_TYPE=7
    ID=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DatabaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DatabaseModelParser.TableContext)
            else:
                return self.getTypedRuleContext(DatabaseModelParser.TableContext,i)


        def getRuleIndex(self):
            return DatabaseModelParser.RULE_database

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDatabase" ):
                listener.enterDatabase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDatabase" ):
                listener.exitDatabase(self)




    def database(self):

        localctx = DatabaseModelParser.DatabaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_database)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.table()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.tableName = None # Token

        def ID(self):
            return self.getToken(DatabaseModelParser.ID, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DatabaseModelParser.ColumnContext)
            else:
                return self.getTypedRuleContext(DatabaseModelParser.ColumnContext,i)


        def relation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DatabaseModelParser.RelationContext)
            else:
                return self.getTypedRuleContext(DatabaseModelParser.RelationContext,i)


        def getRuleIndex(self):
            return DatabaseModelParser.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)




    def table(self):

        localctx = DatabaseModelParser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_table)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(DatabaseModelParser.T__0)
            self.state = 14
            localctx.tableName = self.match(DatabaseModelParser.ID)
            self.state = 15
            self.match(DatabaseModelParser.T__1)
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 16
                    self.column()
                    pass

                elif la_ == 2:
                    self.state = 17
                    self.relation()
                    pass


                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

            self.state = 22
            self.match(DatabaseModelParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.columnName = None # Token
            self.columnType = None # Token

        def PV(self):
            return self.getToken(DatabaseModelParser.PV, 0)

        def ID(self):
            return self.getToken(DatabaseModelParser.ID, 0)

        def TYPE(self):
            return self.getToken(DatabaseModelParser.TYPE, 0)

        def PROP(self, i:int=None):
            if i is None:
                return self.getTokens(DatabaseModelParser.PROP)
            else:
                return self.getToken(DatabaseModelParser.PROP, i)

        def getRuleIndex(self):
            return DatabaseModelParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)




    def column(self):

        localctx = DatabaseModelParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_column)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            localctx.columnName = self.match(DatabaseModelParser.ID)
            self.state = 25
            localctx.columnType = self.match(DatabaseModelParser.TYPE)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 26
                self.match(DatabaseModelParser.PROP)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(DatabaseModelParser.PV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.relationName = None # Token
            self.relationType = None # Token
            self.relatedTable = None # Token

        def PV(self):
            return self.getToken(DatabaseModelParser.PV, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DatabaseModelParser.ID)
            else:
                return self.getToken(DatabaseModelParser.ID, i)

        def REL_TYPE(self):
            return self.getToken(DatabaseModelParser.REL_TYPE, 0)

        def getRuleIndex(self):
            return DatabaseModelParser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)




    def relation(self):

        localctx = DatabaseModelParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_relation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            localctx.relationName = self.match(DatabaseModelParser.ID)
            self.state = 35
            localctx.relationType = self.match(DatabaseModelParser.REL_TYPE)
            self.state = 36
            localctx.relatedTable = self.match(DatabaseModelParser.ID)
            self.state = 37
            self.match(DatabaseModelParser.PV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





