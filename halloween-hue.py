#!/usr/bin/env python3
import random
import time

from phue import Bridge
from pync import Notifier

BRIGHTNESS = 255# Max is 255
TRANSITION_TIME = 5  # Deciseconds for transition

bridge_ip = "192.168.86.24"
b = Bridge(bridge_ip)

all_lights = b.get_light_objects()

to_cycle = all_lights  # Set the lights you want to cycle.

ORANGE = (0.6, 0.4)
RED = (0.67, 0.32)
GREEN = (0.15, 0.8)
PURPLE = (0.25, 0.1)
PINK = (0.5, 0.25)

print("Ctrl + C to stop cycling.")
colors = [ORANGE, GREEN, RED, PURPLE, PINK]
color_i = 0
while True:
    print("Cycling lights to: {}".format(colors[color_i]))
    for light in to_cycle:
        if not light.on:
            message = "Light {} is off!".format(light.name)
            print(message)
            Notifier.notify(message)
        #  Set the transition time of all lights to TRANSITION_TIME
        light.transitiontime = TRANSITION_TIME
        light.brightness = BRIGHTNESS
        light.xy = random.choice(colors)

    time.sleep(TRANSITION_TIME / 10)
    color_i = (color_i + 1) % len(colors)
