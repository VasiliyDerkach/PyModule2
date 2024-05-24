def test(a,   *b, d=4, **c):
    print(a, d, b, c)

def factorial(n):
    if n == 1:
        return n
    else:
        return n*(n-1)

print(factorial(10))

test('999', 2, 3, 4, 6, 0, new= 'y', old= 'n')
test('999', 2, 3, 4, 6, 0, d=9, new='y', old='n')