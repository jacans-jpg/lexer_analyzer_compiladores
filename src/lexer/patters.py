import re

TOKEN_REGEX = [
    ('FLOAT',   r'\d+\.\d+'),
    ('INTEGER', r'\d+'),
    ('STRING',  r'"[^"]*"'),

    ('IDENTIFICADOR',      r'[A-Za-z_]\w*'),

    ('COMPARACION',              r'=='),
    ('DIFERENCIACION',              r'!='),
    ('MENOR_IGUAL',              r'<='),
    ('MAYOR_IGUAL',              r'>='),
    ('IGUALACION',          r'='),
    ('MENOR_QUE',              r'<'),
    ('MAYOR_QUE',              r'>'),
    ('MAS',            r'\+'),
    ('MENOS',           r'-'),
    ('MULTIPLICACION',            r'\*'),
    ('DIVISION',             r'/'),

    ('PARENTESIS_IZQUIERDO',          r'\('),
    ('PARENTESIS_DERECHO',          r'\)'),
    ('LLAVE_DERECHA',          r'\{'),
    ('LLAVE_IZQUIERDA',          r'\}'),
    ('DOS_PUNTOS',       r';'),
    ('COMA',           r','),
    ('ESPACIO',      r'\s+'),
]

KEYWORDS = {
    'if', 'else', 'while', 'for', 'return',
    'int', 'float', 'string', 'bool'
}