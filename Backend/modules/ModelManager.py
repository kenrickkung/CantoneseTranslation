import torch
from models.NllbForwardModelLoader import NllbForwardModelLoader
from models.NllbBackModelLoader import NllbBackModelLoader
from models.OpusForwardModelLoader import OpusForwardModelLoader
from models.OpusBackModelLoader import OpusBackModelLoader
from collections import OrderedDict

class ModelManager:
    def __init__(self):
        self.device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        self.models = OrderedDict()  # Keeps track of loaded models
        self.max_models = 4  # Max number of models to keep in memory simultaneously
        
        # Load 2 Default Model
        self.load_model("nllb", "zh")
        self.load_model("nllb", "en")

    def load_model(self, model_name, src):
        # Load a model
        model = self._load_model_logic(model_name, src)
        model.to_device()
        model.set_eval_mode()

        # If the max number of models is exceeded, unload the least recently used model
        if len(self.models) >= self.max_models:
            self._unload_least_recently_used_model()

        # Add or move the model to the end to mark it as the most recently used
        self.models[f"{model_name}-{src}"] = model

        return model

    def _load_model_logic(self, model_name, src):
        if model_name == "nllb" and src == "zh":
            return NllbForwardModelLoader()
        if model_name == "nllb" and src == "en":
            return NllbBackModelLoader()
        if model_name == "opus" and src == "zh":
            return OpusForwardModelLoader()
        if model_name == "opus" and src == "en":
            return OpusBackModelLoader()
        raise ValueError("The Model does not Exist")

    def _unload_least_recently_used_model(self):
        # Remove the least recently used model from memory and GPU
        _, model = self.models.popitem(last=False)
        del model
        if self.device == "mps":
            torch.mps.empty_cache()

    def get_model(self, model_name, src):
        if f"{model_name}-{src}" in self.models:
            # Move to the end to mark as recently used
            model = self.models.pop(f"{model_name}-{src}")
            self.models[f"{model_name}-{src}"] = model
        else:
            model = self.load_model(model_name, src)
        return model
