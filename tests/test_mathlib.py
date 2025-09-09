import pytest
from mathlib import square, factorial, is_prime, gcd, lcm

# Square Tests
def test_square_positive():
    assert square(5) == 25

def test_square_negative():
    assert square(-4) == 16

def test_square_zero():
    assert square(0) == 0

# Factorial Tests
def test_factorial_small():
    assert factorial(5) == 120

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-3)

# is_prime Tests
def test_is_prime_true():
    assert is_prime(13) is True

def test_is_prime_false():
    assert is_prime(12) is False

def test_is_prime_edge_cases():
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-7) is False

# GCD Tests
def test_gcd_regular():
    assert gcd(48, 18) == 6

def test_gcd_coprime():
    assert gcd(17, 13) == 1

def test_gcd_with_zero():
    assert gcd(0, 5) == 5
    assert gcd(7, 0) == 7


# LCM Tests
def test_lcm_regular():
    assert lcm(4, 6) == 12

def test_lcm_coprime():
    assert lcm(7, 5) == 35

def test_lcm_with_zero():
    assert lcm(0, 10) == 0
    assert lcm(15, 0) == 0
