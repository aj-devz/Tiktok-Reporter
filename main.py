import asyncio
import os
import sys
import webbrowser
import time
import re
import concurrent.futures
import threading
import random
from datetime import datetime
try:
    from colorama import Style,Fore
    import tls_client
    import requests
    import configparser
    import random
    from fake_useragent import UserAgent
    from Static.Methods import StaticMethods
    from Static.Values import StaticValues
    from Handler.ErrorHandler import Handler
    import httpx
except:
    print("Installing Libraries...")
    os.system("pip install -r requirements.txt")
    os.system("python3 main.py")

class Program:
    def _getpayload(self):
        return {
            "WebIdLastTime" : datetime.now().timestamp(),
            "aid" : 1988,
            "app_language" : "en",
            "app_name" : "tiktok_web",
            "r_language": "en-US",
            "browser_name": "Mozilla",
            "browser_online": True,
            "browser_platform": "Win32",
            "browser_version": UserAgent().random,
            "channel": "tiktok_web",
            "cookie_enabled": True,
            "current_region": "PT",
            "data_collection_enabled": True,
            "device_id": random.randint(7000000000000000000,9999999999999999999),
            "device_platform": "web_pc",
            "focus_state": True,
            "from_page": "user",
            "history_len": 2,
            "is_fullscreen": False,
            "is_page_visible": True,
            "lang": "en",
            "nickname": self.victim_data["nickname"],
            "object_id": self.victim_data["id"],
            "odinId": random.randint(7000000000000000000,9999999999999999999),
            "os": "windows",
            "owner_id": self.victim_data["id"],
            "priority_region": "",
            "reason": self.report_type,
            "referer": "",
            "region": "PT",
            "report_type": "user",
            "screen_height": 1080,
            "screen_width": 1920,
            "secUid": self.victim_data["secUid"],
            "target": self.victim_data["id"],
            "tz_name": "Atlantic/Azores",
            "user_is_login": False,
            "webcast_language": "en",
            }
    def _clear(self):
        os.system("cls") if os.name == 'nt' else os.system("clear")

    def main(self):
        self._clear()
        while True:
            print(f"{StaticValues.WAITING}Enter the victim URL or @ ➤ ",end="")
            self.victim = input()
            self.victim = StaticMethods.get_userID(self.victim)
            if "Invalid" in self.victim:
                print(f"{StaticValues.WARNING} Invalid URL or @!")
            else:
                break
        self._clear()
        print(f"{StaticValues.SUCCESS}Valid User!")
        print(f"{StaticValues.WAITING}Gathering User Data..")
        self.victim_data = {
            "id" : StaticMethods.get_userData(self.victim,"id"),
            "nickname" : StaticMethods.get_userData(self.victim,"nickname"),
            "secUid" : StaticMethods.get_userData(self.victim,"secUid"),
        }
        print(f"{StaticValues.SUCCESS}Success!")
        self._clear()
        print(f"{StaticValues.WAITING}Select an Option to report the victim.")
        for key, value in StaticValues.REPORT_TYPES.items():
            print(f"{key}: {value[1]}")
        while True:
            self.report_type = Handler.integer_handler(f"{Fore.YELLOW}➤ {Fore.RESET}",1,15)
            if self.report_type in StaticValues.REPORT_TYPES:
                break
        self.payload = self._getpayload()
    def report(self):
        while True:
            session = tls_client.Session(
                    client_identifier="chrome_106"
                )
            response = session.get("https://www.tiktok.com/aweme/v2/aweme/feedback/", params=self.payload)
            
            StaticValues.TOTAL_REQUESTS += 1
            if "Thanks for your feedback" in response.text or response.status_code == 200:
                StaticValues.REPORT_COUNT += 1
                self._clear()
                print(f"{StaticValues.SUCCESS}{self.victim_data["nickname"]} Reported {StaticValues.REPORT_COUNT} Times! ({(StaticValues.REPORT_COUNT/StaticValues.TOTAL_REQUESTS)*100}% Success Rate)")
            else:  
                print(f"{StaticValues.WARNING}Error ({(StaticValues.REPORT_COUNT/StaticValues.TOTAL_REQUESTS)*100}% Success Rate)")
                StaticValues.COOLDOWN = True
                break
    
if __name__ == "__main__":
    threads = []
    StaticMethods.is_first_run()
    StaticMethods.show_credits()
    t_a = Handler.integer_handler(f"{StaticValues.WAITING}THREADS AMOUNT ➤ ")
    time.sleep(1)
    program = Program()
    program.main()
    for _ in range(t_a):
        t = threading.Thread(target=program.report())
        threads.append(t)
        t.start()
    for thread in threads:
        if not StaticValues.COOLDOWN:
            thread.join()
        else:
            print(f"{StaticValues.WAITING}Cooldown detected. Waiting 10 seconds..")
            time.sleep(10)
            StaticValues.COOLDOWN = False
    # asyncio.run(program.report())