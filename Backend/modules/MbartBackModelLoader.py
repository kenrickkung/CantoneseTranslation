from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from modules.BaseModelLoader import BaseModelLoader
import chinese_converter

class MbartBackModelLoader(BaseModelLoader):
    def __init__(self, path):
        super().__init__()
        if path == " ":
            path = "Synthetic-1t1-NLLB"
        self.load_model(f"./models/mbart-en/{path}")
    
    def load_model(self, path):
        # Model-specific loading logic for Model A
        print("Loading MBart Model...")
        self.tokenizer = AutoTokenizer.from_pretrained(
            "facebook/mbart-large-50-many-to-many-mmt",
        )
        self.tokenizer.src_lang = "en_XX"

        self.model = AutoModelForSeq2SeqLM.from_pretrained(
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
            forced_bos_token_id=self.tokenizer.lang_code_to_id["zh_CN"],
            max_length=50
        )

        translation = self.tokenizer.batch_decode(
            translated_tokens,
            skip_special_tokens=True
        )[0]

        return chinese_converter.to_traditional(translation)




