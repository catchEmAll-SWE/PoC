import re
# In this file you can find function (them identify rules) for latex file's rules

# MACRO RULES


def titleCorrectness(title):
    file_name_rules = r'[a-z]+\d*(_[a-z]+\d*)*$'
    official_doc_rules = r'[a-z]+(_[a-z]+)*_v\.\d\d*\.\d\d*\.\d\d*$'

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


def titlePageFileCorrectness(file, name):
    checks = {
        'unipd logo presence': r'.*\\includegraphics\[scale = 0.05\]\{img/UniPD_Logo.png\}.*',
        'bold text "università degli studi di padova"': r'.*\\large \\textbf\{Università degli Studi di Padova\}.*',
        'catch em all logo': r'.*\\includegraphics\[scale = 1.5\]\{img/logo.png\}.*',
        'Catch em All - project name': r'.*\\large \\textbf\{Catch em All - \\textit\{CAPTCHA: Umano o Sovraumano\?\}\}.*',
        'catch em all email': r'.*\\texttt\{Email: catchemallswe3@gmail.com\}.*',
        # added dynamic name check
        'doc title': r'.*\{\\fontfamily\{ptm\}\\fontsize\{1.5cm\}\{0\}\\selectfont\s*',
        'definition': r'\\begin\{tabularx\}\{\\textwidth\}\{\s*\|\s*c\s*\|\s*c\s*\|\s*\}\s*',
        'version': r'\\textbf\{Versione\}\s*&.*',
        'approvation': r'\\textbf\{Approvazione\}\s*&.*',
        'redaction': r'\\textbf\{Redazione\}\s*&.*',
        'verification': r'\\textbf\{Verifica\}\s*&.*',
        'state': r'\\textbf\{Stato\}\s*&.*',
        'use': r'\\textbf\{Uso\}\s*&.*',
        'distribution': r'\\textbf\{Distribuzione\}\s*&.*',
        'end tabular': r'\\end\{tabularx\}.*',
    }

    file_as_string = file.read_text()
    errors = []
    for check in checks:
        if check == 'doc title':
            if not re.search(checks[check] + name + r'\}\s*\\\\', file_as_string):
                errors.append(check)
        elif not re.search(checks[check], file_as_string):
            errors.append(check)

    if errors:
        print('\nFollowing error in title_page.tex: ', file)
        [print(' - ', error) for error in errors]


def modificheVersion(file):
    checks = {
        'title': r'\\section\*\{Registro delle modifiche\}\s*',
        'centering': r'\\begin\{center\}\s*',
        'proprieties': r'\\renewcommand\\tabularxcolumn\[1\]\{\>\{\\Centering\}m\{#1\}\}\s*',
        'definition': r'\\begin\{\\tabularx\}\{\\textwidth\}\{\|\sc|X\s\|\sc|X\s\|\sc|X\s\|\sc|X\s\|\sc|X\s\|}\s',
        'header': r'\\textbf\{Versione\}\s*&\s*\\textbf\{Data\}\s*&\s*\\textbf\{Descrizione\}\s*&\s*\\textbf\{Autore\}\s*&\s*\\textbf\{Ruolo\}.*',
        # TODO: regex for date, version is already done
        'data line': r'(\d\d?\.\d\d?\.\d\d?)\s*&\s*(\d\d/\d\d/\d\d\d\d)\s*&.*&.*&',
        'end': r'\\end\{tabularx\}.*',
        'end centering': r'\\end\{center\}.*',
    }

    file_as_string = file.read_text()

    versions = []
    errors = []

    for check in checks:
        if check == 'data line':
            if re.search(checks[check], file_as_string):
                versions = [version[0]
                            for version in re.findall(checks[check], file_as_string)]
            else:
                errors.append(check)
        elif not re.search(checks[check], file_as_string):
            errors.append(check)

    if errors:
        print('\nFollowing error in modifiche_version.tex:')
        [print(' - ', error) for error in errors]

    # print(versions)  #remove this line, it's just for debug

    return versions




# ===========================================================================================================================
