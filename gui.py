import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from src.providers.file_reader import FileReaderProvider
from src.services.file_reader_services import FileReaderService
from src.services.lexer_service import LexerService
from src.providers.parser_provider import ParserProvider


class LexerGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico - Compiladores")
        self.root.geometry("1100x700")

        self.crear_componentes()

    def crear_componentes(self):

        # CODIGO FUENTE
        tk.Label(self.root, text="Código Fuente").pack()

        self.code_text = tk.Text(self.root, height=10)
        self.code_text.pack(fill="x", padx=10, pady=5)

        # BOTONES
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        ttk.Button(button_frame, text="Abrir TXT",
                   command=self.abrir_archivo).pack(side="left", padx=5)

        ttk.Button(button_frame, text="Analizar",
                   command=self.analizar).pack(side="left", padx=5)

        ttk.Button(button_frame, text="Exportar",
                   command=self.exportar).pack(side="left", padx=5)

        ttk.Button(button_frame, text="Limpiar",
                   command=self.limpiar).pack(side="left", padx=5)

        # NOTEBOOK (PESTAÑAS)
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        
        # PESTAÑA TOKENS
        frame_tokens = ttk.Frame(notebook)
        notebook.add(frame_tokens, text="Tokens")

        self.token_table = ttk.Treeview(
            frame_tokens,
            columns=("Lexema", "Token"),
            show="headings"
        )

        self.token_table.heading("Lexema", text="Lexema")
        self.token_table.heading("Token", text="Token")

        self.token_table.pack(fill="both", expand=True, padx=10, pady=10)

        # PESTAÑA TABLA DE SIMBOLOS
        frame_symbols = ttk.Frame(notebook)
        notebook.add(frame_symbols, text="Tabla de Símbolos")

        self.symbol_table = ttk.Treeview(
            frame_symbols,
            columns=("Identificador", "Tipo", "Linea", "Columna"),
            show="headings"
        )

        self.symbol_table.heading("Identificador", text="Identificador")
        self.symbol_table.heading("Tipo", text="Tipo")
        self.symbol_table.heading("Linea", text="Línea")
        self.symbol_table.heading("Columna", text="Columna")

        self.symbol_table.pack(fill="both", expand=True, padx=10, pady=10)

        
        # PESTAÑA ERRORES
        frame_errors = ttk.Frame(notebook)
        notebook.add(frame_errors, text="Errores Léxicos")

        self.error_text = tk.Text(frame_errors, fg="red")
        self.error_text.pack(fill="both", expand=True, padx=10, pady=10)


    # ABRIR ARCHIVO
    def abrir_archivo(self):

        ruta = filedialog.askopenfilename(
            filetypes=[("Archivos TXT", "*.txt")]
        )

        if not ruta:
            return

        reader = FileReaderProvider()
        service = FileReaderService(reader)
        contenido = service.readFile(ruta)

        self.code_text.delete("1.0", tk.END)
        self.code_text.insert(tk.END, contenido)


    # ANALIZAR CODIGO
    def analizar(self):

        codigo = self.code_text.get("1.0", tk.END)

        lexer = LexerService(codigo)
        tokens = lexer.tokenizar()

        parser = ParserProvider()
        parser.parse(codigo)

        # limpiar tablas
        for row in self.token_table.get_children():
            self.token_table.delete(row)

        for row in self.symbol_table.get_children():
            self.symbol_table.delete(row)

        self.error_text.delete("1.0", tk.END)

        
        # MOSTRAR TOKENS
        
        for token in tokens:

            token_str = str(token)

            if "(" in token_str and ")" in token_str:
                tipo = token_str.split("(")[0].strip()
                lexema = token_str.split("(")[1].replace(")", "").strip()
            else:
                tipo = token_str
                lexema = ""

            self.token_table.insert(
                "",
                "end",
                values=(lexema, tipo)
            )

        
        # TABLA DE SIMBOLOS
        
        if hasattr(lexer, "tabla_simbolos"):

            for simbolo in lexer.tabla_simbolos:

                try:
                    self.symbol_table.insert(
                        "",
                        "end",
                        values=(
                            simbolo.nombre,
                            simbolo.tipo,
                            simbolo.linea,
                            simbolo.columna
                        )
                    )

                except:

                    self.symbol_table.insert(
                        "",
                        "end",
                        values=(
                            simbolo["nombre"],
                            simbolo["tipo"],
                            simbolo["linea"],
                            simbolo["columna"]
                        )
                    )

        
        # ERRORES LEXICOS / PARSER
        
        if hasattr(parser, "errors") and parser.errors:

            for error in parser.errors:
                self.error_text.insert(tk.END, f"{error}\n")

        else:
            self.error_text.insert(tk.END, "Sin errores léxicos.\n")

    
    # EXPORTAR RESULTADOS
    def exportar(self):

        ruta = filedialog.asksaveasfilename(
            defaultextension=".txt"
        )

        if not ruta:
            return

        with open(ruta, "w", encoding="utf-8") as f:

            f.write("TOKENS\n")
            f.write("------\n")

            for row in self.token_table.get_children():
                values = self.token_table.item(row)["values"]
                f.write(f"{values[0]} -> {values[1]}\n")

            f.write("\nTABLA DE SIMBOLOS\n")
            f.write("-----------------\n")

            for row in self.symbol_table.get_children():
                values = self.symbol_table.item(row)["values"]
                f.write(f"{values}\n")

            f.write("\nERRORES\n")
            f.write("-------\n")
            f.write(self.error_text.get("1.0", tk.END))

        messagebox.showinfo(
            "Exportación",
            "Archivo exportado correctamente"
        )

    
    # LIMPIAR
    
    def limpiar(self):

        self.code_text.delete("1.0", tk.END)
        self.error_text.delete("1.0", tk.END)

        for row in self.token_table.get_children():
            self.token_table.delete(row)

        for row in self.symbol_table.get_children():
            self.symbol_table.delete(row)



# EJECUTAR INTERFAZ

if __name__ == "__main__":

    root = tk.Tk()
    app = LexerGUI(root)
    root.mainloop()