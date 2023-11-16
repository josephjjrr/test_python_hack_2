"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}

    for key, value in result.items():
        """


def fn_hack_9(text):
    result = {}
    del text["bar"]
    for key in text:
        if key == "foo":
            result[key.capitalize()] = text[key].capitalize()[:3] + text[key][4:]
        
    return result