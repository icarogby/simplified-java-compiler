grammar simplified_java;

init: decFuncList? funcMain;

decFuncList: decFunc+;
decFunc: ID '(' parametersList ')' ':' funcType varField? cmmd* 'end';
funcMain: 'main' ':' varField? cmmd* 'end';

parametersList: ((dataType ID )(',' dataType ID)*)?;

funcType: 'int' | 'float' | 'str' | 'bool' | 'void';
dataType: 'int' | 'float' | 'str' | 'bool' ;

varField: 'var' ':' decVarConst+; // declaração de variáveis
decVarConst: decVar | decConst;
decVar: ID (',' ID)* ':' dataType ';';
decConst: 'const' ID '=' value ';';
value: INT | FLOAT | STR | BOOL; // valor que pode ser int float str ou bool ou retorno de função

cmmd: if | assign | while | return | break | inst ';' ;

inst: ID '(' instParamList? ')' ;
instParamList: (instParam (',' instParam)* ) ;
instParam: (ID | value | inst | exp ) ;

assign: ID '=' exp ';'; // Erro de atribuição feito na semantica
return: 'return' (ID | value | exp) ';';

if: 'if' '(' (logic_exp | BOOL) ')' ':' (cmmd)* else? 'end' ;
else: 'else' ':' (cmmd)* ;

while: 'while' '(' (logic_exp | BOOL) ')' ':' (cmmd)* 'end';
break: 'break' ';';

// Expressões lógicas e aritméticas
exp: logic_exp | arith_exp ;

logic_exp: logic_t | logic_exp 'or' logic_t ;
logic_t: logic_f | logic_t 'and' logic_f ;
logic_f: '!' logic_f | '(' logic_exp ')' | comparison | BOOL ;

comparison: arith_exp comparison_op arith_exp ;
comparison_op: '==' | '!=' | '<'| '>'| '<='| '=>' ;

arith_exp: arith_t | arith_exp '+' arith_t | arith_exp '-' arith_t ;
arith_t: arith_f | arith_t '*' arith_f | arith_t '/' arith_f ;
arith_f: number | '-' arith_f  | '(' arith_exp ')';

// Tipos
number: ID | INT | FLOAT | inst; // inst e ID - verificar no semântico

BOOL: 'true' | 'false';
ID: [a-zA-Z][a-zA-Z_0-9]*;
INT: [0-9]
   | [1-9][0-9]* ;
FLOAT: [0-9] '.' [0-9]+
     | [1-9][0-9]* '.' [0-9]+ ;
STR: '"' ( ESC | ~( '\\' | '"' ) )* '"' ;
ESC: '\\' ( 't' | 'n' | '"' | '\\' ) ;

// Commentários de linha e de bloco
comment: LINE_COMMENT | BLOCK_COMMENT ;
LINE_COMMENT: '//' ~[\r\n]* -> channel(HIDDEN) ;
BLOCK_COMMENT: '/*' .*? '*/' -> channel(HIDDEN) ;

WS: [ \t\n\r] -> skip;
