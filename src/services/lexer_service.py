import re
from ..lexer.patters import TOKEN_REGEX, KEYWORDS
from ..classes.token import Token


class LexerService:
    def __init__(self, code: str):
        self.code = code
        self.tokens = []

    def tokenizar(self) -> str:
        for token_type, pattern in TOKEN_REGEX:
            for match in re.finditer(pattern, self.code):
                value = match.group(0)
                if token_type == 'IDENTIFICADOR' and value in KEYWORDS:
                    token_type = 'RESERVADA'
                    
                if token_type != 'ESPACIO':
                    self.tokens.append(Token(token_type, value))
        return self.tokens