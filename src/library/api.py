# -*- coding: utf-8 -*-
import json
import requests


class CustomApi():
    def __init__(self, ID, APIURL, USERNAME, PASSWORD):
        self.url = APIURL
        self.username = USERNAME
        self.password = PASSWORD
        self.token = ''
        self.is_login = 0
        self.msg = ''

        self.id = ID
        self.name = ''
        self.description = ''
        self.path = ''
        self.script_content = ''
        self.input_string = ''
        self.delay = ''
        self.output = ''
        self.result = ''
        self.start_time = ''
        self.is_scheduled = 0
        self.is_deleted = 0

    def login(self):
        self.api_login()

    def logout(self):
        self.is_login = 0
        self.token = ''
        self.msg = 'Good Bye..!!!'

    def get_agent(self):
        self.api_get_agent()

    def set_agent(self):
        self.api_set_agent()

    def api_login(self):
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

    def api_get_agent(self):
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

                self.name = result["name"]
                self.description = result["description"]
                self.path = result["path"]
                self.script_content = result["script_content"]
                self.script_inputs = result["script_inputs"]
                self.delay = result["delay"]
                self.output = result["output"]
                self.result = result["result"]
                self.start_time = result["start_time"]
                self.is_scheduled = result["is_scheduled"]
                self.is_deleted = result["is_deleted"]

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

    def api_set_agent(self):
        result = ""

        try:
            session = requests.Session()
            head = {
                "content-type": "application/json",
                "Authorization": "Token " + self.token
            }
            values = {
                "name": self.name,
                "description": self.description,
                "path": self.path,
                "script_content": self.script_content,
                "input_string": self.input_string,
                "delay": self.delay,
                "output": self.output,
                "result": self.result,
                "start_time": self.start_time,
                "is_scheduled": self.is_scheduled,
                "is_deleted": self.is_deleted
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
