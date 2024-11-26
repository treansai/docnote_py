from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

class Model:
    def __init__(self,
                 model_name: str, 
                 device: str = "cpu", 
                 tokenizer_name: str = None, 
                 prefix: str = ""):
        self.model_name = model_name  
        self.tokenizer_name = tokenizer_name  
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name or model_name)
        self.model = AutoModelForTokenClassification.from_pretrained(model_name)
        self.device = device
        self.name = f"{prefix}{model_name}"

    def predict(self, text: str):
        nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer, device=self.device)
        return nlp(text)
    
    def load(self, model_name: str, device: str = "cpu", tokenizer_name: str = None):
        self.model = AutoModelForTokenClassification.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name or model_name)
        self.device = device
    
    def save(self, model_name: str):
        self.model.save_pretrained(model_name)
        self.tokenizer.save_pretrained(model_name)

    def __str__(self):  
        return f"Model(name={self.name}, model_name={self.model_name}, device={self.device}, tokenizer_name={self.tokenizer_name})"
    
    def __repr__(self):
        return self.__str__()
