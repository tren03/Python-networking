import asyncio

async def coroutine1():
    print("Coroutine 1 started")
    await asyncio.sleep(2)  # Simulate some asynchronous task
    print("Coroutine 1 completed")

async def coroutine2():
    print("Coroutine 2 started")
    await asyncio.sleep(1)  # Simulate some asynchronous task
    print("Coroutine 2 completed")

async def coroutine3():
    print("Coroutine 3 started")
    await asyncio.sleep(3)  # Simulate some asynchronous task
    print("Coroutine 3 completed")

async def main():
    # Create tasks with each coroutine
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())
    task3 = asyncio.create_task(coroutine3())

    # Await each task separately
    await task1
    await task2
    await task3

    # We can also use this syntax to run all 3 routines concurrently
    await asyncio.gather(coroutine1(),coroutine2(),coroutine3())

    # This is a context manager and provides capability to handle errors in concurrent tasks - this didnt work :(
    async with asyncio.TaskGroup() as tg:
        tg.create_task(coroutine1())
        tg.create_task(coroutine2())
        tg.create_task(coroutine3())

# Run the main coroutine
asyncio.run(main())
