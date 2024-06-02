# Gamepass Buyer
## Introduction
It will buy gamepass from gamepassid 

## Code
```py
from roapi import buyer

cookie="Put_Your_Cookie"
GamepassID = 123456
DeleteAfterBought = True

buyer(cookie).buy(DeleteAfterBought,GamepassID)
```
