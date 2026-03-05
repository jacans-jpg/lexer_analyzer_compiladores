import re
from ..lexer.patters import TOKEN_REGEX, KEYWORDS
from ..classes.token import Token


class LexerService:
    def __init__(self, code: str):
        self.code = code
        self.tokens = []
        self.tabla_simbolos = []
        self.errores = []

    def tokenizar(self):

        for token_type, pattern in TOKEN_REGEX:

            for match in re.finditer(pattern, self.code):

                value = match.group(0)
                linea = self.code[:match.start()].count("\n") + 1
                columna = match.start() - self.code.rfind("\n", 0, match.start())

                tipo_final = token_type

                # Verificar palabra reservada
                if token_type == 'IDENTIFICADOR' and value in KEYWORDS:
                    tipo_final = 'RESERVADA'

                if tipo_final != 'ESPACIO':

                    # Agregar token
                    self.tokens.append(Token(tipo_final, value))

                    # 🔥 Agregar a tabla símbolos SOLO identificadores reales
                    if tipo_final == 'IDENTIFICADOR':

                        # Evitar duplicados
                        existe = any(
                            simbolo["nombre"] == value
                            for simbolo in self.tabla_simbolos
                        )

                        if not existe:
                            self.tabla_simbolos.append({
                                "nombre": value,
                                "tipo": tipo_final,
                                "linea": linea,
                                "columna": columna
                            })

        return self.tokens