#!/bin/bash
CURRENT_BRIGHTNESS=$(</sys/class/backlight/intel_backlight/brightness head -n1)
# TWEAK BRIGHTNESS_STEP_VALUE AS YOU LIKE
BRIGHTNESS_STEP_VALUE=53
MAX_BRIGHTNESS=$(</sys/class/backlight/intel_backlight/max_brightness head -n1)
BRIGHTNESS_STEPS=$(( $MAX_BRIGHTNESS / $BRIGHTNESS_STEP_VALUE ))


if [ "$1" == "UP" ]; then
    if [ "$CURRENT_BRIGHTNESS" -lt "$MAX_BRIGHTNESS" ]; then
        qdbus org.kde.Solid.PowerManagement /org/kde/Solid/PowerManagement/Actions/BrightnessControl org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness $(( $CURRENT_BRIGHTNESS + $BRIGHTNESS_STEPS ))
    fi
else
    if [ "$CURRENT_BRIGHTNESS" -gt $(($MAX_BRIGHTNESS/$BRIGHTNESS_STEP_VALUE)) ]; then
            qdbus org.kde.Solid.PowerManagement /org/kde/Solid/PowerManagement/Actions/BrightnessControl org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness $(( $CURRENT_BRIGHTNESS - $BRIGHTNESS_STEPS ))
    fi
fi