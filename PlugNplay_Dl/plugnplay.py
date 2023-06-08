###  ** README **
# 1. Identifier une tache à réaliser. Exemples: reconnaissance d’image, chat bot... ::

#   *Traduction automatique :  un modèle de Deep Learning qui peut traduire automatiquement
#   du texte dans différentes langues.
#   Vous pouvez utiliser des données de jeux de données publics tels que Multi30k, Europarl*

# 2. Trouver un model de deep learning déjà entrainer pour effectuer cette tâche
#     Exemples : open AI, Tensorflow...

from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Chargement du modèle Hugging Face pour la détection de la langue
model_name = "papluca/xlm-roberta-base-language-detection"
language_detection = pipeline("text-classification", model=model_name)

@app.route('/detect-language', methods=['POST'])
def detect_language():
    text = request.json['text']
    result = detect_language(text)
    return jsonify(result)

def detect_language(text):
    result = language_detection(text)
    return {
        'label': result[0]['label'],
        'score': result[0]['score']
    }

if __name__ == '__main__':
    app.run(debug=True)









# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# from flask import Flask, render_template, request
# import torch
# app = Flask(__name__)

# # Nom du modèle pré-entrainé
# nom_modele = "bert-base-multilingual-cased"

# # Charger le tokenizer et le modèle
# tokenizer = AutoTokenizer.from_pretrained(nom_modele)
# modele = AutoModelForSequenceClassification.from_pretrained(nom_modele)

# # Fonction de reconnaissance de la langue
# def reconnaitre_langue(texte):
#     inputs = tokenizer(texte, return_tensors="pt")
#     outputs = modele(**inputs)
#     predictions = outputs.logits.argmax(dim=1)
#     langue_predite = tokenizer.decode(predictions.item())
#     return langue_predite

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         texte_utilisateur = request.form['texte']
#         langue = reconnaitre_langue(texte_utilisateur)
#         return render_template('resultat.html', langue=langue)
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()
