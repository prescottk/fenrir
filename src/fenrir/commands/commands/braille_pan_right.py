#!/bin/python
# -*- coding: utf-8 -*-

# Fenrir TTY screen reader
# By Chrys, Storm Dragon, and contributers.

from core import debug

class command():
    def __init__(self):
        pass
    def initialize(self, environment):
        self.env = environment
    def shutdown(self):
        pass
    def getDescription(self):
        return 'Move braille view to the right.'         
    def run(self):
        panned = self.env['runtime']['outputManager'].setPanRight()
    def setCallback(self, callback):
        pass
