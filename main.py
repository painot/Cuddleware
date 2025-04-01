# Painot, 30/03/2025, 20:00
# Cuddleware - A module for cute mathematical cuddles, snuggles and tickles!

import math
import pyautogui
import time
import os
import random
import numpy
import scipy

# print("[Cuddleware] Started <3")

Version = 1

# MATH

def lerp(a, b, t):
    return a + (b - a) * t

def clamp(min_value, max_value, value):
    return max(min(value, max_value), min_value)

def lambertW(x):
    return scipy.special.lambertw(x).real
def gamma(x):
    return scipy.special.gamma(x)

def code(values, code):
    return [value * code for value in values]

def decode(values, code):
    return [value / code for value in values]

# MISC

def OneNotePages(list):
    for entry in list:
        pyautogui.hotkey('ctrl', 'n')
        pyautogui.write(entry)
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)

if __name__ == "__main__":
    # print("You are not supposed to run Cuddleware directly!")
    pass
