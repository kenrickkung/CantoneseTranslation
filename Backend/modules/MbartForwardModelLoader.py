from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from modules.BaseModelLoader import BaseModelLoader

class MbartForwardModelLoader(BaseModelLoader):
    def __init__(self, path):
        super().__init__()
        if path == " ":
            path = "Synthetic-1t1-NLLB"
        self.load_model(f"./models/mbart-zh/{path}")
    
    def load_model(self, path):
        # Model-specific loading logic for Model A
        print("Loading MBart Model...")
        self.tokenizer = MBart50TokenizerFast.from_pretrained(
            "facebook/mbart-large-50-many-to-many-mmt",
        )
        self.tokenizer.src_lang = "zh_CN"

        self.model = MBartForConditionalGeneration.from_pretrained(
            path,
            local_files_only=True
        )

        self.to_device()
        self.set_eval_mode()
    
    def translate(self, text):
        inputs = self.tokenizer(
            text,
            return_tensors="pt"
        ).to(self.device)

        translated_tokens = self.model.generate(
            **inputs,
            forced_bos_token_id=self.tokenizer.lang_code_to_id["en_XX"],
            max_length=50
        )

        return self.tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]




