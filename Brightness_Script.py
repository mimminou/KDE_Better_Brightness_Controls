import sys
from dasbus.connection import SessionMessageBus

#Needed to get the DCONF interface that handles screen brightness in KDE.
SESSION_BUS = SessionMessageBus() 
Proxy = SESSION_BUS.get_proxy("org.kde.Solid.PowerManagement","/org/kde/Solid/PowerManagement/Actions/BrightnessControl","org.kde.Solid.PowerManagement.Actions.BrightnessControl")


def getMaxBrightness():
    with open("/sys/class/backlight/intel_backlight/max_brightness") as maxBrightness:
        return int(maxBrightness.readline())


def getCurrentBrightness():
    with open("/sys/class/backlight/intel_backlight/brightness") as Brightness :
        return int(Brightness.readline())  


BRIGHTNESS_STEP_VALUE = 53 #! <--- It is best to leave the other variables as default and only tweak THIS value to change how many steps you want.
MAX_BRIGHTNESS = getMaxBrightness()
BRIGHTNESS_STEPS = MAX_BRIGHTNESS / BRIGHTNESS_STEP_VALUE

#When Pressing Birghtness UP Button
if(sys.argv[1]=="UP"):
    Current_Brightness = getCurrentBrightness()
    if(Current_Brightness<MAX_BRIGHTNESS):
        Proxy.setBrightness(Current_Brightness + int(BRIGHTNESS_STEPS))

#When Pressing Birghtness DOWN Button
elif(sys.argv[1]=="DOWN"):
    Current_Brightness = getCurrentBrightness()
    if(Current_Brightness > BRIGHTNESS_STEP_VALUE): #Prevent Screen from going to 0 and turning off
        Proxy.setBrightness(Current_Brightness - int(BRIGHTNESS_STEPS))