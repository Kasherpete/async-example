import asyncio
import random


async def task():
    print("   mark1")
    await asyncio.sleep(2)
    print("   mark2")


async def main():
    while True:
        r = random.randint(1, 10)  # check for new messages in real world uses
        if r == 1:
            asyncio.create_task(task())

        await asyncio.sleep(.5)
        print("check")


asyncio.run(main())
