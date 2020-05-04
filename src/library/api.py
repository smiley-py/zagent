# -*- coding: utf-8 -*-
import json
import requests


class CustomApi():
    def __init__(self, ID, APIURL, USERNAME, PASSWORD):
        self.id = ID
        self.url = APIURL
        self.username = USERNAME
        self.password = PASSWORD
        self.token = ''
        self.is_login = 0
        self.msg = ''
        self.agent = None

    def login(self):
        self.__api_login()

    def logout(self):
        self.is_login = 0
        self.token = ''
        self.msg = 'Good Bye..!!!'

    def get_agent(self):
        self.__api_get_agent()

    def set_agent(self):
        self.__api_set_agent()

    def __api_login(self):
        result = ""

        try:
            session = requests.Session()
            headers = {
                "content-type": "application/json"
            }
            values = {
                "username": self.username,
                "password": self.password
            }
            response = session.post(
                url=self.url + 'rest-auth/login/',
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

    def __api_get_agent(self):
        result = ""

        try:
            session = requests.Session()
            head = {
                "content-type": "application/json",
                "Authorization": "Token " + self.token
            }
            response = session.get(
                url=self.url + 'agents/' + self.id,
                headers=head
            )
            session.close()
            try:
                result = json.loads(response.content)
                self.is_login = 1
                self.msg = "You get agent information"
                self.agent = result

            except KeyError as e:
                self.msg = "Some parameters is invalid."

        except requests.exceptions.HTTPError as errh:
            self.msg = "Http Error: " + str(errh)
        except requests.exceptions.ConnectionError as errc:
            self.msg = "Error Connecting: " + str(errc)
        except requests.exceptions.Timeout as errt:
            self.msg = "Timeout Error: " + str(errt)
        except requests.exceptions.RequestException as err:
            self.msg = "OOps: Something Else " + str(err)

    def __api_set_agent(self):
        result = ""

        try:
            session = requests.Session()
            head = {
                "content-type": "application/json",
                "Authorization": "Token " + self.token
            }
            values = {
                "name": self.agent["name"],
                "description": self.agent["description"],
                "path": self.agent["path"],
                "script_content": self.agent["script_content"],
                "script_inputs": self.agent["script_inputs"],
                "delay": self.agent["delay"],
                "output": self.agent["output"],
                "result": self.agent["result"],
                "start_time": self.agent["start_time"],
                "is_scheduled": self.agent["is_scheduled"],
                "is_deleted": self.agent["is_deleted"]
            }
            response = session.put(
                url=self.url + 'agents/' + self.id + '/update/',
                json=values,
                headers=head
            )
            session.close()
            try:
                result = json.loads(response.content)
                self.is_login = 1
                self.msg = "You set agent information"

            except KeyError as e:
                self.msg = "Some parameters is invalid."

        except requests.exceptions.HTTPError as errh:
            self.msg = "Http Error: " + str(errh)
        except requests.exceptions.ConnectionError as errc:
            self.msg = "Error Connecting: " + str(errc)
        except requests.exceptions.Timeout as errt:
            self.msg = "Timeout Error: " + str(errt)
        except requests.exceptions.RequestException as err:
            self.msg = "OOps: Something Else " + str(err)
