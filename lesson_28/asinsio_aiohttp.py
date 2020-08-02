import asyncio
from aiohttp_requests import requests
import time
import json
import typing


url = f'https://api.pushshift.io/reddit/search/comment'


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
    t1 = time.time()
    resp = await requests.get(url, params=data_params)
    data = await resp.json()
    i = 0
    for item in data['data']:
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
    """ Returns a list of users """
    user_data = []
    resp = await requests.get(url)
    data = await resp.json()
    for item in data['data']:
        user_data.append(item['author'])
    return user_data

event_loop = asyncio.get_event_loop()

try:
    users_name = event_loop.run_until_complete(event_loop.create_task(user_list(url)))
    for item in users_name:
        event_loop.run_until_complete(event_loop.create_task(user_more(url, item)))
finally:
    event_loop.close()