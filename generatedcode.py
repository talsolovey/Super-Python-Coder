def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True



# Unit tests

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(16) == False
    assert is_prime(17) == True
    assert is_prime(-1) == False
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(29) == True
    assert is_prime(100) == False
    assert is_prime(97) == True
    assert is_prime(121) == False
    assert is_prime(2**31 - 1) == True  # Checking a large prime number

test_is_prime()  
