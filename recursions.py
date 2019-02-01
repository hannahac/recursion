def power(number, power_to_raise):
    #2^4 = 2*2*2*2
    #2^4 = 2^3*2
    
    if power_to_raise > 1:
        power_to_raise = power_to_raise - 1
        return number * power(number, power_to_raise)
    else:
        return 1

result = power(3, 8)
print(result)        