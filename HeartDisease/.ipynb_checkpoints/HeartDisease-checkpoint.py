#**********************************
#  Heart Failure Prediction Dataset
#************************************
# **Objectif** : Identifier une possible défaillance cardiaque chez l'individu 
#*************************************

#Packages nécessaires 

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
#%matplotlib inline
sns.set_style("darkgrid")
from sklearn.impute import SimpleImputer
from sklearn.datasets import make_classification
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer,make_column_selector
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder,RobustScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.tree import export_graphviz, DecisionTreeClassifier
from sklearn.feature_selection import RFE, RFECV, chi2, SelectKBest, mutual_info_classif

#***********
import sys 
sys.path.insert(0, "/Users/asnga/KatalyseGits/mypackage")
from mypackage import functions 

#recupeeration du jeu de données 
HeartD_df = pd.read_csv("heart.csv")

#df : copie du jeu de données initial
df = HeartD_df.copy()

functions.dshape(df)
