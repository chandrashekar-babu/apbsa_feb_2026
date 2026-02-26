import asyncio

async def foo():
    for i in range(10):
        print(f"foo: counting {i}")
        await asyncio.sleep(1)

async def bar():
    for i in range(10):
        print(f"bar: counting {i}")
        await asyncio.sleep(1)

async def main():
    print("main: started...")
    await asyncio.gather(foo(), bar())
    print("main: all workers finished.")


if __name__ == '__main__':
    asyncio.run(main())
    