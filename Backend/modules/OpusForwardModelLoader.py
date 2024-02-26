from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from models.BaseModelLoader import BaseModelLoader

class OpusForwardModelLoader(BaseModelLoader):
    def __init__(self, path="./models/opus-mt-zh-en-finetuned"):
        super().__init__()
        self.load_model(path)
    
    def load_model(self, path):
        # Model-specific loading logic for Model A
        print("Loading Opus-MT Model...")
        self.tokenizer = AutoTokenizer.from_pretrained(
            path
        )
        self.model = AutoModelForSeq2SeqLM.from_pretrained(path)

        self.to_device()
        self.set_eval_mode()
    
    def translate(self, text):
        tokens = self.tokenizer(text, return_tensors="pt", padding=False).to(self.device)
        translated = self.model.generate(**tokens)
        return str([self.tokenizer.decode(t, skip_special_tokens=True) for t in translated][0])




