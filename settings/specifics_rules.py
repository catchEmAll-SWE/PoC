import re
# In this file you can find function (them identify rules) for latex file's rules

# MACRO RULES

def titleCorrectness(title):
    file_name_rules = '[a-z]+\d*(_[a-z]+\d*)*$'
    official_doc_rules = '[a-z]+(_[a-z]+)*_v\.\d\d*\.\d\d*\.\d\d*$'

    # brief description
    # name:
    #   - first character must be a lowercase letter
    #   - the other letters must be lowercase letter or '_'
    # version (after name):
    #   - _v. << [0, 99] >>.<< [0, 99] >>.<<[0,99]>>

    return (bool(re.match(official_doc_rules, title)), True) [bool(re.match(file_name_rules, title))]


def srcLatexFileCorrectness(file):
    checks = {
        r'.*\\documentclass\[10pt\]\{article\}.*': 'font size',
        r'.*\\input\{sections/packages\}.*': 'packages file',
        r'.*\\input\{sections/style\}.*': 'style file',
        r'.*\\input\{sections/title_page\}.*': 'title page',
        r'.*\\pagenumbering\{roman\}.*': 'page roman numbering',
        r'.*\\tableofcontents.*': 'table of contents',
    }

    file_as_string = file.read_text()
    errors = []
    for check in checks:
        if not re.search(check, file_as_string):
            errors.append(checks[check])
    if errors:
        print('\nFollowing errors in style.tex:')
        [print(' - ', error) for error in errors]
        
def titlePageFileCorrectness(file):
    checks = {
        r'.*\\includegraphics\[scale = 0.05\]\{img/UniPD_Logo.png\}.*': 'unipd logo presence',
        r'.*\\large \\textbf\{Università degli Studi di Padova\}.*': 'bold text "università degli studi di padova"',
        r'.*\\includegraphics\[scale = 1.5\]\{img/logo.png\}.*': 'catch em all logo', 
        r'.*\\large \\textbf\{Catch em All - \\textit\{CAPTCHA: Umano o Sovraumano\?\}\}.*': 'Catch em All - project name',
        r'.*\\texttt\{Email: catchemallswe3@gmail.com\}.*': 'catch em all email',
        r'.*\{\\fontfamily\{ptm\}\\fontsize\{1.5cm\}\{0\}\\selectfont Analisi dei requisiti\}.*': 'doc title',
        (r'\\begin\{tabularx\}\{\\textwidth\}\{\| c \| c \|\}'
		r'\\hline'
		r'\\textbf\{Versione\} & .*'
		r'\\hline'
		r'\\textbf\{Approvazione\} & .*'
		r'\\hline'
		r'\\textbf\{Redazione\} & .*'
		r'\\hline'
		r'\\textbf\{Verifica\} & .*'
		r'\\hline'
		r'\\textbf\{Stato\} & .*'
		r'\\hline'
		r'\\textbf\{Uso\} & .*'
		r'\\hline'
		r'\\textbf\{Distribuzione\} & .*'
		r'\\hline'
	    r'\\end\{tabularx\}.*'): 'status table',
    }

    file_as_string = file.read_text()
    errors = []
    for check in checks:
        if not re.search(check, file_as_string):
            errors.append(checks[check])
    if errors:
        print('\nFollowing error in title_page.tex:')
        [print(' - ', error) for error in errors]

# ===========================================================================================================================
