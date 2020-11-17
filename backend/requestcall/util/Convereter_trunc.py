from math import trunc



def truncater(input):
    # length = len(str(input))
    value = trunc(input*100)/100
    if value == 0:
        value = int(value)
    return value

def converter(input_text):
    if not isinstance(input_text, str):
        input_text = str(input_text)
    outtab='۱۲۳۴۵۶۷۸۹۰/-'
    intab='1234567890.-'
    translation_table = str.maketrans(intab, outtab)
    output = input_text.translate(translation_table)

    return output