"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(result):
    
    return result
def fn_hack_7(result):
    index = 0

    if len(result) == 0:
        result.append(0)
    else:
        while index < len(result):
            result.append(str(index + 1))
            index += 1
            if index < len(result):
                result.append(index + 1)
                index += 1

    return result
"""
output = fn_hack_7(["a","b","c","d","e"])
print(output)

output = fn_hack_7([])
print(output)"""