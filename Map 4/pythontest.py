########################################################################
#                                                                      #
#	CoSpace Robot                                                      #
#	Version 3.0.0                                                      #
#	March 2024                                                         #
#	Copyright (C) 2024 CoSpace Robot. All Rights Reserved              # 
#                                                                      #
#   This template is for CoSpace Auto-Driving                          # 
#                                                                      #
########################################################################


import math


Duration = int(0)
CurAction = int(-1)
CurGame = int(0)
MyState_1 = int(0)
US_Front = int(0)
IR_L3 = int(0)
IR_L2 = int(0)
IR_L1 = int(0)
IR_M0 = int(0)
IR_R1 = int(0)
IR_R2 = int(0)
IR_R3 = int(0)
CS_R = int(0)
CS_G = int(0)
CS_B = int(0)
RotationX = int(0)
RotationY = int(0)
RotationZ = int(0)
Time = int(0)
WheelLeft = int(0)
WheelRight = int(0)
LED_1 = int(0)
AI_TeamID = int(1) #Robot Team ID.    1:Blue Ream;    2:Red Team.
AI_SensorNum = int(15)



############ CoSpace System Functions,Please DON't modify. ##################
#############################################################################

def GetCurAction():#Get the Current Action ID
    global CurAction
    return CurAction

TaskList = [] #Task List for Code Challenge
def AddTaskItem(TaskID,StationID,ActionID): #Add One task.
    global TaskList
    if len(TaskList) == 0 : 
        for i in range(0,30) :
            TaskList.append([0,0,0])
    if StationID>29 or StationID < 0 :
        print("AddTaskItem: Error StationID = {}",StationID)
    TaskList[StationID] = [TaskID, StationID, ActionID]
    print("TaskItem[{}] = {}\r\n".format(StationID,TaskList[StationID]))   
    return 0

TaskString = "" #Task String for Code Challenge
def SetTaskString(gameTask):#Set Task String for Code Challenge
    global TaskString
    TaskString = gameTask
    print("TaskString:{}".format(TaskString))
    return 1

def GetGameID():#Get the Current Game ID
    global CurGame
    return CurGame


iTurnToGoAhead = int(0)
def TurnTo(curRot, targetRot):#May not work well in Swarmland.
    global WheelLeft,WheelRight  
    global Duration
    global iTurnToGoAhead
    #global SuperDuration #Uncomment this statement for super Action.
    
    angularErrorThreshold = 2
    minTuningSpeed = 4
    angleDiff = (curRot - targetRot + 360) % 360
    turningSpeed = 0        
    Duration = 128
    #SuperDuration = 128; #Uncomment this statement for super Action.
    if iTurnToGoAhead > 0 :
        iTurnToGoAhead = iTurnToGoAhead + 1
        WheelLeft = 40
        WheelRight = 40
        if iTurnToGoAhead > 8: #Stop this turning action after go ahead 8 time units. 
            Duration = 0
            #SuperDuration = 0;#Uncomment this statement for super Action.
            iTurnToGoAhead = 0
            return 0
        return 1
    if angleDiff <= angularErrorThreshold or angleDiff > 360 - angularErrorThreshold:
        turningSpeed = 0
    elif angleDiff <= 180:
        turningSpeed = angleDiff / 6 + minTuningSpeed
    else:
        turningSpeed = (angleDiff - 360) / 6 - minTuningSpeed
    #The Robot Turns
    WheelLeft = turningSpeed
    WheelRight = -WheelLeft
    #Reach the targetRot,then go ahead.
    if turningSpeed == 0: 
        iTurnToGoAhead = 1
    return 1
#############################################################################


def SetGameID(GameID) :#Set the Current Game ID
    global CurGame,Duration
    global MyState_1
    if CurGame != GameID and GameID > 0 :
        GameStart()
        Duration = 0
        MyState_1 = 0;
    CurGame = GameID

 
def GetTeamName() :# Return Team name : DON't change function defination.
    return "pythontest"#You Should change it into your team's Name.

def GetDebugVar_Value() : #DON'T modify this line
    global Duration, CurAction, CurGame, MyState_1, US_Front, IR_L3
    global IR_L2, IR_L1, IR_M0, IR_R1, IR_R2, IR_R3
    global CS_R, CS_G, CS_B, RotationX, RotationY, RotationZ
    global Time, WheelLeft, WheelRight, LED_1
    return [Duration,CurAction,CurGame,MyState_1,US_Front,IR_L3,IR_L2,IR_L1,IR_M0,IR_R1,IR_R2,IR_R3,CS_R,CS_G,CS_B,RotationX,RotationY,RotationZ,Time,WheelLeft,WheelRight,LED_1]

