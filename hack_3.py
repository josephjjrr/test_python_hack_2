"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3():
    result = "fooziman"
    result = result.replace("a" , "@")
    result = result.replace("e" , "3")
    result = result.replace("i" , "¡")
    result = result.replace("o" , "0")
    result = result.replace("u" , "v")
    return result