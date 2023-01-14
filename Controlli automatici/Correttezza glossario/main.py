import re
from pathlib import Path

# TODO
# fare il merge del main con il glossario in questo ramo
# ritornare una lista di errori importando il modulo print_error
# aggiungere lo script al workflow di github con trigger modifiche sul documento Glossario/src/sections/glossario.tex (così non si runna ogni volta che si fa un push inutilmente)

def checkGlossaryWordPresenceInOfficialDocs(word: str) -> bool:
    result = True
    official_docs_dirs = ['Analisi dei requisiti/', 'Norme di progetto/', 'Piano di progetto/', 'Piano di qualifica/']
    official_dirs = [Path('.')/dir_name for dir_name in official_docs_dirs]
    for dir in official_dirs:
        if dir.exists():
            for file in dir.rglob('*'):
                if file.suffix == '.tex':
                    file_text = file.read_text()
                    if re.search(r'word(?!\\textsubscript{\S*G\S*})', file_text):
                        result = False
    return result

#POST: return True if word is present in official docs, False and print files where it is not present otherwise


def main() -> int:
    glossario = (Path('.')/"Controlli automatici/Correttezza glossario/glossario.tex").read_text()
    for word in re.finditer(r'\\paragraph{\s*([A-z]+(\s[A-z]+)*)\s*}', glossario):
        print(word.group(1))



if __name__ == '__main__': #to define that is a script and not a module
    main()