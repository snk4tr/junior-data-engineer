# Junior Data Engineer task

This repository in created as a reference solution for Junior Data Engineer technical task.
The code in based on:
- [How to Move Your Machine Learning Model to Production](https://www.linode.com/docs/applications/big-data/how-to-move-machine-learning-model-to-production/) tutorial (Keras).
- [Handwritten Digit Recognition Using PyTorch](https://towardsdatascience.com/handwritten-digit-mnist-pytorch-977b5338e627) (as a reference for PyTorch MNIST model).

Expected task completion time: **3h**.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine or remote server.

### Prerequisites

* docker `18.09.4+` :white_check_mark:

### Installing

1. Clone this repository on your local machine or remote server:     
`$ git clone https://gitlab.ta.philips.com/pilrus/junior-data-engineer`

2. Create `config.yaml` file based on `config-template.yaml`. Fill it with
you personal info and set of parameters you prefer.

3. Start the run script, it will do all the work:    
`$ bash run.sh <port>`, where `<port>`  is http-port on host machine.

## Built with

* Docker image based on [Deepo](https://github.com/ufoym/deepo)

### Authors

* **Sergey Kastryulin** - _Initial work_ - `sergey.kastryulin@philips.com` 