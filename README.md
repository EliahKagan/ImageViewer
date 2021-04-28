# Image Viewer - an, um, image viewer

**Image Viewer** is a picture viewing program that I wrote to learn
[PySide](https://www.qt.io/qt-for-python). If you&rsquo;re learning it too,
then you might&hellip; *not* really benefit much from this, since there are
many image viewing sample programs written by people who already know what
they&rsquo;re doing.

Actually, my initial motivation was to have a simple cross-platform image
viewer&mdash;other than my web browser&mdash;that could open [.webp
files](https://en.wikipedia.org/wiki/WebP), in addition to all the more
long-standing image types. Qt&rsquo;s `QPixmap` class automatically supports
this, so one gets WebP support with no special effort, when writing an image
viewer targeting Qt.

Image Viewer should run on GNU/Linux systems (such as Ubuntu), Windows, and
macOS. It depends on some other software, mainly PySide6. I suggest using a
virtual environment with [`pipenv`](https://pypi.org/project/pipenv/). To do
that, [install `pipenv` if you don&rsquo;t have it](getting-pipenv.md), then
from the top-level directory of this repository, run:

```bash
pipenv sync
```

Then, to run Image Viewer:

```bash
./viewer
```

Unfortunately, [a bug in Qt](https://bugreports.qt.io/browse/PYSIDE-1547) gives
an error on some systems:

```text
ImportError: libOpenGL.so.0: cannot open shared object file: No such file or directory
```

If you see an error message that ends with that line, you'll have to install
libOpenGL. How to do that varies across systems, but on Debian and Ubuntu, run:

```bash
sudo apt update
sudo apt install libopengl0
```

Then you should be able to run Image Viewer (and other PySide6 programs)
without a crash.
