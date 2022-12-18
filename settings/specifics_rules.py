import re
from pathlib import Path
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

    return (bool(re.match(official_doc_rules, title)), True)[bool(re.match(file_name_rules, title))]


def srcLatexFileCorrectness(file):
    checks = {
        'font size': r'.*\\documentclass\[10pt\]\{article\}.*',
        'packages file': r'.*\\input\{sections/packages\}.*',
        'style file': r'.*\\input\{sections/style\}.*',
        'title page': r'.*\\input\{sections/title_page\}.*',
        'page roman numbering': r'.*\\pagenumbering\{roman\}.*',
        'table of contents': r'.*\\tableofcontents.*',
    }

    file_as_string = file.read_text()
    errors = []
    for check in checks:
        if not re.search(checks[check], file_as_string):
            errors.append(check)

    if errors:
        print('\nFollowing errors in style.tex:')
        [print(' - ', error) for error in errors]


def titlePageFileCorrectness(file):
    checks = {
        'unipd logo presence': r'.*\\includegraphics\[scale = 0.05\]\{img/UniPD_Logo.png\}.*',
        'bold text "università degli studi di padova"': r'.*\\large \\textbf\{Università degli Studi di Padova\}.*',
        'catch em all logo': r'.*\\includegraphics\[scale = 1.5\]\{img/logo.png\}.*',
        'Catch em All - project name': r'.*\\large \\textbf\{Catch em All - \\textit\{CAPTCHA: Umano o Sovraumano\?\}\}.*',
        'catch em all email': r'.*\\texttt\{Email: catchemallswe3@gmail.com\}.*',
        'doc title': r'.*\{\\fontfamily\{ptm\}\\fontsize\{1.5cm\}\{0\}\\selectfont Analisi dei requisiti\}.*',
        'status bar': (r'\\begin\{tabularx\}\{\\textwidth\}\{\| c \| c \|\}'
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
                       r'\\end\{tabularx\}.*'),
    }

    file_as_string = file.read_text()
    errors = []
    for check in checks:
        if not re.search(checks[check], file_as_string):
            errors.append(check)

    if errors:
        print('\nFollowing error in title_page.tex:')
        [print(' - ', error) for error in errors]

# ===========================================================================================================================
