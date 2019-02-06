def power(number, power_to_raise):
    #2^4 = 2*2*2*2
    #2^4 = 2^3*2
    
    if power_to_raise > 1:
        power_to_raise = power_to_raise - 1
        return number * power(number, power_to_raise)
    elif power_to_raise < 0:
        raise Exception("Math error")    
    else:
        return 1

result = power(3, -4)
print(result)        