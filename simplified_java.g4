grammar simplified_java;

init: ID;

ID: [a-zA-Z][a-zA-Z_0-9]*;

if: 'if' '(' cond ')' ':' block else? 'end';
else: 'else' ':' block;

while: 'while' '(' cond ')' ':' block 'end';

cond: 'exp';
block: 'block';

WS: [ \t\n] -> skip;
