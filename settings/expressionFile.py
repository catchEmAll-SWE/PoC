import re
# In this file you can find function (tthem identify rules) for latex file's rules
#
# Rule must be added in regEx.py

# MACRO RULES

def titleCorrectness(title):
    name = '[a-z]+\d*(_[a-z]+\d*)*$'
    name_and_version = '[a-z]+(_[a-z]+)*_v\.\d\d*\.\d\d*\.\d\d*$'

    # brief description
    # name:
    #   - first character must be a lowercase letter
    #   - the other letters must be lowercase letter or '_'
    # version (after name):
    #   - _v. << [0, 99] >>.<< [0, 99] >>.<<[0,99]>>

    return (bool(re.match(name_and_version, title)), True) [bool(re.match(name, title))]






# ===========================================================================================================================
