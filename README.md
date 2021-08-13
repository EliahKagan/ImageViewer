<!--
  Copyright (c) 2021 Eliah Kagan

  Permission to use, copy, modify, and/or distribute this software for any
  purpose with or without fee is hereby granted.

  THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
  REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
  AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
  INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
  LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
  OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
  PERFORMANCE OF THIS SOFTWARE.
-->

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

## License

Image Viewer [**is licensed**](LICENSE) under
[0BSD](https://spdx.org/licenses/0BSD.html).

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

## Other dependency satisfaction bugs

Sometimes other libraries are needed. In particular, you may get:

```text
t.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, xcb.
```

I don&rsquo;t think this happens on Windows; if it does, I don&rsquo;t know how
to solve it there.

Otherwise, to find out how to fix it, re-run the command that produced that
error with the `QT_DEBUG_PLUGINS` environment variable set to `1`. For example,
in a Bourne-style shell like `bash` or `zsh`, if you ran `./viewer`, run:

```bash
QT_DEBUG_PLUGINS=1 ./viewer
```

Likewise, if you ran `pipenv run ./viewer`, run:

```bash
QT_DEBUG_PLUGINS=1 pipenv run ./viewer
```

This produces lots of output. Look near the end, just above the text that appeared before when you ran it without `QT_DEBUG_PLUGINS=1`, and look for an error message that ends like

```text
(FILENAME: cannot open shared object file: No such file or directory)
```

but with some filename in place of `FILENAME`. For example:

```text
Cannot load library /home/ek/.local/share/virtualenvs/ImageViewer-hsDVqvxw/lib/python3.9/site-packages/PySide6/Qt/plugins/platforms/libqxcb.so: (libxcb-icccm.so.4: cannot open shared object file: No such file or directory)
```

In that example, the file I needed was `libxcb-icccm.so.4`.

Then search for how to install the package that provides that file on your
system. Depending on what system or (especially in the case of macOS) what
third-party package manager you&rsquo;re using, you may be able to do this
directly from the package manager. Or you may be able to check online: for
example, you can [search the contents of packages for
Debian](https://www.debian.org/distrib/packages#search_contents) or [search the
contents of packages for Ubuntu](https://packages.ubuntu.com/#search_contents).

Then install that package and try again. You may be missing multiple libraries,
but the error output will only tell you about one each time, so you may need to
do it a few times.