def GetDebugVar_Name(): #DON'T modify this function
    return "Duration,CurAction,CurGame,MyState_1,US_Front,IR_L3,IR_L2,IR_L1,IR_M0,IR_R1,IR_R2,IR_R3,CS_R,CS_G,CS_B,RotationX,RotationY,RotationZ,Time,WheelLeft,WheelRight,LED_1"

def SetDataAI(AI_IN): #DON'T modify this function
    global US_Front, IR_L3, IR_L2, IR_L1, IR_M0, IR_R1, IR_R2, IR_R3, CS_R, CS_G, CS_B, RotationX, RotationY, RotationZ, Time
    US_Front = AI_IN[0]
    IR_L3 = AI_IN[1]
    IR_L2 = AI_IN[2]
    IR_L1 = AI_IN[3]
    IR_M0 = AI_IN[4]
    IR_R1 = AI_IN[5]
    IR_R2 = AI_IN[6]
    IR_R3 = AI_IN[7]
    CS_R = AI_IN[8]
    CS_G = AI_IN[9]
    CS_B = AI_IN[10]
    RotationX = AI_IN[11]
    RotationY = AI_IN[12]
    RotationZ = AI_IN[13]
    Time = AI_IN[14]



def GetCommand() :#DON'T modify this function
    global WheelLeft, WheelRight, LED_1
    return [WheelLeft, WheelRight, LED_1]

def Game0():
    global Duration, CurAction, CurGame
    global WheelLeft, WheelRight, LED_1
    global MyState_1, US_Front, IR_L3, IR_L2, IR_L1, IR_M0, IR_R1, IR_R2, IR_R3, CS_R, CS_G, CS_B, RotationX, RotationY, RotationZ, Time
    if Duration>0:
        Duration = Duration - 1
    elif 1:  #Statement-1
        Duration = 0
        CurAction =1

    
#Statements for CurAction
    if CurAction == 1:  #Statement-1:
        WheelLeft = 0
        WheelRight = 0
        LED_1 = 0


def GameStart():
    #Add your code here!
    return

def AILoopStart():
    # Useless function
    return

#-----------------------------------------------------------------------------------------------------------------
# IF YOU WANT TO COPY COPY FROM BELOW THIS LINE AND PASTE IT IN THE SAME SPOT IN YOUR OWN CODE
# HIGHLY ENCOURAGED TO LEARN AND UNDERSTAND WHAT THE CODE DOES
# ANY QUESTIONS FILE A GITHUB ISSUE REQUEST OR CONTACT ME/SOMEONE WHO KNOWS PYTHON

# Black line tracking
def getPosBlack():
    pos = 0
    count = 0

    if IR_L3 == 0:
        pos += -5
        count += 1
    if IR_L2 == 0:
        pos += -3
        count += 1
    if IR_L1 == 0:
        pos += -1
        count += 1
    if IR_R1 == 0:
        pos += 1
        count += 1
    if IR_R2 == 0:
        pos += 3
        count += 1
    if IR_R3 == 0:
        pos += 5
        count += 1

    if count > 0:
        pos = pos / count
    return pos

def linefollowBlack(speed, gain):
    global WheelLeft, WheelRight
    pos = getPosBlack()
    if pos > 0:
        WheelLeft = speed
        WheelRight = speed - (gain * speed * pos / 5.0)
    else:
        WheelLeft = speed + (gain * speed * pos / 5.0)
        WheelRight = speed

# White line tracking
def getPosWhite():
    pos = 0
    count = 0

    if IR_L3 == 1:
        pos += -5
        count += 1
    if IR_L2 == 1:
        pos += -3
        count += 1
    if IR_L1 == 1:
        pos += -1
        count += 1
    if IR_R1 == 1:
        pos += 1
        count += 1
    if IR_R2 == 1:
        pos += 3
        count += 1
    if IR_R3 == 1:
        pos += 5
        count += 1

    if count > 0:
        pos = pos / count
    return pos

def linefollowWhite(speed, gain):
    global WheelLeft, WheelRight
    pos = getPosWhite()
    if pos > 0:
        WheelLeft = speed
        WheelRight = speed - (gain * speed * pos / 5.0)
    else:
        WheelLeft = speed + (gain * speed * pos / 5.0)
        WheelRight = speed

# Stop function
def stop():
    global WheelLeft, WheelRight
    WheelLeft = 0
    WheelRight = 0

# Move forward function
def moveForward():
    global WheelLeft, WheelRight
    WheelLeft = 70
    WheelRight = 70

# Turn right function
def turnRight():
    global WheelLeft, WheelRight
    WheelLeft = 30
    WheelRight = -10

