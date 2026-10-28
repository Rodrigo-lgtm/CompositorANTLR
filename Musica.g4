grammar Musica;

programa
    : MAIN BARRA DOSPUNTOS instruccion* DOSPUNTOS BARRA EOF
    ;

instruccion
    : PAREN_IZQ DOSPUNTOS PAREN_DER NOTA
    ;

MAIN       : 'Main';
BARRA      : '|';
DOSPUNTOS  : ':';
PAREN_IZQ  : '(';
PAREN_DER  : ')';
NOTA       : [A-G] [3-5]?;
COMENTARIO : '#' ~[\r\n]* -> skip;
ESPACIOS   : [ \t\r\n]+ -> skip;
