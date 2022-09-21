import platform

def get_data_root(cfg):
    # check the system plafrorm and return data root
    if platform.system() == 'Darwin':
        return cfg['mac']['data_root']
    if platform.system() == 'Linux':
        return cfg['linux']['data_root']