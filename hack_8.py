"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(result):
    index = 0
    for index, valor in enumerate(result):
        if len(result) == 5 or len(result) == 3:
            result[index] = valor + "-" + str(index + 1)
        else:
            result[index] = str(index + 1)
    result.reverse()
    return result
print(fn_hack_8(["a","b"]))