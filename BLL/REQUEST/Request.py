from CREDENTIALS.User_Agents import User_Agents
import requests
from typing import List, NoReturn
import random
from time import sleep
from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError


class Request:

    __User_Agents: List[str]
    __data: str

    def __init__(self):
        self.__set_user_agents()

    def __set_user_agents(self) -> NoReturn:
        self.__User_Agents = User_Agents
        print("User Agents Setted ")

    def scrap(self, url: str) -> str:

        headers: dict = {"User-Agent": random.choice(self.__User_Agents)}
        sleep(0.25)
        try:
            response = requests.get(url=url, headers=headers,timeout=(10,10))
        except ReadTimeout:
            sleep(7)
            return self.scrap(url=url)
        except ConnectionError:
            sleep(7)
            return self.scrap(url=url)

        if response.status_code == 200:
            self.__data = response.content.decode('ascii')  # Decoded
            print("Data Scrapped")
            return self.__data

        elif response.status_code == 429:
            print("To Many Requests")
            sleep(7)
            self.scrap(url=url)

        elif response.status_code == 404:
            sleep(7)
            self.scrap(url=url)

        elif response.status_code == 403:
            raise Exception(f"Forbidden  {response.status_code} {url}")

        else:
            raise Exception(f"Forbidden  {response.status_code} {url}")


