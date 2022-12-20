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

# Path to working directory, TODO:find a way to get project root dir (chatchEmAll-Docs)
workingDir = Path('.').absolute()

# ================================================ checks =========================================================
filesNameCorrectness([file for file in workingDir.rglob(
    '*') if file.suffix in allowed_extensions])  # check if files have correct extension

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
            versionCorrectness(sections_path)  # check version
            # TODO: modificheVersion(sections_path, version) #check version
            # TODO: titlePageCorrectness(sections_path, version) #title_page version updated with modifiche version
            # TODO: styleFileCorrectness(sections_path, version) #file footer version updated with title_page and modifiche and styles
            # TODO: checkPackagesFileCorrectness(sections_path)
            titlePageFileCorrectness(sections_path, dir)
        # TODO: check if itemize has an ending semicolon
