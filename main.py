"""
task1

import requests

url = "http://104.197.100.132:5000"

levels = ["/level1", "/level2", "/level3", "/level6"]

for level in levels:
    response = requests.get(url + level)
    print(f"Response for {level}: {response.text}")
"""


"""
task2  first temp

import requests

url = "http://104.197.100.132:5000/level2"
params = {'start': 0, 'end': 10}
response = requests.get(url, params=params)
print(response.text)
"""

"""
import aiohttp
import asyncio


async def fetch_data(start, end):
    url = "http://104.197.100.132:5000/level2"
    params = {'start': start, 'end': end}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            return await response.text()


async def main():
    tasks = []
    for i in range(0, 100, 10):  # تقسيم الطلبات إلى دفعات من 10
        tasks.append(fetch_data(i, i + 10))

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)


# تشغيل المهام غير المتزامنة
asyncio.run(main())
"""

"""

import aiohttp
import asyncio
import json


async def fetch_data(start, end):
    url = "http://104.197.100.132:5000/level2"
    params = {'start': start, 'end': end}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.text()
            # تحليل البيانات هنا
            json_data = json.loads(data)
            for entry in json_data:
                if 'flag' in entry:
                    print(f"Flag found: {entry['flag']}")
            return data


async def main():
    tasks = []
    for i in range(525000, 525100, 100):  # تعديل النطاق حسب الحاجة
        tasks.append(fetch_data(i, i + 10))

    results = await asyncio.gather(*tasks)


# تشغيل المهام غير المتزامنة
asyncio.run(main())
"""

"""

import aiohttp
import asyncio
import json


async def fetch_data(start, end):
    url = "http://104.197.100.132:5000/level2"
    params = {'start': start, 'end': end}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.text()
            # تحويل البيانات إلى JSON
            json_data = json.loads(data)

            # البحث عن الفلاج
            for entry in json_data:
                if 'flag' in entry:
                    print(f"Flag found: {entry['flag']}")
                    print(f"ID: {entry['id']}")
                    return True  # وجد الفلاج، إنهاء الحلقة

            return False  # لم يتم العثور على الفلاج


async def main():
    start = 0
    end = 500

    # حلقة لا نهائية تستمر حتى يتم العثور على الفلاج
    while True:
        print(f"Fetching data from range {start} to {end}")
        flag_found = await fetch_data(start, end)
        if flag_found:
            break  # إنهاء الحلقة عند العثور على الفلاج
        start += 500  # جلب الدفعة التالية
        end += 500


# تشغيل المهام غير المتزامنة
asyncio.ru
"""

"""
import aiohttp
import asyncio
import json
from dotenv import load_dotenv
import os

# تحميل متغيرات البيئة من الملف .env
load_dotenv()

# قراءة متغيرات البيئة
env = os.getenv("ENV")
endpoint_url = os.getenv("ENDPOINT_URL")  # تم استخدام الرابط من ملف .env

print(f"Current environment: {env}")
print(f"Endpoint URL: {endpoint_url}")


async def fetch_data(session, start, end):
    # استخدام URL الخاص بالـ API من المتغير البيئي
    params = {'start': start, 'end': end}

    async with session.get(endpoint_url, params=params) as response:
        data = await response.text()

        if not data:
            print(f"No data received for range {start} - {end}")
            return False

        try:
            json_data = json.loads(data)
        except json.JSONDecodeError:
            print(f"Failed to decode JSON for range {start} - {end}")
            return False

        for entry in json_data:
            if 'flag' in entry:
                print(f"Flag found: {entry['flag']}")
                print(f"ID: {entry['id']}")
                return True
        return False


async def main():
    increment = 500
    tasks = []

    async with aiohttp.ClientSession() as session:
        start = 0
        while True:
            print(f"Fetching data in ranges starting from {start}")
            tasks = [fetch_data(session, i, i + increment) for i in range(start, start + increment * 10, increment)]

            results = await asyncio.gather(*tasks)

            if any(results):
                break

            start += increment * 10


# بدء البرنامج
asyncio.run(main())

"""
import aiohttp
import asyncio
import json
from env import logger, endpoint_url

async def fetch_data(session, start, end):
    params = {'start': start, 'end': end}

    logger.debug(f"Fetching data from {start} to {end}")

    async with session.get(endpoint_url, params=params) as response:
        data = await response.text()
        json_data = json.loads(data)

        for entry in json_data:
            if 'flag' in entry:
                logger.info(f"Flag found: {entry['flag']}")
                logger.info(f"ID: {entry['id']}")
                return True
        return False

async def main():
    increment = 500
    tasks = []

    async with aiohttp.ClientSession() as session:
        start = 0
        while True:
            logger.debug(f"Fetching data in ranges starting from {start}")
            tasks = [fetch_data(session, i, i + increment) for i in range(start, start + increment * 10, increment)]

            results = await asyncio.gather(*tasks)

            if any(results):
                break

            start += increment * 10

asyncio.run(main())
