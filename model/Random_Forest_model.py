
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_curve, auc, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

#Como primer paso se importa la base de datos
df = pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')
df



#Variables a conservar : SMOKE si fuma o no, CALC cantidad de alchool que consume, NCP comidas al día, CH2O litros agua al día,FAF qué tan seguido se ejercita, TUE tiempo usando dispositivos electrónicos, MTRANS medio de transporte, FCVC frecuencia consumo vegetales
df = df.drop(columns=['Gender', 'Age', 'Height', 'Weight', 'family_history_with_overweight', 'CAEC', 'SCC', 'FAF'])

"""Antes de desarrollar los modelos, se hizo una selección de variables, ya que la pregunta de negocio se centra en predecir el nivel de obesidad según los hábitos, se segmentó un poco la información de la base de datos inicial, conservando solamente 8 variables relacionadas a los hábitos de los individuos, al segmentar también enfocamos el proyecto a que la herramienta final solamente haga 8 preguntas a los usuarios finales en lugar de un número más alto de estas, las variables elegidas s Variables a conservar :  

*   SMOKE, que determina si la persona fuma o no.
*   CALC, que explica la cantidad de alcohol que consume la persona.
*   NCP que es el número de comidas ingeridas al día.
*   CH2O que indica los litros agua consumidos al día.
*   FAF indica qué tan seguido se ejercita la persona.  
*   TUE que representa el tiempo que la persona usa dispositivos electrónicos.
*   MTRANS que representa el medio de transporte usado por la persona.
*   FCVC que es la frecuencia del consumo de vegetales.
"""

#Se separa la acoluma a predecir en el modelo de machine learning y también se vuelve binaria la variable de respuesta
y = df["NObeyesdad"]
df = df.drop(columns=['NObeyesdad'])


#Conversión de variables categóricas binarias a unos y ceros

df['SMOKE'] = df['SMOKE'].map({'yes': 1, 'no': 0})


catcols = df.select_dtypes(exclude = ['int64','float64']).columns
intcols = df.select_dtypes(include = ['int64']).columns
floatcols = df.select_dtypes(include = ['float64']).columns

# one-hot encoding para variables categóricas
df = pd.get_dummies(df, columns = catcols)

# minmax scaling para variabls numéricas
for col in df[floatcols]:
    df[col] = MinMaxScaler().fit_transform(df[[col]])

for col in df[intcols]:
    df[col] = MinMaxScaler().fit_transform(df[[col]])

print('Nuevo número de de variables: %d'%(df.shape[1]))

"""Luego se hizo un preprocesamiento de los datos donde básicamente se convierten a números las variables binarias categóricas que contienen información de texto, luego se realiza la técnica de “one hot encoding” para variables de más de dos categorías con el fin de convertir la información de estas en variables binarias numéricas, también se escalan las variables de tipo decimal con el fin de mantener una misma escala en los modelos. Se dividen las bases de datos en conjuntos de test y pruebas y se procede a realizar varios modelos de clasificación para variables categóricas no binarias (ya que se quiere predecir el tipo de obesidad 1, 2, 3, desnutrición o peso normal)"""

for i in df.columns:
  print(i)
  print(df[i].unique())
  print("=" * 30)  # Separador visual entre columnas

# Se dividen los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=42)

from sklearn.metrics import classification_report


# Modelo drandom forest
modelo_random_forest = RandomForestClassifier()
modelo_random_forest.fit(X_train, y_train)  # Asegúrate de que y_train contenga las etiquetas multiclase

def evaluar_random_forest_multiclase(X_test, y_test):
    # Predicciones de probabilidad para todas las clases
    y_probabilidades = modelo_random_forest.predict_proba(X_test)

    # Matriz de confusión
    matriz_confusion = confusion_matrix(y_test, modelo_random_forest.predict(X_test))

    # Gráficos
    # (La curva ROC no es relevante para problemas de clasificación multiclase)

    plt.figure(figsize=(6, 4))
    sns.heatmap(matriz_confusion, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=['Clase 0', 'Clase 1', 'Clase 2', 'Clase 3', 'Clase 4'],
                yticklabels=['Clase 0', 'Clase 1', 'Clase 2', 'Clase 3', 'Clase 4'])
    plt.xlabel('Predicción')
    plt.ylabel('Real')
    plt.title('Matriz de Confusión para Random Forest Multiclase')

    plt.tight_layout()
    plt.show()

    # Métricas multiclase
    exactitud = accuracy_score(y_test, modelo_random_forest.predict(X_test))
    print('Modelo de Random Forest Multiclase')
    print(f'Exactitud: {exactitud:.2f}')
    print(f'Matriz de Confusión:\n{matriz_confusion}')

    # Informe de clasificación, incluyendo sensibilidad (recall)
    report = classification_report(y_test, modelo_random_forest.predict(X_test))
    print(report)

# Evaluar modelo de Random Forest multiclase
evaluar_random_forest_multiclase(X_test, y_test)  # Asegúrate de que y_test contenga las etiquetas multiclase

"""En la fase inicial de análisis de modelos, se implementó un modelo Random Forest de clasificación multiclase. Este enfoque capitaliza la construcción de múltiples árboles de decisión, combinando así su poder predictivo. Para evaluar el poder predictivo del modelo, se llevó a cabo una medición de su exactitud. Además, para un análisis más detallado, se generó una matriz de confusión que desglosa las categorías y se evaluaron también métricas adicionales como precisión, recall, f1-score y support."""
