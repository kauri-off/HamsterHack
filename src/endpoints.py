import requests
from models import *
import time

class Endpoints:
    API = "https://api.hamsterkombatgame.io"
    def __init__(self, token: str) -> None:
        self.token = token

    def account_info(self) -> requests.Response:
        url = f"{Endpoints.API}/auth/account-info"
        headers = {
            "Authorization": self.token,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        return requests.post(url=url, headers=headers)

    def sync(self) -> ClickerUser:
        url = f"{Endpoints.API}/clicker/sync"

        headers = {
            "Authorization": self.token,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        res = requests.post(url=url, headers=headers).json()
        return ClickerUser(**res.get("clickerUser"))

    def config(self) -> requests.Response:
        url = f"{Endpoints.API}/clicker/config"
        headers = {
            "Authorization": self.token,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        return requests.post(url=url, headers=headers)

    def upgrades_for_buy(self) -> requests.Response:
        url = f"{Endpoints.API}/clicker/upgrades-for-buy"
        headers = {
            "Authorization": self.token,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        return requests.post(url=url, headers=headers)

    def list_tasks(self) -> requests.Response:
        url = f"{Endpoints.API}/clicker/list-tasks"
        headers = {
            "Authorization": self.token,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        return requests.post(url=url, headers=headers)

    def list_airdrop_tasks(self) -> requests.Response:
        url = f"{Endpoints.API}/clicker/list-airdrop-tasks"
        headers = {
            "Authorization": self.token,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        return requests.post(url=url, headers=headers)

    def ip(self) -> requests.Response:
        url = f"{Endpoints.API}/ip"
        headers = {
            "Authorization": self.token,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        return requests.post(url=url, headers=headers)

    def tap(self, info: ClickerUser, count) -> requests.Response:
        url = f"{Endpoints.API}/clicker/tap"
        headers = {
            "Accept": "application/json",
            "Authorization": self.token,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        }

        body = {
            "availableTaps": info.availableTaps,
            "count": count,
            "timestamp": round(time.time())
        }

        return requests.post(url=url, headers=headers, json=body)
