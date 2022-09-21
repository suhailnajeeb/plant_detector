import platform

def get_data_root(cfg):
    # check the system plafrorm and return data root
    if platform.system() == 'Darwin':
        return cfg['mac']['data_root']