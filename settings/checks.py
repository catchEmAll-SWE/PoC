from pathlib import *
import re
import collections
import specific_rules as srules
import github_action_utils as gha_utils


def filesNameCorrectness(files):
    """Control files name correctness
    :param files: files you want to control
    :type files: list[Path]
    """
    for file in files:
        if srules.fileNameCorrectness(file.stem):
            return
        else:
            print('Name not correct: ', file)
# POST = print not correct files name path


def officialDocsDirTree(dir):
    """Control dir directories's structure coherence with official dir's structure
    :param dir: official dir you want to control
    :type dir: Path
    :return: True if structure is coherence, False otherwise
    """
    # directory tree is '*/dir_name/src/sections/'
    if (dir/'src/sections/').exists():
        return True
    else:
        print('Directory tree not correct ', dir)
        return False


def officialPdfPresenceOnly(dir):
    """Check if official doc dir has only one file and it is a pdf file

    :param dir: directory in which we want to check files
    :type dir: Path (absolute path)
    :return: None
    """

    files_dic = collections.Counter(getDirectoryExtensions(dir))
    pdfDocPresence(dir, files_dic)
    singlePdfDocInOfficialDir(dir, files_dic)


def pdfDocPresence(dir, files_dic):
    """Official doc dir must have only one .pdf file

    :param dir: official doc dir
    :type dir: Path
    :param files_dic: dictionary with file extensions as keys and number of files with that extension as values
    :type files_dic: dict
    :return: None
    """

    if not (files_dic['.pdf'] == 1):
        print(dir, 'must have exactly one pdf file')


def singlePdfDocInOfficialDir(dir, dir_files):
    """Official doc dir must have only one file

    :param dir: official dir
    :type dir: Path
    :param dir_files: dictionary with file extensions as keys and number of files with that extension as values
    :type files_dic: dict
    :return: None
    """

    if not (len(dir_files) == 1):
        print(dir, 'cannot have more than one file in it')


def latexFilePresenceInSrc(src):
    """source directory (*/dir_name/src/) has only one .tex file

    :param src: source directory
    :type src: Path (absolute path)
    :return: True if source directory has only one .tex file, False otherwise
    :rtype: bool
    """

    src_files_dic = collections.Counter(getDirectoryExtensions(src))
    if (len(src_files_dic) == 1 and src_files_dic['.tex']):
        return True
    else:
        print(src, 'must have exactly one latex file')
        return False


def srcLatexFileCorrectness(src):
    """Control main.tex file correctness
    :param src: official source file
    :type src: Path 
    """
    src_file = next(src.glob('*.tex'))
    srules.srcLatexFileCorrectness(src_file)


def onlyLatexFilesInSection(sections):
    """Control sections dir has only latex files
    :param sections: sections directory
    :type sections: Path
    """
    files_in_sections = getDirectoryExtensions(sections)
    if not (len(collections.Counter(files_in_sections)) == 1 and collections.Counter(files_in_sections)['.tex']):
        print(sections, 'must have only latex files')


def necessarySectionsFilesPresence(sections, necessary_files):
    """Control if sections passed as param has necessary files
    :param sections: sections dir you want to control
    :type sections: Path
    :param necessary_files: necessary files in sections dir
    :type necessary_files: list[string]
    :return: True if sections passed has necessary files, False otherwise
    :rtype: bool
    """
    presence = True
    for file_name in necessary_files:
        if not (sections/file_name).exists():
            print(sections, 'must have ', file_name)
            presence = False
    return presence


def titlePageFileCorrectness(title_page_file, dir):
    """Check if title_page.tex has the name coherent with the main directory name

    :param title_page_file: title_page file you want to control
    :type title_page_file: Path (absolute path)
    :param dir: main directory
    :type dir: Path
    :return: None
    """
    # file_name = sections.strip('/sections').strip('/src').strip('/').split('/')[-1] #alternativa se PRE = non cambiano le directory
    # strip '/' and get main directory name
    file_name = str(dir).strip('/').split('/')[-1].capitalize()
    srules.titlePageFileCorrectness(title_page_file, file_name)


