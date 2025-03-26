"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1, 2, 3]
    new_list = []  
    i = 0
    
    while i < len(result):  
        new_list.append(result[i])  
        new_list.append('@')  
        i += 1
    
    result = new_list  
    return result

fn_hack_9()