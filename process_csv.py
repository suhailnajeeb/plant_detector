from utils import get_data_root
import toml
import pandas as pd
import json

cfg_path = 'config.toml'
cfg = toml.load(cfg_path)

data_root = get_data_root(cfg)

train_csv_path = data_root + 'train.csv'
converted_train_csv_path = data_root + 'converted_train.csv'

print('Loading CSV...')
train_df = pd.read_csv(train_csv_path)

entries = []

print('Converting CSV...')
for idx, row in train_df.iterrows():
    entry = {}
    entry['image_name'] = row['image_id'] + '.jpg'
    entry['page_width'] = row['width']
    entry['page_height'] = row['height']
    bbox = json.loads(row['bbox'])
    entry['x'] = bbox[0] #+ bbox[2] / 2
    entry['y'] = bbox[1] #+ bbox[3] / 2
    entry['width'] = bbox[2]
    entry['height'] = bbox[3]
    entry['labels'] = 0
    entries.append(entry)

converted_train_df = pd.DataFrame(entries)

converted_train_df.to_csv(converted_train_csv_path, index=False)
print('Done!')
print('Saved to: ' + converted_train_csv_path)