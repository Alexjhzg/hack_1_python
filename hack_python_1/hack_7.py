"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    count = 5
    while count > -1:
        result.append(count)
        count -= 1
        
    return result

fn_hack_7()