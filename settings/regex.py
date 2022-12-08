from pathlib import Path
from settings.expression_file import *

def checkLatexFilesCorrectness():

    # file's extension which are checks
    extensions = ['.txt', '.tex', '.py', '.pdf']

    wd = Path(Path.cwd().parent) 

    # all files name in the wd that have extensions extension are controlled
    files = [file for file in wd.rglob('*') if file.suffix in extensions]
    for file in files:
        if not titleCorrectness(file.stem):
            print('Name not correct: ', file)

        # other check like structure... 
    
    
    
    official_docs_dir = [
        '*/Analisi dei requisiti/',
        '*/Norme di progetto/',
        '*/Piano di progetto/',
    ]

    for dir_name in official_docs_dir:
        dir = Path(dir_name)

        # directories tree is '*/dir_name/src/sections/'
        if not (dir/'src/sections/').exists():
            print ('Directories tree not correct ', dir)
        else:
            # dir has only one .pdf file
            if len(list(dir.glob('*.pdf'))) != 1:
                print ('More than one pdf file in ', dir)
            # TODO parte only

            # '*/dir_name/src/' has only one .tex file
            if len(list((dir/'src').glob('*.tex'))) != 1:
                print ('More than one tex file in ', dir/'src')
            # TODO parte only
            
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
