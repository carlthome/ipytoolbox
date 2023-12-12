%load_ext ipytoolbox
%ipytoolbox

import torch
assert torch.cuda.is_available()
%env CUDA_VISIBLE_DEVICES
torch.cuda.device_count()
