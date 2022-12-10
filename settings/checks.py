from pathlib import Path
import collections
import expression_file as rules

def checkFilesNameCorrectness(files):
    for file in files:
        if not rules.titleCorrectness(file.stem):
            print('Name not correct: ', file)
# POST = print not correct files name path 

    
def checkOfficialDocsDirTree(dir):
    # directory tree is '*/dir_name/src/sections/'
    if not (dir/'src/sections/').exists():
        print ('Directories tree not correct ', dir)
        return False
    return True
# POST = print 'Directory tree not correct dir' and return false if directory dir tree is not correct
#        otherwise return True


def checkOfficialDocPresence(dir):
    # official doc dir must has only one .pdf file
    dir_files = collections.Counter(dir.glob('*'))
    if not (len(dir_files) == 1 and dir_files.get('.pdf', False)):
        print (dir, 'must has only one pdf file')

def checkLatexFilePresenceInSrc(src):
    # '*/dir_name/src/' has only one .tex file
    src_files = collections.Counter(src.glob('*'))
    if not (len(src_files) == 1 and src_files.get('.tex', False)):
        print (src, 'must has only one latex file')
        return False
    return True

def checkSrcLatexFileCorrectness(src):
    src_file = next(src.glob('*.tex'))
    # TODO

            
def checkFilesExtensionInSections(sections):
    files_in_sections = sections.glob('*')
    if not (len(collections.Counter(files_in_sections)) == 1 and collections.Counter(files_in_sections).get('.tex', False)):
        print(sections, 'must have only latex files')

def checkNecessarySectionsFilesPresence(sections, files_name):
    presence = True
    for file_name in files_name:
        if not sections/file_name:
            print (sections, 'must have ', file_name)
            presence = False
    return presence

#def checkStyleFileCorrectness():

#def checkStylePackagesCorrectness():

#def checkStyleTitlePageCorrectness():
            

    #checkStyleCorrectness(necessary_sections_file[0])






    #if i am here ==> no failure ==> files are corrects


