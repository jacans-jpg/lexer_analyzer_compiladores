from src.providers.file_reader import FileReaderProvider
from src.services.file_reader_services import FileReaderService
from src.services.lexer_service import LexerService

reader = FileReaderProvider()
service = FileReaderService(reader)
contenido = service.readFile("src/data/archivo.txt")

lexer = LexerService(contenido);
tokens = lexer.tokenizar();

print(tokens)