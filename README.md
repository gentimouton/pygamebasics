# pygamebasics
super simple pygame programs. 

# installation

install python
- download Python x86-64 https://www.python.org/downloads/windows/
- run instal exe as admin
- check the `Add python 3.6 to PATH` box, and select `Customize installation`
- `Customize install location` set it to `C:\python36`
- disable PATH length limit
- check in CLI that python starts
- check in CLI that `path` includes `C:\Python36`

install pygame
- in command line, `pip install -U pygame`
- don't instal with `--user`, it places the library in `~\AppData\Roaming\Python\Python36`, which is a hidden directory.
- if you get `TypeError: can only concatenate str`, it's because Pygame has not kept up with Python. Install an older Python.
- fyi pip installs into `C:\python36\Lib\site-packages`
- check in CLI `python -m pygame.examples.aliens`
- missing numpy? https://www.anaconda.com/download/ - don't set their python as default python

vscode setup
- access settings via `ctrl+,` and check path to interpreter in `python.pythonPath` is `c:/python36/python.exe`. See [link](https://code.visualstudio.com/docs/python/environments)

eclipse setup
- install for java 
- add pydev and egit (both from Liclipse) via `Help` > `Install new software`: http://update.liclipse.com/latest
- right click > new project > pydev > configure interpreter
- check: window > preferences > pydev > interpreters > python - check pygame is in packages below
- shortcuts: `Window > Preferences > General > Keys`, switch ctrl-tab from `next editor` to `next tab`, same with `previous tab`

more links
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
- [tower defense game with py2exe](https://code.google.com/archive/p/colortowerdefense/downloads)

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
- [masked blit with BLEND_RGBA_MULT](https://stackoverflow.com/a/16930209)


# maybe useful libraries
- [entity-component framework for games, with example code](https://github.com/cosmologicon/enco)
- [ptext](https://github.com/cosmologicon/pygame-text)
- [pview](https://github.com/cosmologicon/pygame-view)
- [better sprite class](https://github.com/n0nick/pygame-sprites)
- [pgu - GUI in pygame](https://code.google.com/archive/p/pgu/)


# numpy
- [numeric manual from 2001](http://people.csail.mit.edu/jrennie/python/numeric/numeric-manual.pdf)
- [advanced class about array and ufunc](http://www.scipy-lectures.org/advanced/advanced_numpy/index.html)

# PIL
- [recent doc](https://pillow.readthedocs.io/en/4.3.x/reference/Image.html)
- [old effbot doc](http://www.effbot.org/imagingbook/pil-index.htm)
- [img mono conversion](https://stackoverflow.com/a/37497975)
- [img palette conversion](https://stackoverflow.com/a/12646282)
- or consider [skimage](http://scikit-image.org/)

# making an executable
- [py2exe tuto](http://www.py2exe.org/index.cgi/Tutorial)
- [pygame 2 exe](http://www.pygame.org/wiki/Pygame2exe)
- [cx_freeze for python 3.6](https://stackoverflow.com/a/44433442)
- [making a tarball with distutils](https://wiki.python.org/moin/Distutils/Tutorial)
- [distutils doc](https://docs.python.org/3/distutils/examples.html) and [examples](https://docs.python.org/3/distutils/examples.html)
- [pynsist](https://github.com/takluyver/pynsist)
- [cxfreeze](https://www.youtube.com/watch?v=EY6ZCPxqEtM&index=17&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&t=0s)
