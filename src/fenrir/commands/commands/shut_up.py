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
        return _('interrupts the current presentation')        
    def run(self):
        if len(self.env['input']['prevDeepestInput']) > len(self.env['input']['currInput']):
            return          
        self.env['runtime']['outputManager'].interruptOutput()
    def setCallback(self, callback):
        pass
