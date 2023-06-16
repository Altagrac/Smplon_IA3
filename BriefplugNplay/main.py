from fastapi import FastAPI, UploadFile, File
from torchvision.transforms import transforms
from PIL import Image
import torch
from torchvision.models import resnet50
from torch.nn.functional import softmax
from transformers import AutoImageProcessor, ResNetForImageClassification

app = FastAPI()

# Charger le modèle ResNet pré-entraîné
#model = resnet50(pretrained=True)
#model.eval()

processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
model_DL = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")


# Définir les transformations d'image nécessaires
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Définir les classes d'étiquettes pour ImageNet
LABELS_URL = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
LABELS = torch.hub.load_state_dict_from_url(LABELS_URL)

# Définir la route pour la classification d'image
@app.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    image = Image.open(file.file)

    # Appliquer les transformations d'image
    image = transform(image)
    image = image.unsqueeze(0)

    # Effectuer la prédiction avec le modèle
    with torch.no_grad():
        output = model(image)
        probabilities = softmax(output, dim=1)[0]
        _, predicted_idx = torch.max(output, 1)
        predicted_label = LABELS[predicted_idx.item()]

    return {"predicted_label": predicted_label, "probabilities": probabilities.tolist()}
















#from fastapi import FastAPI
#from typing import Union
#import pandas as pd
#import pickle

#app = FastAPI()

#@app.get("/")
#async def root():
#    return {"message": "Let's succeed"}
