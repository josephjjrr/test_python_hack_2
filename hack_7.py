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

    if result == [0]:
        result
    else:
        while index < len(result):
            result[index] = str(index + 1)
            index += 1
            if index == 1 or index == 3:
                result[index] = index + 1
                index += 1

    return result
print(fn_hack_7([0]))