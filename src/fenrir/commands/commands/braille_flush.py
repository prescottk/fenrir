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
        return _('flush the braille device if a message is written on')
    def run(self):
        self.env['runtime']['outputManager'].clearFlushTime()
    def setCallback(self, callback):
        pass
