import asyncio
import requests

async def main():
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None,
            requests.get,
            i
        )
        for i in ['http://google.com/','http://yahoo.com/']
    ]
    for response in await asyncio.gather(*futures):
        print(response)
        pass

'''
async def main():
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None,
            requests.get,
            'http://google.com/'
        )
        for i in range(20)
    ]
    for response in await asyncio.gather(*futures):
        pass
'''

loop = asyncio.get_event_loop()
loop.run_until_complete(main())