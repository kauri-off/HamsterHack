import time

import requests

from models import *


class Endpoints:
    API = "https://api.hamsterkombatgame.io"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    def __init__(self, token: str) -> None:
        self.token = token
        self.headers = Endpoints.HEADERS.copy()
        self.headers["Authorization"] = self.token

    def account_info(self) -> AccountInfo:
        url = f"{Endpoints.API}/auth/account-info"

        res = requests.post(url=url, headers=self.headers).json()
        return AccountInfo(**res.get("accountInfo"))

    def sync(self) -> ClickerUser:
        url = f"{Endpoints.API}/clicker/sync"

        res = requests.post(url=url, headers=self.headers).json()
        return ClickerUser(**res.get("clickerUser"))

    def config(self) -> requests.Response:
        url = f"{Endpoints.API}/clicker/config"

        return requests.post(url=url, headers=self.headers)

    def upgrades_for_buy(self) -> requests.Response:
        url = f"{Endpoints.API}/clicker/upgrades-for-buy"

        return requests.post(url=url, headers=self.headers)

    def list_tasks(self) -> requests.Response:
        url = f"{Endpoints.API}/clicker/list-tasks"

        return requests.post(url=url, headers=self.headers)

    def list_airdrop_tasks(self) -> requests.Response:
        url = f"{Endpoints.API}/clicker/list-airdrop-tasks"

        return requests.post(url=url, headers=self.headers)

    def ip(self) -> requests.Response:
        url = f"{Endpoints.API}/ip"

        return requests.post(url=url, headers=self.headers)

    def tap(self, info: ClickerUser, count) -> ClickerUser:
        url = f"{Endpoints.API}/clicker/tap"
        headers = self.headers.copy()
        headers["Accept"] = "application/json"

        body = {
            "availableTaps": info.availableTaps,
            "count": count,
            "timestamp": round(time.time())
        }

        res = requests.post(url=url, headers=headers, json=body).json()
        return ClickerUser(**res.get("clickerUser"))

    def boosts_for_buy(self) -> BoostsForBuy:
        url = f"{Endpoints.API}/clicker/boosts-for-buy"

        res = requests.post(url=url, headers=self.headers).json()
        return BoostsForBuy(**res)

    def apply_boost(self, boost: Boost) -> ClickerUser:
        url = f"{Endpoints.API}/clicker/buy-boost"
        headers = self.headers.copy()
        headers["Accept"] = "application/json"

        body = {
            "boostId": boost.id,
            "timestamp": round(time.time())
        }


        res = requests.post(url=url, headers=headers, json=body).json()
        return ClickerUser(**res.get("clickerUser"))

    @staticmethod
    def auth_by_telegram(init_data: str) -> str:
        url = f"{Endpoints.API}/auth/auth-by-telegram-webapp"

        headers = Endpoints.HEADERS.copy()
        headers["Accept"] = "application/json"

        body = {
            "initDataRaw": init_data
        }

        res = requests.post(url=url, headers=headers, json=body).json()
        return res.get("authToken")
