import asyncio


class AsyncSamples:

    def __init__(self):
        self.asyncio = asyncio

    async def print_message(self, message, delay):
        await asyncio.sleep(delay)
        print(message)

    async def gather_runs(self):
        await asyncio.gather(
            self.print_message("First", 1),
            self.print_message("Second", 2),
            self.print_message("Third", 3)
        )

"""
import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)
        item = f"item-{i}"
        await queue.put(item)
        print(f"Produced {item}")

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    producers = [asyncio.create_task(producer(queue))]
    consumers = [asyncio.create_task(consumer(queue))]

    await asyncio.gather(*producers)
    await queue.put(None)  # Signal the consumer to exit
    await asyncio.gather(*consumers)

asyncio.run(main())
"""