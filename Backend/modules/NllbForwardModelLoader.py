from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from models.BaseModelLoader import BaseModelLoader

class NllbForwardModelLoader(BaseModelLoader):
    def __init__(self, path="./models/nllb-forward-1t1"):
        super().__init__()
        self.load_model(path)
    
    def load_model(self, path):
        # Model-specific loading logic for Model A
        print("Loading NLLB Model...")
        self.tokenizer = AutoTokenizer.from_pretrained(
            "facebook/nllb-200-distilled-600M",
            src_lang="yue_Hant",
            tgt_lang="eng_Latn"
        )

        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            path,
            local_files_only=True
        )

        self.to_device()
        self.set_eval_mode()
    
    def translate(self, text):
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)

        translated_tokens = self.model.generate(
            **inputs,
            forced_bos_token_id=self.tokenizer.lang_code_to_id["eng_Latn"],
            max_length=30
        )

        return self.tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]




