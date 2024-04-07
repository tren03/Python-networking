import asyncio

# A shared counter variable
counter = 0

async def increment_counter(semaphore):
    global counter
    async with semaphore:
        print("Acquired semaphore")
        counter += 1
        await asyncio.sleep(1)  # Simulate some asynchronous task
        print("Counter:", counter)
    print("Released semaphore")

async def main():
    # Create a semaphore with a limit of 2 concurrent accesses
    semaphore = asyncio.Semaphore(2)

    # Create multiple coroutines accessing the shared resource
    coroutines = [increment_counter(semaphore) for _ in range(5)]

    # Execute the coroutines concurrently
    await asyncio.gather(*coroutines)

# Run the main coroutine
asyncio.run(main())
