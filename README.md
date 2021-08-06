# Introduction

EHRPrepator prepares EHR datasets to an understandable format for both human
and computer. We belive that, if humans can undertand, computador also can.

# Contributing
## Testing

To test locally, Ehrpreper uses `tox`, which means you can build locally using:
```
pip install tox
tox
```
### Using your local version

To trial using your local development branch of Ehrpreper, I recommend you use
a virtual environment. e.g:

```shell
python3 -m venv .venv
source .venv/bin/activate
```
> `python3 -m venv .venv` creates a new virtual environment (in current working
> directory) called `.venv`.
> `source .venv/bin/activate` activates the virtual environment so that packages
> can be installed/uninstalled into it. [More info on venv](https://docs.python.org/3/library/venv.html).

Once you're in a virtual environment, run:

```shell
pip install -Ur requirements.txt -Ur requirements_dev.txt
python setup.py develop
```

> `setup.py develop` installs the package using a link to the source code so
> that any changes which you make will immediately be available for use.
>
> `pip install -Ur requirements.txt -Ur requirements_dev.txt` installs the
> project dependencies as well as the dependencies needed to run linting,
> formatting, and testing commands. This will install the most up-to-date
> package versions for all dependencies.
