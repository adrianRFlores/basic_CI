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
        result *= i
    return result