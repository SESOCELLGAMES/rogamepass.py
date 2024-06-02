# Gamepass Creator
## Introduction

This will create gamepasses by putting UniverseID and RobuxAmount

## Getting Universe ID
To get UniverseID you need to get Your game page from https://create.roblox.com/dashboard/creations and find your game 
   ![Creationstab](https://github.com/sesocell/roapi.py/blob/main/assets/gamepage.png?raw=true)
   Yay! You found it :D
   (I did this thing because i am bored why  somebody doesnt know how to find universeid coming to here very weird)
## Code
```py
from roapi import gamepass

cookie="Put_Your_Cookie"
AmountNumber = 1000
UniverseID = 123456

gamepass(cookie).pass_creator(AmountNumber,UniverseID)
```
