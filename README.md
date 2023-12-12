# ipytoolbox

A collection of IPython magic commands and other utilities.

## Features

- `%autocuda` - automatically select a CUDA device with the most free memory

## Install

First make sure Python is installed, then run:

```sh
pip install ipytoolbox
```

Then you can use it in IPython or Jupyter Notebooks by

```ipython
%load_ext ipytoolbox
```

## Develop

First clone the repo and set it as working directory. Then install the package in development mode (preferably within its own virtual environment):

```sh
pip install -e ".[tests]"
```

If you have `direnv` installed, you can run `direnv allow` to automatically create and activate a Python virtual environment when you enter the directory.

### Test

```sh
pytest
```

### Lint

```sh
pre-commit run --all-files
```

Or `pre-commit install` to run automatically on `git commit`.

### Publish

```sh
gh release create
```
