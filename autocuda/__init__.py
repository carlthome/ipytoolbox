import os
import subprocess

from IPython.core.magic import Magics, line_magic, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring


@magics_class
class CustomMagics(Magics):
    @magic_arguments()
    @argument("-d", "--max-devices", help="Maximum number of devices to use.", type=int, default=1)
    @line_magic
    def autocuda(self, line):
        args = parse_argstring(self.autocuda, line)
        cmd = f"nvidia-smi --query-gpu=memory.free,index --format=csv,nounits,noheader | sort -nr | head -{args.max_devices} | awk '{{ print $NF }}'"
        devices = subprocess.check_output(cmd, shell=True).decode().splitlines()
        devices = ",".join(devices)
        os.environ["CUDA_VISIBLE_DEVICES"] = devices


def load_ipython_extension(ipython):
    ipython.register_magics(CustomMagics)


def unload_ipython_extension(ipython):
    pass
