from .keywords import reserved

tokens = [
    'IDENTIFIER',
    'NUMBER',
    'STRING_LITERAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQ',
    'NEQ',
    'LT',
    'GT',
    'LE',
    'GE',
    'AND',
    'OR',
    'NOT',
    'ASSIGN',
    'LPAREN','RPAREN',
    'LBRACE','RBRACE',
    'LBRACKET','RBRACKET',
    'SEMICOLON',
    'COMMA',
    'DOT'

] + list(reserved.values())