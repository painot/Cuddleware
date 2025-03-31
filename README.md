# Cuddleware
### Description
- Module with mathematical aura
- Cuddles, tickles n snuggles (kawaii ahh mf)
  
### Features
- Math stuff
- Physics stuff

### Setup

```py
import requests
import types
import importlib.util

url = "https://raw.githubusercontent.com/painot/Cuddleware/main/main.py"
code = requests.get(url).text

Cuddles = types.ModuleType('Cuddleware')
exec(code, Cuddles.__dict__)
```
### Functions
```py
# MORE COMING SOON

.lerp(a, b, t) # linear interpolation
.clamp(value, min, max) # keep a number in range
```

<br>
<b>Stable release expected to come out July 2025</b>
