grammar simplified_java;

init: func+;
func: (ID '(' ')' | 'main') ':' dec comd* 'end';

dec: 'var' ':' (var|const)+; // declaração de variáveis
var: ID ':' ('int' | 'float' | 'str' | 'bool')';';
const: 'const' ID '=' type ';';
type: INT | FLOAT | STR | BOOL;

comd: if | assign | while | return;
assign: ID '=' exp ';'; // Erro de atribuição feito na semantica
return: 'return' (ID | type) ';';

if: 'if' '(' exp ')' ':' block else? 'end';
else: 'else' ':' block;

exp: 'seil';

while: 'while' '(' exp ')' ':' block 'end';
block: 'block';

INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STR: '"' [ a-zA-Z0-9"]* '"'; // colocar pontuação e acentuação
BOOL: 'True' | 'False';

ID: [a-zA-Z][a-zA-Z_0-9]*;

WS: [ \t\n] -> skip;
