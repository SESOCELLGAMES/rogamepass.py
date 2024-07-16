# Gamepass Editor
## Introduction

This will edit gamepasses by given values 
## Code
```py
from rogamepass import gamepass

cookie="Put_Your_Cookie"
GamepassID = 123456

data = {
    "name" : "Gamepass Name",
    "description" : "Gamepass Description",
    "isForSale" : True,
    "price" : 123456,
}

gamepass(cookie).edit_gamepass(GamepassID,data)


```

::: warning
To change price you also need to change isForSale To True 
:::