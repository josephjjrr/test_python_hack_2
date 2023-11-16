"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(result):

    if len(result) >= 8:
        result = result[1:-1]
    return result