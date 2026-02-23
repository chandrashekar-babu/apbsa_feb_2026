import asyncio
import time

async def foo(n):
    while n > 0:
        print("Running foo with n =", n)
        n -= 1
        if n % 2 == 0:
            while True: pass

        await asyncio.sleep(0.5)

async def bar(n):
    while n > 0:
        print("Running bar with n =", n)
        n -= 1
        await asyncio.sleep(0.5)

async def main():
    await asyncio.gather(foo(10), bar(10))

if __name__ == "__main__":
    asyncio.run(main())