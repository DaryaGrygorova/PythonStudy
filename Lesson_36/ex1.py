import asyncio


async def some_work():
    print('starting some work')
    await asyncio.sleep(2)
    print('completed some work')
    return {1: 'some data'}

async def second_coroutine():
    for step in range(3):
        print(f"second coroutine step {step}")
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(some_work())
    task2 = asyncio.create_task(second_coroutine())
    data_task1 = await task1
    await task2
    print('data from task1: ', data_task1)
    both_coroutines = asyncio.gather(some_work(), second_coroutine())
    # both_coroutines - future (promise) - after completed - list of results of gathered function

    print('results of both_coroutines: ', await both_coroutines)
    print('main completed')


print('start program')
# loop = asyncio.new_event_loop()
# loop.create_task(some_work())
# loop.create_task(second_coroutine())


asyncio.run(main())

print('completed program')
