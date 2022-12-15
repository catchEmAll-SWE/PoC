from checks import *
from pathlib import Path
#import github_action_utils as ghub_utils

allowed_extensions = ['.txt', '.tex', '.py', '.pdf']

official_docs_dirs = [
    'Analisi dei requisiti/',
    'Norme di progetto/',
]

necessary_sections_files = [
    'style.tex',
    'packages.tex',
    'title_page.tex',
]

# Can find single files's rules in ./specifics_rules.py
# Single files's rules are applied in order  <--- IMPORTANT

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
        if checkNecessarySectionsFilesPresence(sections_path, necessary_sections_files):
            #checkStyleFileCorrectness(sections_path)
            #checkPackagesFileCorrectness(sections_path)
            checkTitlePageFileCorrectness(sections_path)



