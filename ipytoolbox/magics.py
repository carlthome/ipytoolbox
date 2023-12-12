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

        # Run nvidia-smi to get a list of devices and their memory usage.
        cmd = f"nvidia-smi --query-gpu=index,memory.free --format=csv,nounits,noheader"
        lines = subprocess.check_output(cmd, shell=True).decode().splitlines()

        # Sort lines by free memory, then take the first N devices.
        lines.sort(reverse=True, key=lambda line: int(line.split(",")[1]))
        devices = [line.split(",")[0] for line in lines[: args.max_devices]]

        # Set CUDA_VISIBLE_DEVICES to the list of devices.
        devices = ",".join(devices)
        os.environ["CUDA_VISIBLE_DEVICES"] = devices
