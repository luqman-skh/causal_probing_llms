from transformers import AutoTokenizer, AutoModel, AutoConfig

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name, output_hidden_states=True)
config = AutoConfig.from_pretrained(model_name)
print(f"Number of layers: {config.num_hidden_layers}")