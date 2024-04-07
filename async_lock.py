# When using a shared resource, if we need to some operation that needs to run without any other co routine running in between, we can use lock feature

import asyncio

# A shared counter variable
counter = 0

async def increment_counter(lock):
    global counter
    async with lock:
        print("Acquired lock")
        counter += 1
        await asyncio.sleep(1)  # Simulate some asynchronous task
        print("Counter:", counter)
    print("Released lock")

async def main():
    # Create an async lock
    lock = asyncio.Lock()

    # Create multiple coroutines accessing the shared resource - created when we call async function
    coroutines = [increment_counter(lock) for _ in range(5)]

    # Execute the coroutines concurrently
    await asyncio.gather(*coroutines)

# Run the main coroutine
asyncio.run(main())