# Turn left function
def turnLeft():
    global WheelLeft, WheelRight
    WheelLeft = -10
    WheelRight = 30

# U turn function
def U_turn():
    global WheelLeft, WheelRight
    WheelLeft = 19
    WheelRight = -19

# Colour identification (set colour below with rgb values)
def isColor(r, g, b):
    if (
        CS_R > r - 10 and CS_R < r + 10
        and CS_G > g - 10 and CS_G < g + 10 and
        CS_B > b - 10 and CS_B < b + 10):
        return True
    else:
        return False

def is_orange():
    return isColor(172, 103, 0)

def is_lightblue():
    return isColor(4, 80, 192)

def is_blue():
    return isColor(0, 0, 0)

def is_magenta():
    return isColor(146, 5, 127)

def is_darkorange():
    return isColor(0, 0, 0)

def is_darkgreen():
    return isColor(0, 0, 0)

def is_purple():
    return isColor(0, 0, 0)

def is_green():
    return isColor(0, 0, 0)

def is_lightred():
    return isColor(0, 0, 0)

def is_pink():
    return isColor(0, 0, 0)

def is_brown():
    return isColor(0, 0, 0)

# Cardinal directions 
def is_south():
    if RotationZ > 177 and RotationZ < 183:
        return True
    else:
        return False

def is_west():
    if RotationZ > 87 and RotationZ < 93:
        return True
    else:
        return False

def is_east():
    if RotationZ > 267 and RotationZ < 273:
        return True
    else:
        return False

def is_north():
    if RotationZ > -3 and RotationZ < 3:
        return True
    else:
        return False

# Important for code to run
gameState = int(1)
stateTime = int(0)

def nextState():
    global gameState, stateTime
    gameState += 1
    stateTime = 0

speed = 100
gain = 1.5

# For timers
def is_duration(duration):
    if stateTime >= (duration * 40):
        return True
    return False

# Follows in simulation direction
def gyro_follow(angle, speed):
    error = 0 # Initialize error

    if angle > 180:
        if RotationZ < (angle - 180): # Corrected condition
            RotationZ -= 360
    else:
        if RotationZ > (angle + 180): # Corrected condition
            RotationZ -= 360

    error = RotationZ - angle # Corrected variable name

    move_steering(speed, error) # Corrected argument order

# Move steering function
def move_steering(speed, steering): # Corrected argument order
    global WheelLeft, WheelRight
    if steering > 100:
        steering = 100
    if steering < -100:
        steering = -100
    if steering > 0:
        WheelLeft = speed
        WheelRight = speed - (2 * speed * steering / 100)
    else:
        WheelLeft = speed + (2 * speed * steering / 100)
        WheelRight = speed

# Checkpoint function
def checkpoint():
    global LED_1
    stop()
    LED_1 = 1

def zRange(direction): # Adjust range here if you need a tighter turn
    lower = direction - 10
    upper = direction + 10
    if RotationZ > lower and RotationZ < upper:
        return True
    
def invertzRange(direction): # Adjust range here if you need a tighter turn
    invertdirection = direction # TODO: Implement this


# The in and out function
def inandout(speed, gain, direction, flipdirection, is_color1, is_color2=None): # is_color should be the actual colour function, direction is cardinal direction, function will flip it, should support all directions
    global LED_1, WheelLeft, WheelRight
    LocalState = 1

    if is_color2 is None:
        is_color2 = is_color1

    if LocalState == 1:
        linefollowBlack(speed, gain)
        if is_color1():
            LocalState += 1

    if LocalState == 2:
        gyro_follow(direction, speed)
        if zRange(direction) == True:   
            LocalState += 1

    if LocalState == 3:
        linefollowBlack(speed, gain)
        if is_orange():
            LocalState += 1

    if LocalState == 4:
        checkpoint()
        if is_duration(2):
            LED_1 = 0
            LocalState += 1

    if LocalState == 5:
        gyro_follow(flipdirection, speed)
        if invertzRange(flipdirection) == True:
            LocalState += 1

    if LocalState == 6:
        linefollowBlack(speed, gain)
        if is_color2():
            LocalState += 1

    return

