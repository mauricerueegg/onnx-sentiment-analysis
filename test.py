# Preprocess
import torch
import numpy as np
from simpletransformers.model import TransformerModel
from transformers import RobertaForSequenceClassification, RobertaTokenizer

text = "DevOps is very good"
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
input_ids = torch.tensor(tokenizer.encode(text, add_special_tokens=True)).unsqueeze(0)  # Batch size 1

# Run
import onnxruntime

ort_session = onnxruntime.InferenceSession("roberta-sequence-classification-9.onnx")

def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(input_ids)}
ort_out = ort_session.run(None, ort_inputs)

# Postprocess
pred = np.argmax(ort_out)
if(pred == 0):
    print("Prediction: negative")
elif(pred == 1):
    print("Prediction: positive")