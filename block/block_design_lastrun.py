#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.3),
    on Wed 31 Jan 2018 12:38:07 AM CST
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'block_design'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/media/Data/Documents/devel/PsychoPyExamples/block/block_design.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1366, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Welcome to the experiment!\n\nHere you will press with your\nright index finger everytime you\nsee a red square and your right middle \nfinger every time you see a blue square',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "scantrigger"
scantriggerClock = core.Clock()
scan_trigger_text = visual.TextStim(win=win, name='scan_trigger_text',
    text='Waiting for scan trigger...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "scannerwarmup"
scannerwarmupClock = core.Clock()
warmup_square = visual.Rect(
    win=win, name='warmup_square',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "pretrial"
pretrialClock = core.Clock()


# Initialize components for Routine "trial"
trialClock = core.Clock()
square = visual.Rect(
    win=win, name='square',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
iti_square = visual.Rect(
    win=win, name='iti_square',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "exit"
exitClock = core.Clock()
done = visual.TextStim(win=win, name='done',
    text='Thank you for participating!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
t = 0
welcomeClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
welcomeComponents = [text]
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "welcome"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = welcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "scantrigger"-------
t = 0
scantriggerClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
scan_trigger = event.BuilderKeyResponse()
# keep track of which components have finished
scantriggerComponents = [scan_trigger, scan_trigger_text]
for thisComponent in scantriggerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "scantrigger"-------
while continueRoutine:
    # get current time
    t = scantriggerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *scan_trigger* updates
    if t >= 0.0 and scan_trigger.status == NOT_STARTED:
        # keep track of start time/frame for later
        scan_trigger.tStart = t
        scan_trigger.frameNStart = frameN  # exact frame index
        scan_trigger.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if scan_trigger.status == STARTED:
        theseKeys = event.getKeys(keyList=['asciicircum'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *scan_trigger_text* updates
    if t >= 0.0 and scan_trigger_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        scan_trigger_text.tStart = t
        scan_trigger_text.frameNStart = frameN  # exact frame index
        scan_trigger_text.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in scantriggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "scantrigger"-------
for thisComponent in scantriggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "scantrigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "scannerwarmup"-------
t = 0
scannerwarmupClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
scannerwarmupComponents = [warmup_square]
for thisComponent in scannerwarmupComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "scannerwarmup"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = scannerwarmupClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *warmup_square* updates
    if t >= 0.0 and warmup_square.status == NOT_STARTED:
        # keep track of start time/frame for later
        warmup_square.tStart = t
        warmup_square.frameNStart = frameN  # exact frame index
        warmup_square.setAutoDraw(True)
    frameRemains = 0.0 + 6.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if warmup_square.status == STARTED and t >= frameRemains:
        warmup_square.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in scannerwarmupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "scannerwarmup"-------
for thisComponent in scannerwarmupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'block_rt.csv'),
    seed=1, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "pretrial"-------
    t = 0
    pretrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if stim is None or stim == "NULL":
        stim = 'white'
    # keep track of which components have finished
    pretrialComponents = []
    for thisComponent in pretrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pretrial"-------
    while continueRoutine:
        # get current time
        t = pretrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pretrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pretrial"-------
    for thisComponent in pretrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "pretrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    square.setFillColor(stim)
    square.setLineColor(stim)
    keyboard = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [square, keyboard, iti_square]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *square* updates
        if t >= 0.0 and square.status == NOT_STARTED:
            # keep track of start time/frame for later
            square.tStart = t
            square.frameNStart = frameN  # exact frame index
            square.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if square.status == STARTED and t >= frameRemains:
            square.setAutoDraw(False)
        
        # *keyboard* updates
        if t >= 0.0 and keyboard.status == NOT_STARTED:
            # keep track of start time/frame for later
            keyboard.tStart = t
            keyboard.frameNStart = frameN  # exact frame index
            keyboard.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(keyboard.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if keyboard.status == STARTED and t >= frameRemains:
            keyboard.status = STOPPED
        if keyboard.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if keyboard.keys == []:  # then this was the first keypress
                    keyboard.keys = theseKeys[0]  # just the first key pressed
                    keyboard.rt = keyboard.clock.getTime()
                    # was this 'correct'?
                    if (keyboard.keys == str(ans)) or (keyboard.keys == ans):
                        keyboard.corr = 1
                    else:
                        keyboard.corr = 0
        
        # *iti_square* updates
        if t >= 0.75 and iti_square.status == NOT_STARTED:
            # keep track of start time/frame for later
            iti_square.tStart = t
            iti_square.frameNStart = frameN  # exact frame index
            iti_square.setAutoDraw(True)
        frameRemains = 0.75 + trial_len - 0.75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if iti_square.status == STARTED and t >= frameRemains:
            iti_square.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyboard.keys in ['', [], None]:  # No response was made
        keyboard.keys=None
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           keyboard.corr = 1  # correct non-response
        else:
           keyboard.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('keyboard.keys',keyboard.keys)
    trials.addData('keyboard.corr', keyboard.corr)
    if keyboard.keys != None:  # we had a response
        trials.addData('keyboard.rt', keyboard.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "exit"-------
t = 0
exitClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
exitComponents = [done]
for thisComponent in exitComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "exit"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = exitClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *done* updates
    if t >= 0.0 and done.status == NOT_STARTED:
        # keep track of start time/frame for later
        done.tStart = t
        done.frameNStart = frameN  # exact frame index
        done.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if done.status == STARTED and t >= frameRemains:
        done.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "exit"-------
for thisComponent in exitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
