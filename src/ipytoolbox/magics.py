import os
import subprocess

from IPython.core.magic import Magics, cell_magic, line_magic, magics_class
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

    @cell_magic
    def animate(self, line, cell):
        from matplotlib.lines import Line2D
        import matplotlib.animation
        import matplotlib.pyplot as plt

        plt.rcParams["animation.html"] = "jshtml"
        fig = plt.figure()

        captured_data = []

        def capture():
            ax = plt.gca()
            lines = ax.get_lines()
            ax.cla()
            data = lines[0].get_data()
            captured_data.append(data)

        show = plt.show
        plt.show = capture
        exec(cell, globals(), locals())
        plt.show = show

        ax = fig.gca()

        def func(data) -> list[Line2D]:
            lines = ax.get_lines()
            lines[0].set_data(data)
            return lines

        def init_func() -> list[Line2D]:
            lines = ax.plot([], [])
            return lines

        animation = matplotlib.animation.FuncAnimation(
            fig=fig,
            func=func,
            init_func=init_func,
            frames=captured_data,
            blit=True,
            interval=100,
        )

        plt.close()
        return animation
