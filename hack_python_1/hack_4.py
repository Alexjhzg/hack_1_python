"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    result = result[:-1] + result[-1].upper()
    print(result)
    return result

fn_hack_4()