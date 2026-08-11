import numpy as np
import streamlit as st
import pandas as pd

from sklearn.datasets import load_iris
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier

st.write(''' # Tipos de Flor Iris ''')
st.image("Flor Iris Purpura.webp", caption="Clasificacion de algunos tipos de Flor Iris")

st.header('Datos de evaluación')

def user_input_features():
  # Entrada
  sepal_length_cm = st.number_input('Longitud del Sépalo:', min_value=0.0, max_value=5.0, value = 1.0, step = 0.1)
  sepal_width_cm = st.number_input('Ancho del Sépalo:', min_value=0.0, max_value=5.0, value = 0.0, step = 0.1)
  petal_length_cm = st.number_input('Longitud del Pétalo:', min_value=0.0, max_value=7.0, value = 0.0, step = 0.1)
  petal_width_cm = st.number_input('Ancho del Pétalo:',min_value=0.0, max_value=3.0, value = 0.0, step = 0.1)
  
  user_data_input = {'sepal_length_cm': sepal_length_cm,
                     'sepal_width_cm': sepal_width_cm,
                     'petal_length_cm': petal_length_cm,
                     'petal_width_cm': petal_width_cm}

  features = pd.DataFrame(user_data_input, index=[0])

  return features

df = user_input_features()

iris = load_iris()

classifier = DecisionTreeClassifier(max_depth=8, criterion='entropy', min_samples_leaf=10, max_features=7, random_state=0)
classifier.fit(X, Y)

prediction = classifier.predict(df)

st.subheader('Clasificación de la Flor Iris')
if prediction == 0:
  st.write('El tipo de Flor es Setosa')
elif prediction == 1:
  st.write('El tipo de Flor es Versicolor')
else:
  st.write('El tipo de Flor es Virginica')
