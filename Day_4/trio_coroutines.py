import trio

async def foo():
    for i in range(10):
        print(f"foo: counting {i}")
        await trio.sleep(1)

async def bar():
    for i in range(10):
        print(f"bar: counting {i}")
        await trio.sleep(1)

async def main():
    print("main: started...")
    async with trio.open_nursery() as nursery:
        print("main: spawning foo...")
        nursery.start_soon(foo)

        print("main: spawning bar...")
        nursery.start_soon(bar)

        print("main: waiting for workers to complete")
    
    print("main: all workers finished.")


trio.run(main)