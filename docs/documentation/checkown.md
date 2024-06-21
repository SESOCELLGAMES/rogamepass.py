# Checking If Bought
## Introduction
There is 2 functions for that, check_own and check_bought. check_own Searches Player Inventory Other One is Checks sales of gamepass. Both returns a Bool Value. But check_own Doesn't need a cookie to get.

## Code 1 (check_own)
```py
from roapi import gamepass

GamepassID = 123456
UserID = 1

print(gamepass().check_own(UserID,GamepassID))

```

## Code 2 (check_bought)
```py
from roapi import gamepass

cookie="Put_Your_Cookie"
GamepassID = 123456

print(gamepass(cookie).check_bought(GamepassID))
```
