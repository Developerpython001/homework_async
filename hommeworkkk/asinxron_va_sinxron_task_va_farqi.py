import asyncio
import time
import datetime

async def async_task(num):
    print(f"Async task {num} bowlandi")
    await asyncio.sleep(1)
    print(f"Async task {num} yakunlandi")

def sync_task(num):
    print(f"Sync task {num} bowlandi")
    time.sleep(1)
    print(f"Sync task {num} yakunlandi")

async def main():
    start_time = datetime.datetime.now()

    async_tasks = [asyncio.create_task(async_task(i)) for i in range(1, 9)]
#as task ^

    sync_tasks = [sync_task(i) for i in range(1, 9)]
#s task ^

    await asyncio.gather(*async_tasks)

    for task in sync_tasks:
        task

    end_time = datetime.datetime.now()
    duration = end_time - start_time
    print(f"Barcha tasklar yakunlandi. Iw vaqt: {duration.total_seconds()} s")

asyncio.run(main())
