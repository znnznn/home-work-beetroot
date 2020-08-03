import asyncio


async def factorials(n):
    print(f'start factorials {n}')
    k = n
    f = 1
    while n > 1:
        f *= n
        n -= 1
        await asyncio.sleep(1)
    print(f'end factorials digit {k} with result {f}')
    return f


async def factorials_recurs(n):
    print(f'start factorial recurs with {n}')
    if n == 1:
        return 1
    f = await factorials_recurs(n-1) * n
    return f


async def fibonacci(n):
    print(f'start fibonacci number {n}')
    fp1 = 0
    fn2 = 1
    i = 1
    fib = 1
    await asyncio.sleep(0.5)
    while i < n:
        fib = fp1 + fn2
        fp1 = fn2
        fn2 = fib
        i += 1
        await asyncio.sleep(0.5)
    print(f'end fibonacci number {n} with result {fib}')
    return fib


async def pow(n):
    print(f'start pow number {n}')
    k = n ** 2
    await asyncio.sleep(0.5)
    print(f'end pow digit {n} with result {k}')
    return k


async def pow_3(n):
    print(f'start pow number {n}')
    await asyncio.sleep (0.3)
    k = await pow(n) * n
    print(f'end pow_3 digit {n} with result {k}')
    return k


async def main1():
    for n in range(1, 11):
        await asyncio.gather(factorials(n), factorials_recurs(n), fibonacci(n), pow(n), pow_3(n))

print(asyncio.run(main1()))
