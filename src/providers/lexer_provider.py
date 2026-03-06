import ply.lex as lex

from ..grammar.java.keywords import reserved
from ..grammar.java.tokens import tokens
from ..grammar.java.symbols import symbols

class LexerProvider:
    reserved = reserved
    tokens = tokens

    for name, regex in symbols.items():
        locals()[name] = regex

    t_ignore = ' \t'

    def t_IDENTIFIER(self, t):
        r'[A-Za-z_][A-Za-z0-9_]*'
        t.type = self.reserved.get(t.value, 'IDENTIFIER')
        return t

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_STRING_LITERAL(self, t):
        r'\"([^\\\n]|(\\.))*?\"'
        return t

    def t_COMMENT(self, t):
        r'//.*'
        pass

    def t_MULTILINE_COMMENT(self, t):
        r'/\*[\s\S]*?\*/'
        pass

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)