# Introduction à <img src="https://global.discourse-cdn.com/business7/uploads/streamlit/original/2X/8/8cb5b6c0e1fe4e4ebfd30b769204c0d30c332fec.png" alt="drawing" width="300"/>
## Etape 0 - installation :
## pip install streamlit
&nbsp;
## Etape 1 - arborescence des fichiers :
.
├── README.md
├── app
│   ├── app.py
│   └── pages
│       └── 01_page.py
├── data
│   └── data.csv
└── requirements.txt
├── .streamlit
│   └── secrets.toml
└── .gitignore

&nbsp;

## Etape 2 - Exécution :
- fichier app.py contenant tout le code python, avec les méthodes streamlit permettant la mise en page web préconçue.
 Voir la <a src='https://docs.streamlit.io/library/cheatsheet%27%3Edoc</a>
- exécution du code via serveur, ligen de commande dans le Terminal :
&nbsp;
streamlit run app.py
&nbsp;
## Etape 3 - déploiement
- déploiement expliqué <a src='https://streamlit.io/cloud%27%3Eici</a>)
