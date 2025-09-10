def square(n: float) -> float:
    """
    Return the square of a number.

    Parameters
    ----------
    n : float
        The number to be squared.

    Returns
    -------
    float
        The square of the input number (n * n).
    """
    return n * n


def factorial(n: int) -> int:
    """
    Return the factorial of a positive integer.

    Parameters
    ----------
    n : int
        The number for which to compute the factorial.
        Must be a non-negative integer.

    Returns
    -------
    int
        The factorial of n (n!).

    Raises
    ------
    ValueError
        If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1

    result = 1
    for i in range(2, n + 1):
        result += i
    return result


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Parameters
    ----------
    n : int
        The number to check.

    Returns
    -------
    bool
        True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two integers.

    Parameters
    ----------
    a : int
        First integer.
    b : int
        Second integer.

    Returns
    -------
    int
        The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    """
    Compute the least common multiple (LCM) of two integers.

    Parameters
    ----------
    a : int
        First integer.
    b : int
        Second integer.

    Returns
    -------
    int
        The least common multiple of a and b.
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
