""""""
# patch

def m(string):
    output = ""
    for element in string:
        if element not in output:
            output += element
    return output

print(m("pythontestlatest"))
# pythonesla
"""