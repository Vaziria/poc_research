import asyncio
from uuid import uuid4

import httpx
import os

from anti_crawler import HeadAf


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from webdriver_manager.chrome import ChromeDriverManager

from main import start_fix_proxy

    
def create_driver(profile_path = './crawler_data/'):
    
    service = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("start-maximized")


    options.add_argument("--disable-extensions")
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-features=ChromeWhatsNewUI")
    options.add_argument('--proxy-server=http://localhost:8881')


    profile_path = os.path.abspath(profile_path)
    options.add_argument(f"user-data-dir={profile_path}")
        
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"
    


    driver = webdriver.Chrome(service=service, options=options, desired_capabilities=caps)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.implicitly_wait(30)
    
    return driver


async def get_product(driver):
    head = HeadAf()
    
    af_ac_enc = head.create_af_ac_enc()
    
    client = httpx.AsyncClient(http2=True)
    
    viewid = str(uuid4())
    
    url = f'https://shopee.co.id/api/v4/search/search_items?by=relevancy&keyword=sapu&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2&view_session_id={viewid}'
    
    
    
    
    api_protection = get_api_protection(driver, url)
    command = 'return window.test_entry_2(300, 1)'
    af_ac = driver.execute_script(command)
    print(af_ac)
    
    
    
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en',
        'af-ac-enc-dat': af_ac[0],
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'pragma': 'no-cache',
        'referer': 'https://shopee.co.id/search?keyword=sapu%20tangan%20bayi&trackingId=searchhint-1671689722-046aa738-81c0-11ed-82f5-f4ee081907e2',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-api-source': 'pc',
        'x-requested-with': 'XMLHttpRequest'
    }
    
    headers.update(api_protection)
    
    print(headers)
    
    all_cookies = driver.get_cookies()
    cookies = {}
    for cookie in all_cookies:
        cookies[cookie['name']] = cookie['value']
    
    res = await client.get(url, headers=headers, cookies=cookies)
    
    print(res.text)
    
    
def get_api_protection(driver, url: str):
    # by=relevancy&keyword=gamis&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2&view_session_id=8f9ba85b-58d0-4422-bdfb-4c9dc09bf035 0 2 true
    
    url = url.split('?')[-1]
    print(url)
    
    command = f"return window.test_get_api_protection('{url}', 0, 2, true)"
    print(command)
    
    hasil = driver.execute_script(command)
    
    print(hasil)
    
    return hasil
    
async def main():
    print("sasdasdas")
    
    task = asyncio.create_task(start_fix_proxy('localhost', 8881))
    
    driver = create_driver()
    driver.get('https://shopee.co.id/search?keyword=gamis')
    
    await asyncio.sleep(5)
    
    
    command = """
        window.get_prod = function(url){


            t = {
                "antiFraudConfig": {
                    "antiCrawler": {
                        "appKey": "Search.PC",
                        "shouldReplaceHistory": true,
                        "redirectType": "1"
                    },
                    "deviceFingerPrint": {},
                    "apiProtection": {}
                }
            };


            return window.rekuest.get(url, t);
        }
        
        
        """
        
    data = driver.execute_script(command)
    loop = asyncio.get_event_loop()
    
    coros = []
    
    async def get_pp(c):
        try:
        
            data = await asyncio.wait_for(loop.run_in_executor(None, driver.execute_script, command), 100)

        except asyncio.exceptions.TimeoutError as e:
            print('timeout')
            
            return await get_pp(c)
            
        print(c, type(data))
    
    for c in range(0, 1000):
        idnya = str(uuid4())
        command = f'return await window.get_prod("/api/v4/search/search_items?by=relevancy&keyword=gamis&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2&view_session_id={idnya}");'
        
        coro = get_pp(c)
        
        coros.append(coro)
        
    
    
    await asyncio.gather(*coros)
    
    task.cancel()
    
    
    
    
if __name__ == '__main__':
    
    loop = asyncio.get_event_loop()
    
    loop.run_until_complete(main())