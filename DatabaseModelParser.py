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
        4,1,15,52,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,1,1,1,1,1,1,1,5,1,20,8,1,10,1,12,1,23,9,1,1,1,1,1,
        1,1,1,1,4,1,29,8,1,11,1,12,1,30,1,1,1,1,1,2,1,2,1,2,5,2,38,8,2,10,
        2,12,2,41,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,
        4,6,8,0,1,1,0,6,9,51,0,11,1,0,0,0,2,15,1,0,0,0,4,34,1,0,0,0,6,44,
        1,0,0,0,8,49,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,
        11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,0,15,16,5,1,0,0,16,17,5,14,0,
        0,17,21,5,2,0,0,18,20,3,8,4,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,
        1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,3,0,0,
        25,28,5,4,0,0,26,29,3,4,2,0,27,29,3,6,3,0,28,26,1,0,0,0,28,27,1,
        0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,0,32,
        33,5,5,0,0,33,3,1,0,0,0,34,35,5,14,0,0,35,39,5,10,0,0,36,38,5,12,
        0,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,
        1,0,0,0,41,39,1,0,0,0,42,43,5,11,0,0,43,5,1,0,0,0,44,45,5,14,0,0,
        45,46,5,13,0,0,46,47,5,14,0,0,47,48,5,11,0,0,48,7,1,0,0,0,49,50,
        7,0,0,0,50,9,1,0,0,0,5,13,21,28,30,39
    ]

class DatabaseModelParser ( Parser ):

    grammarFileName = "DatabaseModel.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'table'", "'('", "')'", "'{'", "'}'", 
                     "'POST'", "'PUT'", "'GET'", "'DELETE'", "<INVALID>", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "TYPE", "PV", "PROP", "REL_TYPE", 
                      "ID", "WS" ]

    RULE_database = 0
    RULE_table = 1
    RULE_column = 2
    RULE_relation = 3
    RULE_op = 4

    ruleNames =  [ "database", "table", "column", "relation", "op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    TYPE=10
    PV=11
    PROP=12
    REL_TYPE=13
    ID=14
    WS=15

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
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.table()
                self.state = 13 
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

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DatabaseModelParser.OpContext)
            else:
                return self.getTypedRuleContext(DatabaseModelParser.OpContext,i)


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
            self.state = 15
            self.match(DatabaseModelParser.T__0)
            self.state = 16
            localctx.tableName = self.match(DatabaseModelParser.ID)
            self.state = 17
            self.match(DatabaseModelParser.T__1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 960) != 0):
                self.state = 18
                self.op()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(DatabaseModelParser.T__2)
            self.state = 25
            self.match(DatabaseModelParser.T__3)
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 26
                    self.column()
                    pass

                elif la_ == 2:
                    self.state = 27
                    self.relation()
                    pass


                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
                    break

            self.state = 32
            self.match(DatabaseModelParser.T__4)
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
            self.state = 34
            localctx.columnName = self.match(DatabaseModelParser.ID)
            self.state = 35
            localctx.columnType = self.match(DatabaseModelParser.TYPE)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 36
                self.match(DatabaseModelParser.PROP)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
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
            self.state = 44
            localctx.relationName = self.match(DatabaseModelParser.ID)
            self.state = 45
            localctx.relationType = self.match(DatabaseModelParser.REL_TYPE)
            self.state = 46
            localctx.relatedTable = self.match(DatabaseModelParser.ID)
            self.state = 47
            self.match(DatabaseModelParser.PV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatabaseModelParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)




    def op(self):

        localctx = DatabaseModelParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





