import asyncio

async def fetch(delay):
    print("getting data")
    await asyncio.sleep(delay)
    print("fetched data")
    return {"data": "Some data"}





# coroutine function
async def main():
    print("start of main coroutine")
    task = fetch(4)
    # await the fetch coroutine pausing execution of main until fetch completes
    print("end of main coroutine")
    result = await task # we created a routine object
    print(f"recieved data {result} ")


# main is a coroutine object
print(type(main()))

# run the main coroutine, starts event loop
asyncio.run(main())