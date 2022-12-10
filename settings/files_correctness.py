from checks import *
from pathlib import Path

allowed_extensions = ['.txt', '.tex', '.py', '.pdf']

official_docs_dirs = [
    'Analisi dei requisiti/',
    'Norme di progetto/',
]

necessary_sections_files = [
    'styles.tex',
    'packages.tex',
    'title_page.tex',
]

wd = Path('.').absolute()

# ================================================ checks =========================================================
checkFilesNameCorrectness([file for file in wd.rglob('*') if file.suffix in allowed_extensions])

official_dirs = [wd/dir_name for dir_name in official_docs_dirs]
for dir in official_dirs:
    if dir.exists() and checkOfficialDocsDirTree(dir):
        src_path = dir/'src/'
        sections_path = src_path/'sections'
        checkOfficialDocPresence(dir)
        if checkLatexFilePresenceInSrc(src_path):
            checkSrcLatexFileCorrectness(src_path)
        checkFilesExtensionInSections(sections_path)
        #if checkNecessarySectionsFilesPresence(sections_path, necessary_sections_files):

            #checkStyleFileCorrectness(sections_path)
            #checkPackagesFileCorrectness(sections_path)
            #checkStyleTitlePageCorrectness(sections_path)



