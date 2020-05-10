# -*- coding: utf-8 -*-
import json


class CustomMenu():

    def get_help_text(self):
        menu = []

        menu.append(
            '---------------------------------------------------------\n')

        menu.append("*** Z Agent Shell Help Menu ***\n")

        menu.append('exit \t\t close the system')
        menu.append('start \t\t start the scheduled service')
        menu.append('stop \t\t stop the scheduled service')
        menu.append('restart \t restart the scheduled service')

        menu.append(
            '\n---------------------------------------------------------')

        return menu
