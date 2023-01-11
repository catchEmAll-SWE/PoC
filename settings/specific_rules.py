# In this file you can find function (them identify rules) for latex file's rules
import re
import github_action_utils as gha_utils
from print_error import *


def fileNameCorrectness(file_name):
    """Correctness of file name
    :param file_name: file name you want to control (without extension)
    :type file_name: string
    :retutn: True if name is valid, False otherwise
    :rtype: bool
    """
    # name:
    #   - first character must be a lowercase letter
    #   - the other letters must be lowercase letter or '_'
    # version (after name):
    #   - _v. << [0, 99] >>.<< [0, 99] >>.<<[0,99]>>

    file_name_rules = r'[a-z]+\d*(_[a-z]+\d*)*$'
    official_doc_rules = r'[a-z]+(_[a-z]+)*_v\.\d\d?\.\d\d?\.\d\d?$'

    return (bool(re.match(official_doc_rules, file_name)), True)[bool(re.match(file_name_rules, file_name))]


def srcLatexFileCorrectness(file):
    """Correctness of src/main.tex file
    :param file: src file
    :type file: Path
    """
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
        PrintSimpleError.print_error(errors, str(file)+' is not correct, errors:')


def titlePageFileCorrectness(file, name):
    """title_page file correctness
    :param file: title_page file
    :type file: Path
    :param name: name of official's document
    :type name: string 
    """
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
        PrintSimpleError.print_error(errors, str(file)+' is not correct, errors:')


def stylePageFileCorrectness(file, name):
    """style file correctness
    :param file: style file
    :type file: Path
    :param name: name of official's document
    :type name: string 
    """
    checks = {
        'section style': r'\\fancypagestyle\{section_style\}.*',
        'empty page style': r'\\thispagestyle\{empty\}',
        'fancy page style': r'\\thispagestyle\{fancy\}',
        'pagestyle definition': r'\\pagestyle\{fancy\}',
        'specifications for header and footer': r'\\fancyhf\{\}',
        'group name': r'\\fancyhead\[L\]\{\\textit\{Gruppo Catch em All\}\}',
        'head style': r'\\fancyhead\[R\]\{\\uppercase\{\\textbf\{\\leftmark\}\}\}',
        'doc title and version': r'\\fancyfoot\[L\]\{\\fontfamily\{qtm\}\\selectfont\s',
        'footer style': r'\\fancyfoot\[R\]\{Pagina \\thepage\~di\~\\pageref\{LastPage\}\}',
        'page counter': r'\\setcounter{page\}\{0\}',
        'page nubering': r'\\pagenumbering\{arabic\}',
        'headrulewidth': r'\\renewcommand\{\\headrulewidth\}\{0.4pt\}',
        'footrulewidth': r'\\renewcommand\{\\footrulewidth\}\{0.4pt\}',
        'table style C': r'\\newcolumntype\{C\}\[1\]\{>\{\\centering\\let\\newline\\\\\\arraybackslash\\hspace\{0pt\}\}m\{#1\}\}',
        'table style R': r'\\newcolumntype\{R\}\[1\]\{>\{\\raggedleft\\let\\newline\\\\\\arraybackslash\\hspace\{0pt\}\}m\{#1\}\}',
        'table style L': r'\\newcolumntype\{L\}\[1\]\{>\{\\raggedright\\let\\newline\\\\\\arraybackslash\\hspace\{0pt\}\}m\{#1\}\}',
    }

    file_as_string = file.read_text()
    errors = []
    for check in checks:
        if check == 'doc title and version':
            # letter 'v' has to have a space before and after
            if not re.search(checks[check] + name + r'\sv\s.*\}\s*', file_as_string):
                errors.append(check)
        elif not re.search(checks[check], file_as_string):
            errors.append(check)

    if errors:
        PrintSimpleError.print_error(errors, str(file)+' is not correct, errors:')


def modificheFileCorrectness(file):
    checks = {
        'title': r'\\section\*\{Registro delle modifiche\}\s*',
        'centering': r'\\begin\{center\}\s*',
        'proprieties': r'\\renewcommand\\tabularxcolumn\[1\]\{\>\{\\Centering\}m\{#1\}\}\s*',
        'definition': r'\\begin\{\\tabularx\}\{\\textwidth\}\{\|\sc|X\s\|\sc|X\s\|\sc|X\s\|\sc|X\s\|\sc|X\s\|}\s',
        'header': r'\\textbf\{Versione\}\s*&\s*\\textbf\{Data\}\s*&\s*\\textbf\{Descrizione\}\s*&\s*\\textbf\{Autore\}\s*&\s*\\textbf\{Ruolo\}.*',
        'data line': r'(\d\d?\.\d\d?\.\d\d?)\s*&\s*(\d\d/\d\d/\d\d\d\d)\s*&.*&.*&',
        'end': r'\\end\{tabularx\}.*',
        'end centering': r'\\end\{center\}.*',
    }

    file_as_string = file.read_text()
    errors = []

    for check in checks:
        if not re.search(checks[check], file_as_string):
            errors.append(check)

    if errors:
        PrintSimpleError.print_error(errors, str(file)+' is not correct, errors:')


