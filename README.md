# ipytoolbox

A collection of IPython magic commands and other utilities.

## Features

### `%autocuda`

Automatically select the local CUDA device(s) with most free memory.

<img width="673" alt="image" src="https://github.com/carlthome/ipytoolbox/assets/1595907/7634b369-1c68-4e69-a2fd-fc938c7a2261">

### `%animate`

Automatically capture `plt.plot(); plt.show()` calls and display them as an animation once the cell has finished executing.

[Example notebook](./notebooks/demo.ipynb)

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
