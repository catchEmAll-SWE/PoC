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
        r'.*\\input\{sections/packages\}.*': 'packages file presence',
        r'.*\\input\{sections/style\}.*': 'style file presence',
        r'.*\\input\{sections/title_page\}.*': 'title page presence',
        r'.*\\pagenumbering\{roman\}.*': 'page numbering',
        r'.*\\tableofcontents.*': 'table of contents presence',
    }

    file_as_string = file.read_text()
    errors = []
    for check in checks:
        if not re.search(check, file_as_string):
            errors.append(checks[check])
    if errors:
        print('\n', file, ' has the following errors:')
        [print(' - ', error) for error in errors]
        print('\n')
    else:
        print('No errors in ', file)
        



# ===========================================================================================================================
