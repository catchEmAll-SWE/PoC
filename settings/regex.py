from pathlib import Path
from settings.expression_file import *

def checkLatexFilesCorrectness():

    # file's extension which are checks
    extensions = ['.txt', '.tex', '.py', '.pdf']

    # final / official document which version name are checks
    official_documents_name = [
        '*/Analisi dei requisiti/*.pdf',
        '*/Norme di progetto/*.pdf',
        '*/Piano di progetto/*.pdf',
    ]

    wd = Path(Path.cwd().parent) 

    # all files name in the wd that have extensions extension are controlled
    files = [file for file in wd.rglob('*') if file.suffix in extensions]
    for file in files:
        if not titleCorrectness(file.stem):
            print('Name not correct: ', file)

        # other check like structure... 
    
    

    #if i am here ==> no failure ==> files are corrects
    return True

    
checkLatexFilesCorrectness()