def getVersionsFromModificheFile(file):
    """modifiche fule correctness
    :param file: modifiche file
    :type file: Path
    """
    return re.findall(r'\d\d?\.\d\d?\.\d\d?', file.read_text())


def getLatestVersionFromModificheFile(file):
    return re.search(r'\d\d?\.\d\d?\.\d\d?', file.read_text()).group(0)


def listCorrectness(file):
    """Check latex file list correctness as request in norme_di_progetto

    :param file: latex file you want to control list correctness
    :type file: Path

    :py:func:declarationListEndingWithColon
    :py:func:itemInListEndingWithSemicolon
    :py:func:declarationListEndingWithColon
    :py:func:firstLetterInListMustBeMaiusc
    """
    file_as_string = file.read_text(encoding="utf-8")
    missin_colon_lines = declarationListEndingWithColon(file_as_string)
    missin_semicolon_lines = itemInListEndingWithSemicolon(file_as_string)
    missing_dot_lines = itemInListEndingWithDot(file_as_string)
    minusc_first_item_letter = firstLetterInListMustBeMaiusc(file_as_string)
    if missin_colon_lines or missin_semicolon_lines or missing_dot_lines or minusc_first_item_letter:
        gha_utils.notice("Errors in " + str(file) +
                         ":")
        if missin_colon_lines:
            printMissingCharacterLines(
                'Missing ":" in lists definition:', missin_colon_lines, file)
        if missin_semicolon_lines:
            printMissingCharacterLines(
                'Missing ";" in items:', missin_semicolon_lines, file)
        if missing_dot_lines:
            printMissingCharacterLines(
                'Missing "." in last item:', missing_dot_lines, file)
        if minusc_first_item_letter:
            printMissingCharacterLines(
                'Minusc first item letter:', minusc_first_item_letter, file)


def printMissingCharacterLines(error_message, lines, file):
    PrintErrorsWithLines.print_error([error_message], lines)


def declarationListEndingWithColon(file):
    """Return lines's missing ':' in list declaration in the file passed 

    :param file: latex file we want to control
    :type file: string
    :return: list of missing colon lines
    :rtype: list[string] 
    """
    missing_colon = re.finditer(
        r'[^:]\s*\n(?=\s*\\begin\s*{(itemize|enumerate)})', file)
    missing_colon_lines = []
    for obj in missing_colon:
        missing_colon_lines.append(getMatchedStringLine(obj, file))
    return missing_colon_lines


def itemInListEndingWithSemicolon(file):
    """Return lines's missing ';' in item in the file passed 

    :param file: latex file we want to control
    :type file: string
    :return: list of missing semi colon lines
    :rtype: list[string] 
    """
    missing_semicolon = re.finditer(r'\\item.*[^;]\s*\n(?=\s*\\item)', file)
    missing_semicolon_lines = []
    for obj in missing_semicolon:
        missing_semicolon_lines.append(getMatchedStringLine(obj, file))
    return missing_semicolon_lines


def itemInListEndingWithDot(file):
    """Return lines's missing '.' in last item in the file passed 

    :param file: latex file we want to control
    :type file: string
    :return: list of missing dot lines
    :rtype: list[string] 
    """
    missing_dot = re.finditer(
        r'\\item.*[^\.]\s*\n(?=\s*\\end\s*{(itemize|enumerate)})', file)
    missing_dot_lines = []
    for obj in missing_dot:
        missing_dot_lines.append(getMatchedStringLine(obj, file))
    return missing_dot_lines


def firstLetterInListMustBeMaiusc(file_as_string):
    """Return lines's with first minusc letter in item in the file passed 

    :param file: latex file we want to control
    :type file: string
    :return: list of first minusc letter lines
    :rtype: list[string] 
    """
    pattern = r'\\item\s*[a-z]'
    minusc_letters = re.finditer(pattern, file_as_string)
    minusc_letter_lines = []
    for obj in minusc_letters:
        minusc_letter_lines.append(getMatchedStringLine(obj, file_as_string))
    return minusc_letter_lines


def getMatchedStringLine(obj_found, text):
    """Return the line's number of the obj_found in the text

    :param obj_found: element we ewant to now line's number
    :type obj_found: Match Object
    :param text: text which contains obj_found string
    :type text: string
    """
    start_character_number = obj_found.start()
    lines_in_text = re.finditer(r'\n', text)
    line_number = 1
    for iterator in lines_in_text:
        if iterator.start() < start_character_number:
            line_number += 1
    return line_number
# POST = return the line's number of the obj_found in the text
# ===========================================================================================================================
