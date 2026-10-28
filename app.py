from flask import Flask, request, jsonify
from flask_cors import CORS
from antlr4 import InputStream, CommonTokenStream
from MusicaLexer import MusicaLexer
from MusicaParser import MusicaParser
from antlr4.error.ErrorListener import ErrorListener

app = Flask(__name__, static_folder=".")
CORS(app)

class ErroresMusicales(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errores.append(f"Línea {line}, columna {column}: {msg}")

@app.get("/")
def inicio():
    return app.send_static_file("index.html")

@app.post("/analizar")
def analizar():
    datos = request.get_json(silent=True) or {}
    codigo = datos.get("codigo", "")

    lexer = MusicaLexer(InputStream(codigo))
    errores = ErroresMusicales()
    lexer.removeErrorListeners()
    lexer.addErrorListener(errores)

    tokens = CommonTokenStream(lexer)
    parser = MusicaParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(errores)
    parser.programa()

    if errores.errores:
        return jsonify({"valido": False, "errores": errores.errores}), 400

    return jsonify({
        "valido": True,
        "mensaje": "La secuencia musical es válida.",
        "notas": sum(1 for token in tokens.tokens if token.type == MusicaLexer.NOTA)
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
