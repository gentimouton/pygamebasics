# pygamebasics
super simple pygame programs. 

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


# existing non-trivial games
- [bomberman](https://github.com/joereynolds/Mr-Figs), with map editor
- [cabbage and kings](https://github.com/Mekire/cabbages-and-kings)
- [tuxemon](https://github.com/Tuxemon/Tuxemon)
- [pyroller](https://github.com/iminurnamez/pyroller): casino mini games. Controller switches scenes, [with unit testing](https://github.com/iminurnamez/pyroller/blob/master/test/testcontrol.py)
- [bunch of pyweek entries](https://github.com/cosmologicon/pyjam)

# tips
- http://www.nerdparadise.com/programming/pygametips bunch of stuff!
- [surfarray and mixer tips](https://github.com/cosmologicon/pyjam/wiki/pygame-notes-and-tricks)
- [newbie guide to pygame](http://pygame.org/docs/tut/newbieguide.html)
- `import pygame; filter(lambda x:'K_' in x, dir(pygame))` lists all keyboard keys

# demo scripts
- [tutorials](http://www.pygame.org/docs/), surfarray, camera, sprite, tips
- [gfx surfarray hacks, and some font, gui, and utility scripts](http://pygame.org/pcr/repository.php).
- [mekire's samples](https://github.com/Mekire/pygame-samples)
- [blit PNG with transparent pixels with opacity](http://www.nerdparadise.com/programming/pygameblitopacity)
- [playing multiple sounds simultaneously](https://stackoverflow.com/questions/15385727/pygame-mixer-only-plays-one-sound-at-a-time)
- [joystick fallback to keyboard](http://www.nerdparadise.com/programming/pygamejoystick), may require [muting joystick console output](https://stackoverflow.com/questions/36624000/how-to-hide-sdl-library-debug-messages-in-python) (this is fixed in python 3.6 and pygame 1.9.3)
- [Tileset guide](https://bitbucket.org/thesheep/qq/src/ce58427c58263abdd02a10976ca5514d20c2701b/qq.py)
- [simple map editor](https://joereynoldsaudio.com/programming/articles/building-a-level-editor)
- [unit testing](http://infinitemonkeycorps.net/docs/pph/#id5)
- [singleton allowing for unit testing](http://glyph.twistedmatrix.com/2007/07/functional-functions-and-python.html)
- [dirty sprite monkey punch](https://github.com/n0nick/dirty_chimp)
- [greyscale image conversion with surfarray](https://stackoverflow.com/a/10693616)


# maybe useful libraries
- [entity-component framework for games, with example code](https://github.com/cosmologicon/enco)
- [ptext](https://github.com/cosmologicon/pygame-text)
- [pview](https://github.com/cosmologicon/pygame-view)
- [better sprite class](https://github.com/n0nick/pygame-sprites)

# numpy
- [numeric manual from 2001](http://people.csail.mit.edu/jrennie/python/numeric/numeric-manual.pdf)
- [advanced class about array and ufunc](http://www.scipy-lectures.org/advanced/advanced_numpy/index.html)

# PIL
- [recent doc](https://pillow.readthedocs.io/en/4.3.x/reference/Image.html)
- [old effbot doc](http://www.effbot.org/imagingbook/pil-index.htm)
- [img mono conversion](https://stackoverflow.com/a/37497975)
- [img palette conversion](https://stackoverflow.com/a/12646282)
