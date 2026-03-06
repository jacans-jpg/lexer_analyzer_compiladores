import ply.yacc as yacc
from .lexer_provider import LexerProvider

class ParserProvider:

    tokens = LexerProvider.tokens

    precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'EQ', 'NEQ'),
        ('left', 'LT', 'LE', 'GT', 'GE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
    )

    def __init__(self):
        self.lexer = LexerProvider()
        self.lexer.build()
        self.errors = []

        self.parser = yacc.yacc(
            module=self,
            debug=False,
            write_tables=False,
            errorlog=yacc.NullLogger()
        )

    # ---------- PROGRAMA ----------

    def p_program(self, p):
        '''
        program : class
        '''

    # ---------- CLASE ----------

    def p_class(self, p):
        '''
        class : modifiers CLASS IDENTIFIER LBRACE class_body RBRACE
        '''

    # ---------- MODIFICADORES ----------

    def p_modifiers_multiple(self, p):
        '''
        modifiers : modifier modifiers
        '''

    def p_modifiers_single(self, p):
        '''
        modifiers : modifier
        '''

    def p_modifier(self, p):
        '''
        modifier : PUBLIC
                 | PRIVATE
                 | PROTECTED
                 | STATIC
        '''

    # ---------- CUERPO DE CLASE ----------

    def p_class_body_multiple(self, p):
        '''
        class_body : class_member class_body
        '''

    def p_class_body_single(self, p):
        '''
        class_body : class_member
        '''

    def p_class_member(self, p):
        '''
        class_member : field
                     | method
                     | constructor
        '''

    # ---------- ATRIBUTOS ----------

    def p_field(self, p):
        '''
        field : modifiers type IDENTIFIER SEMICOLON
        '''

    # ---------- CONSTRUCTOR ----------

    def p_constructor(self, p):
        '''
        constructor : modifiers IDENTIFIER LPAREN params RPAREN block
        '''

    # ---------- MÉTODOS ----------

    def p_method(self, p):
        '''
        method : modifiers type IDENTIFIER LPAREN params RPAREN block
               | modifiers VOID IDENTIFIER LPAREN params RPAREN block
        '''

    # ---------- TIPOS ----------

    def p_type(self, p):
        '''
        type : INT
             | FLOAT
             | DOUBLE
             | BOOLEAN
             | STRING
             | IDENTIFIER
        '''

    # ---------- PARÁMETROS ----------

    def p_params_multiple(self, p):
        '''
        params : param COMMA params
        '''

    def p_params_single(self, p):
        '''
        params : param
        '''

    def p_params_empty(self, p):
        '''
        params :
        '''

    def p_param(self, p):
        '''
        param : type IDENTIFIER
        '''

    # ---------- BLOQUES ----------

    def p_block(self, p):
        '''
        block : LBRACE statements RBRACE
        '''

    # ---------- SENTENCIAS ----------

    def p_statements_multiple(self, p):
        '''
        statements : statement statements
        '''

    def p_statements_single(self, p):
        '''
        statements : statement
        '''

    def p_statement(self, p):
        '''
        statement : assignment
                  | variable_declaration
                  | method_call
                  | if_statement
                  | while_statement
                  | for_statement
                  | return_statement
        '''

    # ---------- DECLARACIÓN DE VARIABLES ----------

    def p_variable_declaration(self, p):
        '''
        variable_declaration : type IDENTIFIER ASSIGN expression SEMICOLON
                             | type IDENTIFIER SEMICOLON
        '''

    # ---------- ASIGNACIONES ----------

    def p_assignment(self, p):
        '''
        assignment : THIS DOT IDENTIFIER ASSIGN expression SEMICOLON
                   | IDENTIFIER ASSIGN expression SEMICOLON
        '''

    # ---------- LLAMADAS A MÉTODOS ----------

    def p_method_call(self, p):
        '''
        method_call : access LPAREN args RPAREN SEMICOLON
        '''

    def p_access_chain(self, p):
        '''
        access : IDENTIFIER
               | access DOT IDENTIFIER
        '''

    # ---------- ARGUMENTOS ----------

    def p_args_multiple(self, p):
        '''
        args : expression COMMA args
        '''

    def p_args_single(self, p):
        '''
        args : expression
        '''

    def p_args_empty(self, p):
        '''
        args :
        '''

    # ---------- IF ----------

    def p_if_statement(self, p):
        '''
        if_statement : IF LPAREN expression RPAREN block
                     | IF LPAREN expression RPAREN block ELSE block
        '''

    # ---------- WHILE ----------

    def p_while_statement(self, p):
        '''
        while_statement : WHILE LPAREN expression RPAREN block
        '''

    # ---------- FOR ----------

    def p_for_statement(self, p):
        '''
        for_statement : FOR LPAREN assignment expression SEMICOLON assignment RPAREN block
        '''

    # ---------- RETURN ----------

    def p_return_statement(self, p):
        '''
        return_statement : RETURN expression SEMICOLON
        '''

    # ---------- NEW ----------

    def p_expression_new(self, p):
        '''
        expression : NEW IDENTIFIER LPAREN args RPAREN
        '''

    # ---------- EXPRESIONES ----------

    def p_expression_binop(self, p):
        '''
        expression : expression PLUS expression
                   | expression MINUS expression
                   | expression TIMES expression
                   | expression DIVIDE expression
                   | expression EQ expression
                   | expression NEQ expression
                   | expression LT expression
                   | expression GT expression
                   | expression LE expression
                   | expression GE expression
        '''

    def p_expression_group(self, p):
        '''
        expression : LPAREN expression RPAREN
        '''

    def p_expression_number(self, p):
        '''
        expression : NUMBER
        '''

    def p_expression_string(self, p):
        '''
        expression : STRING_LITERAL
        '''

    def p_expression_identifier(self, p):
        '''
        expression : IDENTIFIER
        '''

    def p_expression_this(self, p):
        '''
        expression : THIS DOT IDENTIFIER
        '''

    # ---------- ERROR ----------

    def p_error(self, p):
        if p:
            self.errors.append(f"Syntax error at '{p.value}' line {p.lineno}")
        else:
            self.errors.append("Syntax error at EOF")

    # ---------- PARSE ----------

    def parse(self, data):
        return self.parser.parse(data, lexer=self.lexer.lexer)