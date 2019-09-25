import torch.nn as nn


def get_mnist_net(config: dict):
    return nn.Sequential(nn.Linear(config['model']['input_size'], config['model']['layer1']),
                         nn.ReLU(),
                         nn.Linear(config['model']['layer1'], config['model']['layer2']),
                         nn.ReLU(),
                         nn.Linear(config['model']['layer2'], config['model']['output_size']),
                         nn.LogSoftmax(dim=1))
