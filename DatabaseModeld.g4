grammar Expressoes;

// Analise Lexica
PRINT : 'print' ;
IF : 'if' ;
ELSE : 'else';
PV : ';' ;
VAR : [A-Za-z]+ ;
NUM : [0-9]+ ;
EQ : '=';
OP1 : '==' | '!=' | '<' | '>' ;
OP2 : '+' | '-' ; 
OP3 : '*' |  '/' ;
APAR : '(' ;
FPAR : ')' ;
ACHAVE : '{';
FCHAVE : '}';
BRANCO : ( ' ' | '\n'  ) -> skip ;

// Analise Sintatica
prog : com EOF ; 
com : PRINT exp PV 
    | VAR EQ exp PV
    | ACHAVE com* FCHAVE
    | IF APAR exp FPAR com ELSE com
    ; 
exp : exp op=OP3 exp
    | exp op=OP2 exp 
    | exp op=OP1 exp
    | NUM 
    | VAR 
    | APAR exp FPAR
    ;