def Game0():
    #Add your code here!
    global stateTime, LED_1, WheelLeft, WheelRight, RotationZ, CS_R, CS_G, CS_B, IR_L1, IR_L2, IR_L3, IR_R1, IR_R2, IR_R3 # Declare globals

    stateTime += 1

    if gameState == 1:
        linefollowWhite(speed, gain)
        if is_orange():
            nextState()

    if gameState == 2: # Checkpoint 1
        checkpoint()
        if is_duration(2):
            LED_1 = 0
            nextState()

    if gameState == 3:
        if inandout(speed, gain, 180, 0, is_blue) == True:
            nextState()

    if gameState == 4:
        gyro_follow(90, speed)
        if is_east():
            nextState()

    if gameState == 5:
        checkpoint()
        if is_duration(2):
            LED_1 = 0
            nextState()

    if gameState == 6:
        if inandout(speed, gain, 180, 0, is_magenta) == True:
            nextState()

    if gameState == 7:
        gyro_follow(90, speed)
        if is_east():
            nextState()

    if gameState == 8:
        linefollowBlack(speed, gain)
        if is_orange():
            nextState()

    if gameState == 9:
        checkpoint()
        if is_duration(2):
            LED_1 = 0
            nextState()

    if gameState == 10:
        if inandout(speed, gain, 270, 90, is_darkorange) == True:
            nextState()

    if gameState == 11:
        gyro_follow(0, speed)
        if is_north():
            nextState()

    if gameState == 12:
        linefollowBlack(speed, gain)
        if is_darkgreen():
            nextState()

    if gameState == 13:
        gyro_follow(270, speed)
        if is_west():
            nextState()

    if gameState == 14:
        linefollowBlack(speed, gain)
        if is_orange():
            nextState()

    if gameState == 15:
        checkpoint()
        if is_duration(2):
            LED_1 = 0
            nextState()
    
    if gameState == 16:
        linefollowBlack(speed, gain)
        if is_purple():
            nextState()
    
    if gameState == 17:
        gyro_follow(0, speed)
        if is_north():
            nextState()
    
    if gameState == 18:
        linefollowBlack(speed, gain)
        if is_orange():
            nextState()
    
    if gameState == 19:
        checkpoint()
        if is_duration(2):
            LED_1 = 0
            nextState()

    if gameState == 20:
        linefollowBlack(speed, gain)
        if is_green():
            nextState()
    
    if gameState == 21:
        if inandout(speed, gain, 180, 0, is_green) == True:
            nextState()

    if gameState == 22:
        gyro_follow(270, speed)
        if is_west():
            nextState()

    if gameState == 23:
        if inandout(speed, gain, 180, 0, is_lightred) == True:
            nextState()

    if gameState == 24:
        gyro_follow(270, speed)
        if is_west():
            nextState()

    if gameState == 25:
        linefollowBlack(speed, gain)
        if is_orange():
            nextState()
    
    if gameState == 26:
        checkpoint()
        if is_duration(2):
            LED_1 = 0
            nextState()

    if gameState == 27:
        moveForward()
        if is_duration(0.5):
            nextState()
    
    if gameState == 28:
        linefollowBlack(speed, gain)
        if is_orange():
            nextState()

    if gameState == 29:
        checkpoint()
        if is_duration(2):
            LED_1 = 0
            nextState()

    if gameState == 30:
        moveForward()
        if is_duration(0.5):
            nextState()

    if gameState == 31:
        linefollowBlack(speed, gain)
        if is_orange():
            nextState()

    if gameState == 32:
        checkpoint()
        if is_duration(2):
            LED_1 = 0
            nextState()

    if gameState == 33:
        moveForward()
        if is_duration(0.5):
            nextState()

    if gameState == 34:
        linefollowBlack(speed, gain)
        if is_orange():
            nextState()

    if gameState == 35:
        checkpoint()
        if is_duration(2):
            LED_1 = 0
            nextState()

    if gameState == 36:
        linefollowBlack(speed, gain)
        if is_pink():
            nextState()

    if gameState == 37:
        gyro_follow(0, speed)
        if is_north():
            nextState()
    
    if gameState == 38:
        linefollowBlack(speed, gain)
        if is_brown():
            nextState()

    if gameState == 39:
        moveForward()
        if is_duration(0.5):
            nextState()

    if gameState == 40:
        gyro_follow(60, speed)
        if RotationZ == zRange(60):
            nextState()

    if gameState == 41:
        linefollowBlack(speed, gain)
        if is_brown():
            nextState()

    if gameState == 42:
        moveForward()
        if is_duration(0.5):
            nextState()

    if gameState == 43:
        gyro_follow(90, speed)
        if RotationZ == zRange(90):
            nextState()

    if  gameState == 44:
        linefollowBlack(speed, gain)
        if is_orange():
            nextState()

    if gameState == 45:
        checkpoint()
        if is_duration(2):
            LED_1 = 0
            nextState()

    return 1

def AILoop():
    
    global CurGame,WheelLeft,WheelRight,LED_1
    AILoopStart()
    if CurGame == 0:
        Game0()
    else:
        WheelLeft= 0;  WheelRight= 0;  LED_1= 0;

