from pathlib import Path
import collections
from expression_file import *

def checkLatexFilesCorrectness():

    # file's extension which are checks
    extensions = ['.txt', '.tex', '.py', '.pdf']

    wd = Path('.').absolute()

    # all files name in the wd that have extensions extension are controlled
    files = [file for file in wd.rglob('*') if file.suffix in extensions]
    for file in files:
        if not titleCorrectness(file.stem):
            print('Name not correct: ', file)

        # other check like structure... 
    
    
    
    official_docs_dir = [
        'Analisi dei requisiti/',
        'Norme di progetto/',
        'Piano di progetto/',
    ]

    for dir_name in official_docs_dir:
        dir = wd/dir_name
        # directories tree is '*/dir_name/src/sections/'
        if not (dir/'src/sections/').exists():
            print ('Directories tree not correct ', dir)
        else:

            # official doc dir has only one .pdf file
            dir_files = collections.Counter(dir.glob('*'))
            if len(dir_files) == 1:
                if dir_files.get('.pdf', False):
                    print('File must be pdf in', dir)
                
            else:
                if len(dir_files) > 1:
                    print('Only one pdf file is admit in ', dir)
                else:
                    print(dir, 'must have a pdf file')
        

            # '*/dir_name/src/' has only one .tex file
            src_files = collections.Counter((dir/'src').glob('*.*'))
            if len(src_files) == 1:
                if src_files.get('.tex', False):
                    print('File must be latex in ', dir/'src/')
            else:
                if len(src_files) > 1:
                    print('Only one latex file is admit in ', dir/'src/')
                else:
                    print(dir/'src/', 'must have a latex file')
            
            # '*/dir_name/src/sections/' has:
            #   - only tex files TODO
            #   - styles.tex
            #   - packages.tex
            #   - title_page.tex
            
            sections_path = dir/'src/sections/'
            necessary_files_sections_dir = [
                'styles.tex',
                'packages',
                'title_page.tex',
            ]






    #if i am here ==> no failure ==> files are corrects

    
checkLatexFilesCorrectness()
