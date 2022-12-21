from pathlib import *
import re
import collections
import specific_rules as srules


def filesNameCorrectness(files):
    for file in files:
        if srules.titleCorrectness(file.stem):
            return
        else:
            print('Name not correct: ', file)
# POST = print not correct files name path


def officialDocsDirTree(dir):
    # directory tree is '*/dir_name/src/sections/'
    if (dir/'src/sections/').exists():
        return True
    else:
        print('Directory tree not correct ', dir)
        return False
# POST = print 'Directory tree not correct dir' and return false if directory dir tree is not correct
#        otherwise return True


def officialPdfPresenceOnly(dir):
    """Check if official doc dir has only one file and it is a pdf file

    :param dir: directory in which we want to check files
    :type dir: Path (absolute path)
    :return: None
    """

    files_dic = collections.Counter(getDirectoryExtensions(dir))
    pdfDocPresence(dir, files_dic)
    singleFileInDir(dir, files_dic)


def pdfDocPresence(dir, files_dic):
    """Official doc dir must have only one .pdf file

    :param files_dic: dictionary with file extensions as keys and number of files with that extension as values
    :type files_dic: dict
    :return: None
    """

    if not (files_dic['.pdf'] == 1):
        print(dir, 'must have exactly one pdf file')


def singleFileInDir(dir, dir_files):
    """Official doc dir must have only one file

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
    src_file = next(src.glob('*.tex'))
    srules.srcLatexFileCorrectness(src_file)


def filesExtensionInSections(sections):
    files_in_sections = getDirectoryExtensions(sections)
    if not (len(collections.Counter(files_in_sections)) == 1 and collections.Counter(files_in_sections)['.tex']):
        print(sections, 'must have only latex files')


def necessarySectionsFilesPresence(sections, files_name):
    presence = True
    for file_name in files_name:
        if not (sections/file_name).exists():
            print(sections, 'must have ', file_name)
            presence = False
    return presence


def titlePageFileCorrectness(sections, dir):
    """Check if title_page.tex has the name coherent with the main directory name

    :param sections: path to sections directory
    :type sections: Path (absolute path)
    :param dir: main directory
    :type dir: Path (absolute path)
    :return: None
    """
    title_page_file = sections/'title_page.tex'
    # file_name = sections.strip('/sections').strip('/src').strip('/').split('/')[-1] #alternativa se PRE = non cambiano le directory
    # strip '/' and get main directory name
    file_name = str(dir).strip('/').split('/')[-1].capitalize()
    srules.titlePageFileCorrectness(title_page_file, file_name)


def styleFileCorrectness(sections, dir):
    """Check if style.tex has the correct settings fot stylings

    :param sections: path to sections directory
    :type sections: Path (absolute path)
    :param dir: main directory
    :type dir: Path (absolute path)
    :return: None
    """
    title_page_file = sections/'style.tex'
    # file_name = sections.strip('/sections').strip('/src').strip('/').split('/')[-1] #alternativa se PRE = non cambiano le directory
    # strip '/' and get main directory name
    file_name = str(dir).strip('/').split('/')[-1].capitalize()
    srules.stylePageFileCorrectness(title_page_file, file_name)


def versionCorrectness(sections_path):
    """Check if version is coherent with modifiche.tex

    :param sections_path: path to sections directory
    :type sections_path: Path (absolute path)
    :return: None
    """
    version = modificheVersion(sections_path)
    titlePageVersionCorrectness(sections_path, version)
    styleFileVersionCorrectness(sections_path, version)


def modificheVersion(sections_path):
    """Get version from modifiche.tex and check for file correctness in descending order with no duplicates

    :param sections_path: path to sections directory
    :type sections_path: Path (absolute path)
    :return: version
    :rtype: str
    """
    modifiche_file = sections_path/'modifiche.tex'
    versions = srules.modificheVersion(modifiche_file)

    prev_version = sum([int(i)*(10**iteration) for i, iteration in zip(
        versions[0].split('.')[::-1], range(0, len(versions[0].split('.'))))])

    last_version = versions[0]

    for version in versions[1:]:
        cur_version = sum([int(i)*(10**iteration) for i, iteration in zip(
            version.split('.')[::-1], range(0, len(version.split('.'))))])
        if (cur_version > prev_version or cur_version == prev_version):
            print('Version order not correct or same version used in ', modifiche_file, ': ',
                  cur_version, prev_version)
            return False
        else:
            prev_version = cur_version
    return last_version


def titlePageVersionCorrectness(sections_path, version):
    """Check if title page is coherent with version

    :param sections_path: path to sections directory
    :type sections_path: Path (absolute path)
    :param version: version of the document
    :type version: str
    """
    if version:
        titlePage_file = sections_path/'title_page.tex'
        version_search = re.findall(r'\\textbf\{Versione\}\s*&\s*\(' + version +
                                    r'\)\s*\\\\\s*', titlePage_file.read_text())
        if len(version_search) > 1:
            print(
                'Multiple versions found in ', titlePage_file, ', check for duplicates')
        elif not version_search:
            # PRE: title_page.tex has been checked for version string presence
            print('Version number not correct in ', titlePage_file)


# TODO: check if style.tex is correct
def styleFileVersionCorrectness(sections_path, version):
    """Check if style file is coherent with version

    :param sections_path: path to sections directory
    :type sections_path: Path (absolute path)
    :param version: version of the document
    :type version: str
    """
    style_file = sections_path/'style.tex'

def latexFilesCorrectness(latex_files):
    """Check latex_files correctness

    Invoke follow function:
    :py:func:declarationListEndingWithColon

    :param latex_files: latex_files controlled
    :type obj_found: list[Path]
    """
    declarationListEndingWithColon(latex_files)



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

