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

def addRegexControllToPossibleDuplicate(regex: str, list_of_duplicates: list[str]) -> str:
    for duplicate in list_of_duplicates:
        regex += r'(?!\s+'+duplicate+')'
    return regex

def checkGlossaryWordPresenceInOfficialDocs(word: str) -> bool:
    ambiguous_words = ['verifica', 'commit', 'id', 'captcha', 'requisiti'] #must be lowercase
    unnecessary_files = ['title_page', 'packages', 'style', 'modifiche']
    possible_duplicate = {'github' : ['workflow'], 'framework' : ['scrum']} #must be lowercase
    errors = []
    warnings = []
    official_docs_dirs = ['Analisi dei requisiti/', 'Norme di progetto/', 'Piano di progetto/', 'Piano di qualifica/']
    official_dirs = [Path('.')/dir_name for dir_name in official_docs_dirs]
    for dir in official_dirs:
        if dir.exists():
            for file in dir.rglob('*'):
                if file.suffix == '.tex' and file.stem not in unnecessary_files:
                    file_text = file.read_text(encoding="UTF-8")
                    regex = r'((?<=\s)|(?<=^))'+word+r'(?=[^\w])(?!\.\w)(?!\\textsubscript{\s*G\s*})'
                    if word.lower() in possible_duplicate.keys():
                        regex = addRegexControllToPossibleDuplicate(regex, possible_duplicate[word.lower()])
                    if re.search(regex, file_text, re.IGNORECASE):
                        if word.lower() in ambiguous_words:
                            warnings.append(str(file))
                        else:
                            errors.append(str(file))    
    if errors:
            PrintSimpleError.print_error(errors, group_name = word)
    if warnings:
            PrintWarning.print_warning(warnings, group_name = word)


def main() -> int:
    glossario = (Path('.')/"Glossario/src/sections/glossario.tex").read_text(encoding="UTF-8")
    for word in re.finditer(r'\\paragraph{\s*(.*)\s*}', glossario):
        checkGlossaryWordPresenceInOfficialDocs(word.group(1))
    sys.exit(PrintError.build_status.value)


if __name__ == '__main__': #to define that is a script and not a module
    main()

# Comment regard ambiguos words meaning:
# Verifica: can assume different meaning in different context
# Commit: can be included in a command explanation
# Id: can be included in a command explanation
# CAPTCHA: can be reference to another document, can assume his own meaning 
# Requisiti: can assume different meaning in different context