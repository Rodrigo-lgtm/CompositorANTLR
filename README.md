# Compositor musical con ANTLR

## Qué cambia
- `Musica.g4` define la gramática del lenguaje musical.
- ANTLR genera el analizador léxico y sintáctico en Python.
- `app.py` recibe el código Bazilio y lo valida usando el parser de ANTLR.
- `index.html` conserva el compositor visual y consulta el servidor para validar el código.

## Requisitos
Python 3.10 o posterior y Java instalado.

## Instalación en Windows PowerShell
```powershell
cd CompositorANTLR
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
java -version
```

Descarga el archivo `antlr-4.13.2-complete.jar` desde la página oficial de ANTLR y colócalo dentro de esta carpeta. Después ejecuta:

```powershell
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor Musica.g4
python app.py
```

Abre `http://127.0.0.1:5000`.

## Sintaxis aceptada
```text
Main |:
    (:) C
    (:) D
    (:) E4
:|
```
Las notas válidas son A, B, C, D, E, F y G; se puede agregar opcionalmente una octava del 3 al 5. Las líneas que comienzan con `#` son comentarios.
