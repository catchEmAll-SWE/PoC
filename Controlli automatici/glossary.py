import re
import sys
from pathlib import Path
from modules.print_error import PrintWarning, PrintError, PrintSimpleError

# TODO
# escludere il controllo ai file title_page, packages, style, modifiche
# \textit{parola}\textsubscript{G} questo viene rilevato senza pedice (per la parentesi graffa)
# parola dentro la parola es. parola "Id" e' presente anche in "Identificazione", lo script segna la parola
# ritornare una lista di errori importando il modulo print_error stampando anche la linea dove manca la parola
# aggiungere lo script al workflow di github con trigger modifiche sul documento Glossario/src/sections/glossario.tex (così non si runna ogni volta che si fa un push inutilmente)

def checkGlossaryWordPresenceInOfficialDocs(word: str) -> bool:
    ambiguous_words = ['Verifica']
    unnecessary_files = ['title_page', 'packages', 'style', 'modifiche']
    errors = []
    warnings = []
    official_docs_dirs = ['Analisi dei requisiti/', 'Norme di progetto/', 'Piano di progetto/', 'Piano di qualifica/']
    official_dirs = [Path('.')/dir_name for dir_name in official_docs_dirs]
    for dir in official_dirs:
        if dir.exists():
            for file in dir.rglob('*'):
                if file.suffix == '.tex' and file.stem not in unnecessary_files:
                    file_text = file.read_text(encoding="UTF-8")
                    if re.search(r'\s+'+word+'(?!\\textsubscript{\S*G\S*})', file_text):
                        if word in ambiguous_words:
                            warnings.append(str(file))
                        else:
                            errors.append(str(file))    
    if errors:
            PrintSimpleError.print_warning(errors, group_name = word)
    if warnings:
            PrintWarning.print_warning(warnings, group_name = word)


def main() -> int:
    glossario = (Path('.')/"Glossario/src/sections/glossario.tex").read_text(encoding="UTF-8")
    for word in re.finditer(r'\\paragraph{\s*([A-z]+(\s[A-z]+)*)\s*}', glossario):
        checkGlossaryWordPresenceInOfficialDocs(word.group(1))
    sys.exit(PrintError.build_status.value)


if __name__ == '__main__': #to define that is a script and not a module
    main()


# TODO
#   [ ] recognize word that is ambigous (ex. Verifica)
#   [x] check not in title page, packages, style, modifiche
#   [ ] add workflow using push affects specific files trigger event
