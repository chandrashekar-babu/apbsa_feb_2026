import asyncio
#import time
async def foo():
    for i in range(10):
        print(f"In foo: counting {i}")
        #time.sleep(1)
        await asyncio.sleep(1)

async def bar():
    for i in range(10):
        print(f"In bar: counting {i}")
        await asyncio.sleep(1)

async def main():
    print("main invoked...")
    await asyncio.gather(foo(), bar())
    print("main complete...")


if __name__ == '__main__':
    asyncio.run(main())
