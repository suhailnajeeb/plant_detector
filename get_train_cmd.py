from utils import get_data_root
import toml
import os
import pyperclip

cfg_path = 'config.toml'
cfg = toml.load(cfg_path)
data_root = get_data_root(cfg)
train_path = os.path.join(data_root, 'train')
train_path = '"' + train_path + '"'

cmd_string = "python src/train.py -n {} -t {}".format(train_path, train_path)
pyperclip.copy(cmd_string)

print('You have to execute the following command:')
print('-' * 80)
print(cmd_string)
print('-' * 80)
print('Command has been copied to clipboard! Just paste to run!')

#os.system(run_string)