from .magics import CustomMagics


def load_ipython_extension(ipython):
    ipython.register_magics(CustomMagics)


def unload_ipython_extension(ipython):
    pass
