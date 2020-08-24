import asyncio
from aiohttp_requests import requests
import time
import json


url = f'https://stock-and-options-trading-data-provider.p.rapidapi.com/options/'


async def user_more(url: str, user_name: str) -> list:
    """ Writes comments to a file by user """
    try:
        check_file = open('pushshift.json', 'r')
        check_file.close()
    except Exception:
        check_file = open('pushshift.json', 'w')
        check_file.close()
    data_text = []
    data_user = {}
    all_data = []
    data_params = {'author': user_name}
    headers = {
        'x-rapidapi-host': "stock-and-options-trading-data-provider.p.rapidapi.com",
        'x-rapidapi-key': "4a42178342msh176c04807e3bf72p1da7c0jsn8f657ad00a8b",
        'x-rapidapi-proxy-secret': "a755b180-f5a9-11e9-9f69-7bf51e845926"
    }
    t1 = time.time()
    resp = await requests.get(url, heades=headers)
    print(resp)
    data = await resp.json()
    print(data['stock']['longBusinessSummary'])
    i = 0
    for item in data:
        i += 1
        data_text.append(f"{i}: {item['body']}")
    data_user[f'{user_name}'] = data_text
    all_data.append(data_user)
    try:
        with open('pushshift.json', 'a') as my_file:
            json.dump(all_data, my_file, indent=4)
    except Exception as e:
        print(e)
    print(f'time: {time.time() - t1}')
    return data


async def user_list(url: str) -> list:
    """ Returns a list of users and start Writes comments to a file by user"""
    headers = {
        'x-rapidapi-host': "stock-and-options-trading-data-provider.p.rapidapi.com",
        'x-rapidapi-key': "4a42178342msh176c04807e3bf72p1da7c0jsn8f657ad00a8b",
        'x-rapidapi-proxy-secret': "a755b180-f5a9-11e9-9f69-7bf51e845926"
    }
    user_data = []
    resp = await requests.get(url, headers=headers)
    print(resp)
    data = await resp.json()
    print(data)
    for item in data:
        print(item)
    return user_data


async def main():
    t1 = time.time()
    await asyncio.gather(user_list(url))
    print(f'all time: {time.time() - t1}')

asyncio.run(main())

