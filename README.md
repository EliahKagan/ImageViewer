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

## How to run it

Image Viewer should run on GNU/Linux systems (such as Ubuntu), Windows, and
macOS. It depends on some other software, mainly PySide6. I suggest using a
virtual environment with [`pipenv`](https://pypi.org/project/pipenv/). To do
that, [install `pipenv` if you don&rsquo;t have it](getting-pipenv.md), then
from the top-level directory of this repository, run:

```bash
pipenv update
```

Then, to run Image Viewer:

```bash
pipenv run python viewer
```

(You can alternatively use `pipenv run ./viewer`, except on Windows.)

That opens a file picker dialog, in which you select a picture to open.

If you like, you can instead pass the path as a command-line argument, such as:

```bash
pipenv run python viewer unexpected-bobcat.webp
```

(Likewise, `pipenv run ./viewer unexpected-bobcat.webp` works except on
Windows.)

If you're going to run Image Viewer multiple times in succession, you can have
`pipenv` start you a shell:

```bash
pipenv shell
```

Then you can run it in the shell like this:

```bash
python viewer
```

(Though you&rsquo;ll likely prefer simply `./viewer`&mdash;except on Windows.)

To be reminded of how to run it:

```bash
python viewer --help
```

## The `libOpenGL.so.0` bug

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
