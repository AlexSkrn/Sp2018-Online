"""
test_generator.py

tests the solution to the generator lab

can be run with py.test or nosetests
"""

import generator_1 as gen


def test_intsum():

    g = gen.intsum()

    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 3
    assert next(g) == 6
    assert next(g) == 10
    assert next(g) == 15


'''
This test case is not used in generator_1 assignment
def test_intsum2(): 
'''


def test_doubler():

    g = gen.doubler()

    assert next(g) == 1
    assert next(g) == 2
    assert next(g) == 4
    assert next(g) == 8
    assert next(g) == 16
    assert next(g) == 32

    for i in range(10):
        j = next(g)

    assert j == 2**15


def test_fib():
    g = gen.fib()
    assert [next(g) for i in range(9)] == [1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_prime():
    g = gen.prime()
    for val in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        assert next(g) == val


def main():
    print("\n"+"1. Sum of integers:")
    print("==============================")
    test_intsum()

    print("\n"+"2. Double the previous value:")
    print("==============================")
    test_doubler()

    print("\n"+"3. Fibonacci sequence:")
    print("==============================")
    test_fib()

    print("\n"+"4. Prime numbers:")
    print("==============================")
    test_prime()


if __name__ == "__main__":
    main()

