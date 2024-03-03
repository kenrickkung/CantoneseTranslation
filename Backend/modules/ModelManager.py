import torch
from modules.MbartBackModelLoader import MbartBackModelLoader
from modules.MbartForwardModelLoader import MbartForwardModelLoader
from modules.OpusForwardModelLoader import OpusForwardModelLoader
from modules.OpusBackModelLoader import OpusBackModelLoader
from modules.NllbForwardModelLoader import NllbForwardModelLoader
from modules.NllbBackModelLoader import NllbBackModelLoader
from collections import OrderedDict
from os import listdir

class ModelManager:
    def __init__(self):
        self.device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        self.models = OrderedDict()  # Keeps track of loaded models
        self.max_models = 4  # Max number of models to keep in memory simultaneously
        self.model_types = set(["nllb", "opus", "mbart"])
        self.srcs = set(["zh", "en"])

    def get_model_path(self, model_type, src):
        if model_type not in self.model_types:
            raise ValueError(f"Model Type {model_type} does not Exist")
        if src not in self.srcs:
            raise ValueError(f"Source {src} does not Exist")
        
        return [file for file in listdir(f"models/{model_type}-{src}") if not file.startswith('.')]


    def _load_model(self, model_type, src, path):
        # Load a model
        model = self._load_model_logic(model_type, src, path)
        model.to_device()
        model.set_eval_mode()

        # If the max number of models is exceeded, unload the least recently used model
        if len(self.models) >= self.max_models:
            self._unload_least_recently_used_model()

        # Add or move the model to the end to mark it as the most recently used
        self.models[f"{model_type}-{src}-{path}"] = model

        return model

    def _load_model_logic(self, model_type, src, path):
        if path != " " and path not in self.get_model_path(model_type, src):
                raise ValueError("The Model Path does not exist")
        if model_type == "nllb" and src == "zh":
            return NllbForwardModelLoader(path)
        if model_type == "nllb" and src == "en":
            return NllbBackModelLoader(path)
        if model_type == "opus" and src == "zh":
            return OpusForwardModelLoader(path)
        if model_type == "opus" and src == "en":
            return OpusBackModelLoader(path)
        if model_type == "mbart" and src == "zh":
            return MbartForwardModelLoader(path)
        if model_type == "mbart" and src == "en":
            return MbartBackModelLoader(path)
        raise ValueError(f"The Model Type {model_type} or Source {src} does not Exist")

    def _unload_least_recently_used_model(self):
        # Remove the least recently used model from memory and GPU
        _, model = self.models.popitem(last=False)
        del model
        if self.device == "mps":
            torch.mps.empty_cache()

    def get_model(self, model_type, src, path):
        if f"{model_type}-{src}-{path}" in self.models:
            # Move to the end to mark as recently used
            model = self.models.pop(f"{model_type}-{src}-{path}")
            self.models[f"{model_type}-{src}-{path}"] = model
        else:
            model = self._load_model(model_type, src, path)
        return model
