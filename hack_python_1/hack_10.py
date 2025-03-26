"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    sustitutos = {
        'o': '0',
        'i': '1',
        'a': '@',
    }
    resultado = []
    
    for letter in result:
        resultado.append(sustitutos.get(letter, letter.upper()))
        
    return resultado

fn_hack_10()

