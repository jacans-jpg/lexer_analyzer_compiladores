from src.providers.parser_provider import ParserProvider
from src.providers.file_reader import FileReaderProvider;
from src.services.file_reader_services import FileReaderService;

reader = FileReaderProvider()
service = FileReaderService(reader)
contenido = service.readFile("src/data/archivo.txt")

parser = ParserProvider();
parser.parse(contenido);

print(parser.errors);