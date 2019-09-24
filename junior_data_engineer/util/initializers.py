import yaml


def load_config(path: str) -> dict:
    with open(path, 'r') as f:
        config = yaml.load(f)

    return config
