from pathlib import *
import collections
import specifics_rules as srules


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


def necessaryFiles(dir):
    """Check if official doc dir has only one file and it is a pdf file

    :param dir: directory in which we want to check files
    :type dir: Path (absolute path)
    :return: None"""

    files_dic = collections.Counter(getDirectoryExtensions(dir))
    pdfDocPresence(dir, files_dic)
    singleFileInDir(dir, files_dic)


def pdfDocPresence(dir, files_dic):
    """Official doc dir must have only one .pdf file

    :param files_dic: dictionary with file extensions as keys and number of files with that extension as values
    :type files_dic: dict
    :return: None"""

    if not (files_dic['.pdf'] == 1):
        print(dir, 'must have exactly one pdf file')


def singleFileInDir(dir, dir_files):
    """Official doc dir must have only one file

    :param dir_files: dictionary with file extensions as keys and number of files with that extension as values
    :type files_dic: dict
    :return: None"""

    if not (len(dir_files) == 1):
        print(dir, 'cannot have more than one file')


def latexFilePresenceInSrc(src):
    # '*/dir_name/src/' has only one .tex file
    src_files_ext = collections.Counter(getDirectoryExtensions(src))
    if (len(src_files_ext) == 1 and src_files_ext['.tex']):
        return True
    else:
        print(src, 'must have one latex file')
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


def styleFileCorrectness(sections):
    style_file = sections/'style.tex'

# def checkStylePackagesCorrectness():


def titlePageFileCorrectness(sections):
    title_page_file = sections/'title_page.tex'
    srules.titlePageFileCorrectness(title_page_file)

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
