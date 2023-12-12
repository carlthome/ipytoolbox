import os
from unittest.mock import patch

import pytest
from IPython.testing.globalipapp import get_ipython

NVIDIA_SMI_OUTPUT = b"""\
0, 24253
1, 24253
2, 8136
3, 24253
4, 24253
5, 24253
6, 24253
7, 4060"""


@pytest.fixture
def ipython():
    ipython = get_ipython()
    assert ipython is not None
    ipython.run_line_magic("load_ext", "ipytoolbox")
    yield ipython
    ipython.run_line_magic("unload_ext", "ipytoolbox")


def test_autocuda(ipython):
    with patch("subprocess.check_output", return_value=NVIDIA_SMI_OUTPUT):
        ipython.run_line_magic("autocuda", "-d 1")
    assert os.environ["CUDA_VISIBLE_DEVICES"] == "0"
