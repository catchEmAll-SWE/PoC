import re
from pathlib import Path

# TODO
# escludere il controllo ai file title_page, packages, style, modifiche
# \textit{parola}\textsubscript{G} questo viene rilevato senza pedice (per la parentesi graffa)
# parola dentro la parola es. parola "Id" e' presente anche in "Identificazione", lo script segna la parola
# ritornare una lista di errori importando il modulo print_error stampando anche la linea dove manca la parola
# aggiungere lo script al workflow di github con trigger modifiche sul documento Glossario/src/sections/glossario.tex (così non si runna ogni volta che si fa un push inutilmente)

def checkGlossaryWordPresenceInOfficialDocs(word: str) -> bool:
    result = True
    official_docs_dirs = ['Analisi dei requisiti/', 'Norme di progetto/', 'Piano di progetto/', 'Piano di qualifica/']
    official_dirs = [Path('.')/dir_name for dir_name in official_docs_dirs]
    for dir in official_dirs:
        if dir.exists():
            for file in dir.rglob('*'):
                if file.suffix == '.tex':
                    file_text = file.read_text(encoding="UTF-8")
                    if re.search(word+r'(?!\\textsubscript{\S*G\S*})', file_text):
                        print(str(file) + ' - ' + word)
                        result = False
    return result

#POST: return True if word is present in official docs, False and print files where it is not present otherwise


def main() -> int:
    glossario = (Path('.')/"Glossario/src/sections/glossario.tex").read_text(encoding="UTF-8")
    print('wrong files: ')
    for word in re.finditer(r'\\paragraph{\s*([A-z]+(\s[A-z]+)*)\s*}', glossario):
        checkGlossaryWordPresenceInOfficialDocs(word.group(1))



if __name__ == '__main__': #to define that is a script and not a module
    main()