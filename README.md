# autocuda

TODO

## Usage

First make sure Python is installed, then run:

```sh
pip install autocuda
```

Then you can use it in IPython or Jupyter Notebooks by

```ipython
%load_ext autocuda
%autocuda
```

Check that it worked by

```ipython
import torch
assert torch.cuda.is_available()
%env CUDA_VISIBLE_DEVICES
torch.cuda.device_count()
```

## Develop

First clone the repo and set it as working directory. Then install the package in development mode (preferably within its own virtual environment):

```sh
pip install -e .[tests]
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
