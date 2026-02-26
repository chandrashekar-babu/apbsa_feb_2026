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
    async with asyncio.TaskGroup() as tg:
        print("Create a task for foo...")
        task1 = tg.create_task(foo())

        print("Create a task for bar...")
        task2 = tg.create_task(bar())

        print("main: waiting for tasks to complete...")
    print("main: all workers finished.")


if __name__ == '__main__':
    asyncio.run(main())
    