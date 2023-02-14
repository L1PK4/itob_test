import asyncio
from kettle import Kettle



kettle = Kettle()

async def log(kettle: Kettle):
    while True:
        print(kettle)
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(log(kettle), kettle.start())

if __name__ == "__main__":
    asyncio.run(main())
