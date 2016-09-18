#!/bin/python

import time
from utils import debug
from core import inputEvent

class inputManager():
    def __init__(self):
        pass
    def initialize(self, environment):
        environment['runtime']['settingsManager'].loadDriver(environment,\
          environment['runtime']['settingsManager'].getSetting(environment,'keyboard', 'driver'), 'inputDriver')     
        #self.grabDevices(environment)

    def shutdown(self, environment):
        environment['runtime']['inputManager'].releaseDevices(environment)    
        if environment['runtime']['inputDriver']:
            environment['runtime']['inputDriver'].shutdown(environment)
    
    def proceedInputEvent(self, environment):

        timeout = True    	
        event = environment['runtime']['inputDriver'].getInput(environment)
        mEvent = environment['runtime']['inputDriver'].mapEvent(environment, event)
        if mEvent and event:
            if mEvent['EventValue'] == 0:
                return True  
            timeout = False
            if mEvent['EventState'] == 0:
                if self.isFenrirKey(environment, mEvent):
                    environment['input']['currInput'].remove('KEY_FENRIR')
                elif mEvent['EventName'] in ['KEY_RIGHTCTRL','KEY_LEFTCTRL'] :
                    environment['input']['currInput'].remove('KEY_CTRL')
                elif mEvent['EventName'] in ['KEY_RIGHTSHIFT','KEY_LEFTSHIFT'] :
                    environment['input']['currInput'].remove('KEY_SHIFT')                
                else:
                    environment['input']['currInput'].remove(mEvent['EventName'])
                environment['input']['currInput'] = sorted(environment['input']['currInput'])                    
            elif mEvent['EventState'] == 1:
                if self.isFenrirKey(environment, mEvent):
                    if not 'KEY_FENRIR' in environment['input']['currInput']:                
                       environment['input']['currInput'].append('KEY_FENRIR')
                elif mEvent['EventName'] in ['KEY_RIGHTCTRL','KEY_LEFTCTRL'] :
                    if not 'KEY_CTRL' in environment['input']['currInput']:
                        environment['input']['currInput'].append('KEY_CTRL')
                elif mEvent['EventName'] in ['KEY_RIGHTSHIFT','KEY_LEFTSHIFT'] :
                    if not 'KEY_SHIFT' in environment['input']['currInput']:                
                        environment['input']['currInput'].append('KEY_SHIFT')                       
                else:
                    if not mEvent['EventName'] in environment['input']['currInput']:                                
                        environment['input']['currInput'].append(mEvent['EventName'])            
                environment['input']['currInput'] = sorted(environment['input']['currInput'])
            elif mEvent['EventState'] == 2:
                pass
            else:
                pass  
            environment['input']['oldNumLock'] = environment['input']['newNumLock']
            environment['input']['newNumLock'] = environment['runtime']['inputDriver'].getNumlock(environment) 
            environment['input']['oldCapsLock'] = environment['input']['newCapsLock'] 
            environment['input']['newCapsLock'] = environment['runtime']['inputDriver'].getCapslock(environment)       
            environment['input']['oldScrollLock'] = environment['input']['newScrollLock'] 
            environment['input']['newScrollLock'] = environment['runtime']['inputDriver'].getScrollLock(environment)                     
            environment['input']['lastInputTime'] = time.time()
            environment['input']['shortcutRepeat'] = 1
        return timeout
    
    def grabDevices(self, environment):
        if environment['runtime']['settingsManager'].getSettingAsBool(environment, 'keyboard', 'grabDevices'):
            environment['runtime']['inputDriver'].grabDevices(environment)

    def releaseDevices(self, environment):
        environment['runtime']['inputDriver'].releaseDevices()
        
    def isConsumeInput(self, environment):
	    return environment['input']['consumeKey'] and \
          not environment['input']['keyForeward'] or \
          not environment['runtime']['settingsManager'].getSettingAsBool(environment, 'keyboard', 'grabDevices')
          
    def passInput(self, environment):
        try:
            environment['runtime']['inputDriver']
        except Exception as e:
            environment['runtime']['debug'].writeDebugOut(environment,"Error while writeUInput",debug.debugLevel.ERROR)
            environment['runtime']['debug'].writeDebugOut(environment, str(e),debug.debugLevel.ERROR)    

    def getPrevDeepestInput(self, environment):
        shortcut = []
        shortcut.append(environment['input']['shortcutRepeat'])
        shortcut.append(sorted(environment['input']['prevDeepestInput']))

    def getPrevShortcut(self, environment):
        shortcut = []
        shortcut.append(environment['input']['shortcutRepeat'])
        shortcut.append(sorted(environment['input']['prevInput']))
        return str(shortcut)

    def getCurrShortcut(self, environment):
        shortcut = []
        shortcut.append(environment['input']['shortcutRepeat'])
        shortcut.append(sorted(environment['input']['currInput']))
        return str(shortcut)
        
    def isFenrirKey(self,environment, mEvent):
        return str(mEvent['EventName']) in environment['input']['fenrirKey']

    def getCommandForShortcut(self, environment, shortcut):
        shortcut = shortcut.upper()
        if not self.shortcutExists(environment, shortcut):
            return '' 
        return environment['bindings'][shortcut].upper()

    def shortcutExists(self, environment, shortcut):
        return( str(shortcut).upper() in environment['bindings'])
        
