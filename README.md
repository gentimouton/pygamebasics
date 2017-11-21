# pygamebasics
super simple pygame programs

# installation
From https://docs.python.org/3/using/windows.html#installation-steps
1. Download `Windows x86-64 executable installer` from https://www.python.org/downloads/release/python-363/
1. Run it. Check the `Add python 3.6 to PATH` box, and select `Customize installation`. 
1. Next screen, in `Customize install location`, specify `C:\python36`.

- [installing python on windows](https://docs.python.org/3/using/windows.html#installation-steps)
- [installing pygame](https://www.pygame.org/wiki/GettingStarted#Windows%20installation)
- Adding a package on Windows: `python -m pip install numpy`
- In Eclipse, [fix PyDev "Undefined variable from import" errors?](https://stackoverflow.com/a/30381908) if needed.
- [Eclipse Neon/Oxygen dark theme](https://marketplace.eclipse.org/content/eclipse-color-theme)
- installing numpy in python3.6: [download package](https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy), then `pip install package.whl`. Compiling is [harder](https://stackoverflow.com/questions/28413824/installing-numpy-on-windows).


# coding for both python 2 and 3
- Use // for integer division, and add 0.0 to ints if you intend for float division.
- Put parenthesis around all print statements.

# links
- http://www.nerdparadise.com/programming/pygametips bunch of stuff!
- [blit PNG with transparent pixels with opacity](http://www.nerdparadise.com/programming/pygameblitopacity)
- [joystick fallback to keyboard](http://www.nerdparadise.com/programming/pygamejoystick), may require [muting joystick console output](https://stackoverflow.com/questions/36624000/how-to-hide-sdl-library-debug-messages-in-python) (this is fixed in python 3.6 and pygame 1.9.3)
- [cheat sheet](http://www.cogsci.rpi.edu/~destem/gamedev/pygame.pdf)
- [tips and tricks](https://github.com/cosmologicon/pyjam/wiki/pygame-notes-and-tricks)


# one-liners
- `import pygame; filter(lambda x:'K_' in x, dir(pygame))` lists all keys
