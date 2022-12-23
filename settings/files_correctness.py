from checks import *
from pathlib import Path
import github_action_utils as ghub_utils

allowed_extensions = ['.txt', '.tex', '.py', '.pdf']

official_docs_dirs = [
    'Analisi dei requisiti/',
    'Norme di progetto/',
]  # directories that contains official docs on which we want to apply checks

necessary_sections_files = [
    'style.tex',
    'packages.tex',
    'title_page.tex',
    'modifiche.tex',
]  # files that must be present in docs directory

# Can find single files's rules in ./specifics_rules.py
# Single files's rules are applied in order  <--- IMPORTANT

workingDir = Path('.')

# ================================================ checks =========================================================

files_w_allowed_ext = [file for file in workingDir.rglob(
    '*') if file.suffix in allowed_extensions]

# check if files have correct extension
filesNameCorrectness(files_w_allowed_ext)

official_dirs = [workingDir/dir_name for dir_name in official_docs_dirs]
for dir in official_dirs:
    if dir.exists() and officialDocsDirTree(dir):
        src_path = dir/'src/'
        sections_path = src_path/'sections'
        officialPdfPresenceOnly(dir)
        if latexFilePresenceInSrc(src_path):
            srcLatexFileCorrectness(src_path)
        filesExtensionInSections(sections_path)
        if necessarySectionsFilesPresence(sections_path, necessary_sections_files):
            titlePageFileCorrectness(sections_path, dir)
            styleFileCorrectness(sections_path, dir)
            # check version PRE: title_page.tex and style.tex verified for correctness (to exclude parsing errors)
            versionCorrectness(sections_path)
            # TODO: checkPackagesFileCorrectness(sections_path)


# TODO: check if itemize has an ending semicolon
latex_files = [file for file in files_w_allowed_ext if file.suffix == '.tex']
latexFilesCorrectness([workingDir/'prova_latex.tex'])
