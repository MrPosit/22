''') Загрузите массив json – объектов с сайта jsonplaceholder, используя библиотеку 
requests.
б) Сохраните циклом каждый в отдельный файл, в одну новую папку.
а) Загрузите массив json – объектов с сайта jsonplaceholder, используя библиотеку 
aiohttp.
б) Сохраните циклом каждый в отдельный файл, в одну новую папку.
'''

import os
import aiohttp
import asyncio
import json

os.makedirs("json_files", exist_ok=True)

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def save_json(index, obj):
    with open(f"json_files/{index}.json", "w") as file:
        json.dump(obj, file)

async def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = await fetch_json(url)
    
    tasks = []
    for index, obj in enumerate(data):
        task = save_json(index, obj)
        tasks.append(task)
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())