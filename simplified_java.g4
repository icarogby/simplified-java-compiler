grammar simplified_java;

init: func* func_main;

func: ID '(' parameters_list ')' ':' (type | 'void') dec_list? comd* 'end' ;
func_main: 'main' ':' dec_list? comd* 'end' ;

parameters_list: ( ( type ID ) (',' type ID)* )? ;
type: 'int' | 'float' | 'str' | 'bool' ;

dec_list: 'var' ':' (dec_var | dec_const)+; // declaração de variáveis
dec_var: ID (',' ID)* ':' type ';';
dec_const: 'const' ID '=' value ';';
value: INT | FLOAT | STR | BOOL; // valor que pode ser int float str ou bool ou retorno de função

comd: if | assign | while | return | break | inst ';' ;

// instância de função
inst: ID '(' value_list? ')' ;
value_list: ( (ID | value | inst | exp) ( ',' (ID | value | inst| exp) )* ) ;

assign: ID '=' exp ';'; // Erro de atribuição feito na semantica
return: 'return' (ID | value | exp) ';';

if: 'if' '(' (logic_exp | BOOL) ')' ':' (comd)* else? 'end' ;
else: 'else' ':' (comd)* ;

while: 'while' '(' (logic_exp | BOOL) ')' ':' (comd)* 'end';
break: 'break' ';';

BOOL: 'true' | 'false';
ID: [a-zA-Z][a-zA-Z_0-9]*;

// Expressões lógicas e aritméticas
exp: logic_exp | arith_exp ;

logic_exp: logic_t | logic_exp 'or' logic_t ;
logic_t: logic_f | logic_t 'and' logic_f ;
logic_f: '!' logic_f | '(' logic_exp ')' | comparison ;

comparison: arith_exp comparison_op arith_exp ;
comparison_op: '==' | '!=' | '<'| '>'| '<='| '=>' ;

arith_exp: arith_t | arith_exp '+' arith_t | arith_exp '-' arith_t ;
arith_t: arith_f | arith_t '*' arith_f | arith_t '/' arith_f ;
arith_f: number | '-' arith_f  | '(' arith_exp ')';

// Tipos
number: ID | INT | FLOAT | inst ; // inst e ID - verificar no semântico

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
