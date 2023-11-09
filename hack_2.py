"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2():
    result = "fooziman"
    vocales = set("aeiouAEIOU")
    for vocal in vocales:
        result = result.replace(vocal, "")

    return result