import torch

# Initialize your model and load it into GPU on import
class BaseModelLoader:
    def __init__(self):
        self.device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        self.model = None

    def load_model(self, path):
        raise NotImplementedError("This method should be overridden by subclasses.")
    
    def translate(self, text):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def to_device(self):
        if self.model:
            self.model.to(self.device)

    def set_eval_mode(self):
        if self.model:
            self.model.eval()

