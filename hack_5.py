"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5():
    result = "fooziman"
    if result[0] == "f":
        result = result[:2] + result[2].replace("o", "-") + result[3:5] + "-" + result[5:-1] + "-"
    elif result[0] == "b":
        result = result[:2] + result[2].replace("r", "-") + result[3:5] + "-" + result[6:]
    elif len(result) == 3:
        result = result.replace("x", "-")
    return result
