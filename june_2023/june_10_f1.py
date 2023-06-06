def check_prime(number):
    #true if prime
    #false if not
    if number < 2:
        return False
    i = 2
    while i*i <= number:
        if number%i == 0:
            return False
        i += 1
    return True
