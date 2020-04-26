# -*- coding: utf-8 -*-
import json
import requests


class CustomApi():
    def __init__(self):
        self.token = ''
        self.is_login = 0
        self.msg = ''

    def login(self, url, username, password):
        self.api_login(url, username, password)

    def logout(self,):
        self.is_login = 0
        self.token = ''
        self.msg = 'Good Bye..!!!'

    def api_login(self, url, username, password):
        result = ""

        try:
            session = requests.Session()
            headers = {
                "content-type": "application/json"
            }
            values = {
                "username": username,
                "password": password
            }
            response = session.post(
                url=url,
                data=values
            )
            session.close()
            try:
                result = json.loads(response.content)
                self.is_login = 1
                self.msg = "Welcome !!!"
                self.token = result["key"]
            except KeyError as e:
                self.is_login = 0
                self.msg = "Username or password is invalid."

        except requests.exceptions.HTTPError as errh:
            self.msg = "Http Error: " + str(errh)
        except requests.exceptions.ConnectionError as errc:
            self.msg = "Error Connecting: " + str(errc)
        except requests.exceptions.Timeout as errt:
            self.msg = "Timeout Error: " + str(errt)
        except requests.exceptions.RequestException as err:
            self.msg = "OOps: Something Else " + str(err)
