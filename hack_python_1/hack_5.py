"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    sustitutos = {
        'o': '0',
        'i': '1',
        'a': '@',
    }
    resultado = []  
    
    for letter in result:
        resultado.append(sustitutos.get(letter, letter))  
        print(resultado)
    result = ''.join(resultado)
    
    return  result

fn_hack_5()