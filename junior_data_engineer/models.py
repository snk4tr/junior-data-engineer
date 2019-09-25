import torch
import os
import re

from junior_data_engineer.graphs import MnistNet


class MnistModel:
    def __init__(self, config):
        self.name = self.__class__.__name__.lower()[:-5]  # remove postfix 'model' from name.

        self.__device = self.__config['general']['device']
        if self.__device is None:
            self.__device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

        self.__config = config
        self.__model = self.__init_model()

    def predict(self, digit_image: torch.Tensor) -> int:
        """
        Perform inference of MNIST model.
        Args:
            digit_image(torch.Tensor): content image to be recognized.

        Returns(int):
            the number from the picture.
        """
        self.__model.eval()
        with torch.no_grad():
            log_probs = self.__model(digit_image).cpu()
            print('log_probs:', log_probs)

        probs = torch.exp(log_probs)
        probab = list(probs.cpu().numpy()[0])
        return probab.index(max(probab))

    def __init_model(self):
        """
        Initialize style model of given architecture.
        Returns(torch.nn.Module):
            ready for inference initialized style model.
        """
        weights_to_use_path = self.__weights_path()
        with torch.no_grad():
            style_model = MnistNet(self.__config)
            state_dict = torch.load(weights_to_use_path)

            # remove saved deprecated running_* keys in InstanceNorm from the checkpoint
            for k in list(state_dict.keys()):
                if re.search(r'in\d+\.running_(mean|var)$', k):
                    del state_dict[k]

            style_model.load_state_dict(state_dict)
            style_model.to(self.__device)

        return style_model

    def __weights_path(self):
        """
        Define path to the models weights.
        Returns(str):
            path to the models weights.
        """
        root_folder = self.__config['general']['weights_root_folder']
        model_folder = self.name
        weights_name = self.__config['style']['weights_name']

        weights_path = os.path.join(root_folder, model_folder, weights_name)
        assert os.path.exists(weights_path), f"There is not weights for style model! " \
            f"Expected to have weights in path: [{weights_path}]"
        assert os.path.isfile(weights_path), f"Found weights are not file! (Folder? O_o)"

        return weights_path
