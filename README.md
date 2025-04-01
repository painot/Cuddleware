# Cuddleware 🧸
## Description
- Module with mathematical aura
- Module with random ahh stuff
- Module with cuddles, tickles n snuggles (kawaii ahh mf)
- Some functions are directly called from numpy/scipy
- I am NOT a pro btw 😭😭
  
## Features
- Math stuff
- Physics stuff
- Random stuff

## Setup

```py
import requests
import types

url = "https://raw.githubusercontent.com/painot/Cuddleware/main/main.py"
code = requests.get(url).text

Cuddles = types.ModuleType("Cuddleware")
exec(code, Cuddles.__dict__)
```

## Functions
#### Maths

```py
# MORE SOON
Cuddles.lerp(a, b, t) # linear interpolation
Cuddles.clamp(value, min, max) # keep a number in range
Cuddles.lambertW(x) # from scipy, x = xe^x
Cuddles.gamma(x) # from scipy, (n-1)!
Cuddles.code(values, factor) # make data easier to understand
Cuddles.deocde(values, factor) # decode encoded data
Cuddles.distance(x1, y1, x2, y2) # dist between 2 pts
Cuddles.xerp(x, y, x_new) # exponential interpolation
```

#### Misc

```py
# MORE SOON
Cuddles.OneNotePages(entries) # creates pages from entries list, focus on the OneNote window
```

<br>
<b>Full release expected to come out 20 June 2025</b>
