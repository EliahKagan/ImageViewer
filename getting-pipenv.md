# Getting `pipenv`

These are some brief instructions for installing
[`pipenv`](https://pypi.org/project/pipenv/).

## Prerequisite: Python

I assume you have [Python](https://www.python.org/). Image Viewer uses Python
3. If you&rsquo;re running a GNU/Linux system (such as Ubuntu) then you almost
certainly have Python 3 already.

## You might have `pipenv` already

You might have `pipenv` already. Try running:

```bash
pipenv
```

If that gives a list of commands, you have `pipenv`.

## Your shell may have told you what to do

On some systems, running a command that you don&rsquo;t hve but that is
available from the system&rsquo;s package manager tells you how to install it;
then you can just follow those instructions.

If not, the best way to install it depends on your personal preferences and
what operating system you&rsquo;re running.

## Installing `pipenv` with your system&rsquo;s package manager

If you're using a GNU/Linux system, it&rsquo;s likely been packaged your
system. For example, on all recent versions of Debian and Ubuntu, you can just
run:

```bash
sudo apt update
sudo apt install pipenv
```

## Installing `pipenv` with `pip`

Otherwise, or if you don&rsquo;t have administrative powers on the machine
you&rsquo;re using, or if you just prefer to install it for just your user
account, then you can install it with [`pip`](https://pypi.org/project/pip/).

### On GNU/Linux and macOS

```bash
python3 -m pip install --user pipenv
```

On some systems, `python` means `python2`; on others, it means `python3`; on
still others, there is on `python` command. But if you don&rsquo;t have a
`python3` command, check if `python` is Python 3 by running `python -V`. If it
is, run:

```bash
python -m pip install --user pipenv
```

### On Windows

```powershell
py -3 -m pip install --user pipenv
```

<sup>`py` is the [Python launcher for
Windows](https://www.python.org/dev/peps/pep-0397/).</sup>

## Further reading

[&ldquo;Pipenv & Virtual
Environments&rdquo;](https://docs.python-guide.org/dev/virtualenvs/) in [*The
Hitchhiker&rsquo;s Guide to Python*](https://docs.python-guide.org/) by Kenneth
Reitz and Tanya Schlusser.
