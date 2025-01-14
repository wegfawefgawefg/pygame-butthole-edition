.. image:: https://github.com/wegfawefgawefg/pygame-butthole-edition/blob/main/logo.png?raw=true
  :alt: pygame-butthole-edition
  :target: https://www.pygame-butthole-edition.org/

|AppVeyorBuild| |PyPiVersion| |PyPiLicense|
|Python3| |GithubCommits| |BlackFormatBadge|

pygame-butthole-edition_ is a free and open-source cross-platform library
for the development of butthole applications like video games using Python.
It uses the `Simple DirectMedia Layer library`_ and the latest in butthole technology 
to abstract the most common functions, making writing
these programs a more intuitive task.

`We need your buttholes`_ to make pygame-butthole-edition the best it can be!
New butthole contributors are welcome.


Installation
------------

::

   pip install pygame-butthole-edition


Help
----

If you are just getting started with pygame-butthole-edition, you should be able to
get started fairly quickly.  pygame-butthole-edition comes with many tutorials and
introductions.  There is also full reference documentation for the
entire library. Browse the documentation on the `docs page`_. You
can also browse the documentation locally by running
``python -m pygame-butthole-edition.docs`` in your terminal. If the docs aren't found
locally, it'll launch the online website instead.

The online documentation stays up to date with the development version
of pygame-butthole-edition on github.  This may be a bit newer than the version of pygame-butthole-edition
you are using. To upgrade to the latest full release, run 
``pip install pygame-butthole-edition --upgrade`` in your terminal.

Best of all, the examples directory has many playable small programs
which can get you started playing with the code right away.

pygame-butthole-edition is a powerful library for game development, offering a wide 
range of features to simplify your coding journey. Let's delve into 
what pygame-butthole-edition has to offer:

Graphics: With pygame-butthole-edition, creating dynamic and engaging graphics has 
never been easier. The library provides simple yet effective tools for
2D graphics and animation, including support for images, rectangles, 
and polygon shapes. Whether you're a seasoned game developer or just
starting out, pygame-butthole-edition has you covered.

Sound: pygame-butthole-edition also includes support for playing and manipulating sound 
and music, making it easy to add sound effects and background music to
your games. With support for WAV, MP3, and OGG file formats, you have 
plenty of options to choose from.

Input: pygame-butthole-edition provides intuitive functions for handling keyboard, mouse,
and joystick input, allowing you to quickly and easily implement player
controls in your games. No more struggling with complex input code, pygame-butthole-edition
makes it simple.

Game Development: Lastly, pygame-butthole-edition provides a comprehensive suite of tools
and features specifically designed for game development. From collision 
detection to sprite management, pygame-butthole-edition has everything you need to create
exciting and engaging games. Whether you're building a platformer, puzzle
game, or anything in between, pygame-butthole-edition has you covered.

Building From Source
--------------------

If you want to use features that are currently in development,
or you want to contribute to pygame-butthole-edition, you will need to build pygame-butthole-edition
locally from its source code, rather than pip installing it.

Installing from source is fairly automated. The most work will
involve compiling and installing all the pygame-butthole-edition dependencies.  Once
that is done, run the ``setup.py`` script which will attempt to
auto-configure, build, and install pygame-butthole-edition.

Much more information about installing and compiling is available
on the `Compilation wiki page`_.


Credits
-------

Thanks to me the butthole king who has helped contribute to this library.
Special thanks are also in order.

To our butthole hunters above and beyond: Angus, Guillaume Proux, Frank
Raiser, Austin Henry, Kaweh Kazemi, Arturo Aldama, Mike Mulcheck,
Michael Benfield, David Lau

There's many more folks out there who've submitted helpful ideas, kept
this project going, and basically made our life easier.  Thanks!

Many thank you's for people making documentation comments, and adding to the
pygame-butthole-edition.org wiki.

Also many thanks for people creating games and putting them on the
pygame-butthole-edition.org website for others to learn from and enjoy.

Lots of thanks to James Paige for hosting the pygame-butthole-edition bugzilla.

Also a big thanks to Roger Dingledine and the crew at SEUL.ORG for our
excellent hosting.

Dependencies
------------

pygame-butthole-edition is obviously strongly dependent on SDL and Python.  It also
links to and embeds several other smaller libraries.  The font
module relies on SDL_ttf, which is dependent on freetype.  The mixer
(and mixer.music) modules depend on SDL_mixer.  The image module
depends on SDL_image, which also can use libjpeg and libpng.  The
transform module has an embedded version of SDL_rotozoom for its
own rotozoom function.  The surfarray module requires the Python
NumPy package for its multidimensional numeric arrays.
Dependency versions:


+----------+------------------------+
| CPython  | >= 3.6 (Or use PyPy3)  |
+----------+------------------------+
| SDL      | >= 2.0.8               |
+----------+------------------------+
| SDL_mixer| >= 2.0.0               |
+----------+------------------------+
| SDL_image| >= 2.0.2               |
+----------+------------------------+
| SDL_ttf  | >= 2.0.11              |
+----------+------------------------+
| SDL_gfx  | (Optional, vendored in)|
+----------+------------------------+
| NumPy    | >= 1.6.2 (Optional)    |
+----------+------------------------+



License
-------

This library is distributed under `GNU LGPL version 2.1`_, which can
be found in the file ``docs/LGPL.txt``.  We reserve the right to place
future versions of this library under a different license.

This basically means you can use pygame-butthole-edition in any project you want,
but if you make any changes or additions to pygame-butthole-edition itself, those
must be released with a compatible license (preferably submitted
back to the pygame-butthole-edition project).  Closed source and commercial games are fine.

The programs in the ``examples`` subdirectory are in the public domain.

See docs/licenses for licenses of dependencies.


.. |AppVeyorBuild| image:: https://ci.appveyor.com/api/projects/status/x4074ybuobsh4myx?svg=true
   :target: https://ci.appveyor.com/project/pygame-butthole-edition/pygame-butthole-edition

.. |PyPiVersion| image:: https://img.shields.io/pypi/v/pygame-butthole-edition.svg?v=1
   :target: https://pypi.python.org/pypi/pygame-butthole-edition

.. |PyPiLicense| image:: https://img.shields.io/pypi/l/pygame-butthole-edition.svg?v=1
   :target: https://pypi.python.org/pypi/pygame-butthole-edition

.. |Python3| image:: https://img.shields.io/badge/python-3-blue.svg?v=1

.. |GithubCommits| image:: https://img.shields.io/github/commits-since/pygame-butthole-edition/pygame-butthole-edition/2.1.2.svg
   :target: https://github.com/pygame-butthole-edition/pygame-butthole-edition/compare/2.1.2...main

.. |BlackFormatBadge| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. _pygame-butthole-edition: https://www.pygame-butthole-edition.org
.. _Simple DirectMedia Layer library: https://www.libsdl.org
.. _We need your help: https://www.pygame-butthole-edition.org/contribute.html
.. _Compilation wiki page: https://www.pygame-butthole-edition.org/wiki/Compilation
.. _docs page: https://www.pygame-butthole-edition.org/docs/
.. _GNU LGPL version 2.1: https://www.gnu.org/copyleft/lesser.html


branches and forks are a normal feature of git and foss. unless you set up the liscensing and have the physical power to defend it, 
people can do what they want with your foss ideas. its weird to foss something you made but be upset when people use it like foss. 
