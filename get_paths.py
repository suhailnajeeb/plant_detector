from utils import get_data_root
import toml

cfg_path = 'config.toml'

cfg = toml.load(cfg_path)

data_root = get_data_root(cfg)
print('Data Root: ' + data_root)

train_csv_path = data_root + 'train.csv'
print('Train CSV Path:' + train_csv_path)

