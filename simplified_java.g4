grammar simplified_java;

init: func* func_main;

func: ID '(' parameters_list ')' ':' (type | 'void') dec? (comd | inst)* 'end'; // comandos ou instâncias de funções
func_main: 'main' ':' dec? (comd|inst)* 'end';
parameters_list: ( ( type ID ) (',' type ID)* )?;

type: ('int' | 'float' | 'str' | 'bool' );

dec: 'var' ':' (dec_var | dec_const)+; // declaração de variáveis
dec_var: ID (',' ID)* ':' type ';';
dec_const: 'const' ID '=' value ';';
value: inst_op | INT | FLOAT | STR | BOOL; // valor que pode ser int float str ou bool ou retorno de função

inst: (ID | 'print' | 'scanf') '(' ((ID | value | exp) (',' (ID | value | exp))*)? ')' ';'; // instância de função. Limitação de recursividade na semântica
inst_op: (ID | 'print' | 'scanf') '(' ((ID | value | exp) (',' (ID | value | exp))*) ')'; // instância de função dentro de uma operação
comd: if | assign | while | return | exp | break;

assign: ID '=' exp ';'; // Erro de atribuição feito na semantica
return: 'return' (ID | value | exp) ';';

if: 'if' '(' exp ')' ':' (comd | inst)* else? 'end';
else: 'else' ':' (comd | inst)*;

exp: inst_op | exp op exp | INT | ID | '(' exp ')' ;
op: '!' | '-' | '+' | '*' | '/' | '==' | '!=' | '>=' | '<=' | '>' | '<';

while: 'while' '(' exp ')' ':' (comd | inst)* 'end';
break: 'break' ';';

INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STR: '"' [a-záàâãäéèêëíìîïóòôõöúùûüçA-ZÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇ 0-9_,.:;´`~^?]* '"';
BOOL: 'True' | 'False';

ID: [a-zA-Z][a-zA-Z_0-9]*;

WS: [ \t\n] -> skip;
