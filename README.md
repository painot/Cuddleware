# Cuddleware
### Description
- Module with mathematical aura
  
### Features
- Math stuff
- Physics stuff

### Setup

```py
import requests
import types
import importlib.util

url = "https://raw.githubusercontent.com/painot/Cuddleware/refs/heads/main/main.py"
code = requests.get(url).text

Cuddles = types.ModuleType('Cuddleware')
exec(code, Cuddles.__dict__)
```
### Functions
```py
# Functions to be added soon
```

<br>
<b>Stable release expected to come out July 2025</b>
