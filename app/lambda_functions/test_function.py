from common_test import calc 

def lambda_handler(event, context): 
    
    a = 1
    b = 2
    
    return calc(a, b)