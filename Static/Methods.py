import os
try:
    import requests,webbrowser,tempfile
    from colorama import Fore,Style
    from Static.Values import StaticValues
    import re,urllib,json
    from bs4 import BeautifulSoup
    from jsonpath_ng import parse
except:
    os.system(f"pip install -r requirements.txt")
class StaticMethods:
    @staticmethod
    def get_proxies():
        with open('proxies.txt', 'w') as f:
            pass

        response = requests.get('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies')
        
        if response.status_code == 200:
            with open('proxies.txt', 'a') as f:
                proxies = response.text.strip().split('\n')
                for proxy in proxies:
                    f.write(proxy.strip() + '\n')
        else:
            return
        return 1
    @staticmethod
    def  is_first_run():
        """Check if it's the first run of the program"""
        file_path = os.path.join(tempfile.gettempdir(), 'TtkReporter.txt')
        if not os.path.isfile(file_path):
            with open(file_path, "w") as file:
                file.write("Don't Worry, this isn't a virus, just a check to see if it's your first time. :)")
            print(f"{StaticValues.INFO}First Time Detected. Welcome! (This won't appear anymore){Style.RESET_ALL}")
            webbrowser.open("https://discord.gg/nAa5PyxubF")

    @staticmethod
    def show_credits():
        """Display program credits"""
        print(f"{StaticValues.INFO}{Fore.BLUE}Provided to you by {Fore.CYAN}Sneezedip.{Style.RESET_ALL}")
        print(f"{StaticValues.INFO}{Fore.BLUE}Join Our Discord For More Tools! {Fore.GREEN}"
            f"https://discord.gg/nAa5PyxubF{Style.RESET_ALL}")
    @staticmethod   
    def get_match(match,url):
        format = re.search(rf'{match}', url)
        if format:
            format_x = format.group(1)
            return urllib.parse.unquote(format_x)
    @staticmethod
    def _solve_name(user):
        if "https" in user and "@" in user:
            return user
        elif not "https" in user and "@" in user:
            return f"https://www.tiktok.com/{user}"
        elif not "https" in user and not "@" in user:
            return f"https://www.tiktok.com/@{user}"
    @staticmethod
    def get_userID(user):
        from bs4 import BeautifulSoup
        import json
        response = requests.get(StaticMethods._solve_name(user))
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            script_tag = soup.find("script", {"id": "__UNIVERSAL_DATA_FOR_REHYDRATION__"})
            if script_tag:
                data = json.loads(script_tag.string)
                try:
                    return data["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"]["id"]
                except KeyError:
                    return "Invalid Profile. Check Username/Url"
            else:
                raise Exception("No JSON Found.")
        else:
            raise Exception("Internal Error")
    @staticmethod
    def get_userData(user,infotype):
        from bs4 import BeautifulSoup
        import json
        response = requests.get(StaticMethods._solve_name(user))
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            script_tag = soup.find("script", {"id": "__UNIVERSAL_DATA_FOR_REHYDRATION__"})
            if script_tag:
                data = json.loads(script_tag.string)
                try:
                    return data["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"][infotype]
                except KeyError:
                    return "Invalid Profile. Check Username/Url"
            else:
                raise Exception("No JSON Found.")
        else:
            raise Exception("Internal Error")

    
    