def styleFileCorrectness(style_file, dir):
    """Check if style.tex has the correct settings fot stylings

    :param style_file: 
    :type style_file: Path
    :param dir: main directory
    :type dir: Path
    :return: None
    """
    # file_name = sections.strip('/sections').strip('/src').strip('/').split('/')[-1] #alternativa se PRE = non cambiano le directory
    # strip '/' and get main directory name
    file_name = str(dir).strip('/').split('/')[-1].capitalize()
    srules.stylePageFileCorrectness(style_file, file_name)


def modificheFileCorrectness(modifiche_file):
    """Control sections/modifiche.tex correctness
    :param modifiche_file: modifiche file
    :type modifiche_file: Path  
    """
    srules.modificheFileCorrectness(modifiche_file)
    versionsOrderInModificheFileCorrectness(modifiche_file)


def versionsOrderInModificheFileCorrectness(modifiche_file):
    """Get version from modifiche.tex and check versions correctness in descending order with no duplicates

    :param modifiche_file: path to modifiche file
    :type modifiche_file: Path
    :return: True if versions in modifiche file are in descending order with no duplicates
    :rtype: bool
    """
    versions = srules.getVersionsFromModificheFile(modifiche_file)

    prev_version = sum([int(i)*(10**iteration) for i, iteration in zip(
        versions[0].split('.')[::-1], range(0, len(versions[0].split('.'))))])

    for version in versions[1:]:
        cur_version = sum([int(i)*(10**iteration) for i, iteration in zip(
            version.split('.')[::-1], range(0, len(version.split('.'))))])
        if (cur_version > prev_version or cur_version == prev_version):
            print('Version order not correct or same version used in ', modifiche_file, ': ',
                  cur_version, prev_version)
            return False
        else:
            prev_version = cur_version
    return True


def versionCorrectnessInSectionsFiles(sections_path):
    """Check if version in sections files is coherent with modifiche.tex

    :param sections_path: path to sections directory
    :type sections_path: Path
    :return: None
    """
    version = srules.getLatestVersionFromModificheFile(
        sections_path/'modifiche.tex')
    titlePageVersionCorrectness(sections_path/'title_page.tex', version)
    styleFileVersionCorrectness(sections_path/'style.tex', version)


def titlePageVersionCorrectness(titlePage_file, version):
    """Check if title page is coherent with version

    :param titlePage_file: path to title_page file
    :type sections_path: Path
    :param version: latest version of the official document
    :type version: str
    """
    if version:
        version_search = re.findall(r'\\textbf\{Versione\}\s*&\s*\(' + version +
                                    r'\)\s*\\\\\s*', titlePage_file.read_text())
        if len(version_search) > 1:
            print(
                'Multiple versions found in ', titlePage_file, ', check for duplicates')
        elif not version_search:
            # PRE: title_page.tex has been checked for version string presence
            print('Version number not correct in ', titlePage_file)


def styleFileVersionCorrectness(style_file, version):
    """Check if style file is coherent with version

    :param style_file: path to style file
    :type style_file: Path
    :param version: version of the document
    :type version: str
    """
    if re.search(r'\\fancyfoot\s*\[L\].*v\s'+version+r'\s*}', style_file.read_text()):
        return
    else:
        print('Version number not correct in ', style_file)


def latexFilesCorrectness(latex_files):
    """Check latex files correctness

    :param latex_files: latex_files you want to controll correctness
    :type obj_found: list[Path]

    Invoke follow function:
    :py:func:srules.itemizeListCorrectness
    """

    for file in latex_files:
        srules.listCorrectness(file)


# ======================================================== auxiliar functions ============================================================================
# if i am here ==> no failure ==> files are corrects


def getDirectoryExtensions(dir, recursive=False):
    files = getFilesFromDir(dir, recursive)
    return [file.suffix for file in files]


def getFilesFromDir(dir, recursive=False):
    if not recursive:
        return [file for file in dir.glob('*') if file.is_file()]
    else:
        return [file for file in dir.rglob('*') if file.is_file()]
