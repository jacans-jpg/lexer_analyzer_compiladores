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

    ('ESPACIO',      r'\s+'),
]

KEYWORDS = {
    "abstract","assert","boolean","break","byte",
    "case","catch","char","class","const",
    "continue","default","do","double",
    "else","enum","extends",
    "final","finally","float","for",
    "goto",
    "if","implements","import","instanceof","int","interface",
    "long",
    "native","new",
    "package","private","protected","public",
    "return",
    "short","static","strictfp","super","switch","synchronized",
    "this","throw","throws","transient","try",
    "void","volatile","while", "String", "System", "out", "println"
}

LITERALS = {"true", "false", "null"}