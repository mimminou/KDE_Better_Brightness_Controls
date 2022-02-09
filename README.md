# KDE_Better_Brightness_Controls
Better Brightness control script for laptops running linux under KDE ( Will Also prevent screen from turning off when hitting 0 ).

This script is to be added through KDE's Custom Shortcuts Menu in Settings as a Global Shortcut.

There are 2 variants of this code, one is written in bash, and the other one is python based (for python 3.6+ , requires dasbus module to work).
Both do exactly the same thing , but i presume that the python script has a lot more overhead and therefore might run slower than the bash counterpart (Did not test but seems logical to me).


You will have to change the `BRIGHTNESS_STEP` variable to one of the divisors of `MAX_BRIGHTNESS` (You can read it's value by running `cat /sys/class/backlight/intel_backlight/max_brightness` in terminal). Note that this isn't obligatory but if your device has a max brightness value of 1060 (Like my laptop for example), dividing by 53 will yield 20 steps of brightness controle.
