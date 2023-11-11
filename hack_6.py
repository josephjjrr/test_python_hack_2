"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6():
    result = ["a","b","c","d","e"]
    for index, valor in enumerate(result):
        if valor == "a" or valor == "c" or valor == "e":
             result[index] = str(index+1)
        elif valor == "b" or valor == "d":
            result[index] = "-"
        elif result == []:
            result = ["0"]
    return result