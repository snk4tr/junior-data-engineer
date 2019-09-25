import torch
import torch.nn as nn


class MnistNet(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(config['model']['input_size'], config['model']['layer1']),
                                 nn.ReLU(),
                                 nn.Linear(config['model']['layer1'], config['model']['layer2']),
                                 nn.ReLU(),
                                 nn.Linear(config['model']['layer2'], config['model']['output_size']),
                                 nn.LogSoftmax(dim=1))

    def forward(self, *input):
        return self.net(input)
