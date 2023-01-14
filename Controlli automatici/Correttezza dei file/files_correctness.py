from checks import *
from pathlib import Path
import sys
import github_action_utils as gha_utils
from print_error import PrintError


def main() -> int:
    # ================================================ settings =========================================================

    allowed_extensions = ['.txt', '.tex', '.py', '.pdf']

    official_docs_dirs = [
        'Analisi dei requisiti/',
        'Norme di progetto/',
        'Piano di progetto/',
        'Piano di qualifica/',
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
            # in dir/src/
            if latexFilePresenceInSrc(src_path):
                srcLatexFileCorrectness(src_path)
            # in dir/src/sections/
                onlyLatexFilesInSection(sections_path)
                if necessarySectionsFilesPresence(sections_path, necessary_sections_files):
                    titlePageFileCorrectness(sections_path/'title_page.tex', dir)
                    styleFileCorrectness(sections_path/'style.tex', dir)
                    modificheFileCorrectness(sections_path/'modifiche.tex')
                    # check version PRE: title_page.tex and style.tex verified for correctness (to exclude parsing errors)
                    versionCorrectnessInSectionsFiles(sections_path, dir)

    latex_files = [
        file for file in files_w_allowed_ext if file.suffix == '.tex']
    with gha_utils.group('Latex files correctness'):
        latexFilesCorrectness(latex_files)
    sys.exit(PrintError.build_status.value)


if __name__ == '__main__':  # to define that this is a script and not a module
    main()
