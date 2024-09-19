import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from modules.funcs import *


def main():

    choices = ['Titanic', 'Gráficos', 'Explicación']
    choice = st.sidebar.selectbox(label='Menú', options=choices, index=0)

    if choice == 'Titanic':

        st.title('Base de datos de pasajeros del Titanic')
        st.text('A través de esta plataforma podremos filtrar los datos para conocer más '
                'las características de la población de este barco')

        path = 'sources/titanic.csv'
        df = read_csv(path)

        # Seleccionador de filtros del df

        sex = ['male', 'female']
        choice = st.multiselect(label="Sexo",
                                options=sex,
                                default=sex,
                                placeholder="Placeholder", )

        df = df[df['Sex'].isin(choice)]

        clases = [1, 2, 3]
        clase = st.multiselect(label="Clase",
                               options=clases,
                               default=clases,
                               placeholder="Placeholder", )

        min_age = st.slider(label="Edad Mínima",
                            min_value=0,
                            max_value=80,
                            value=0,
                            step=1)

        max_age = st.slider(label="Edad Máxima",
                            min_value=0,
                            max_value=80,
                            value=80,
                            step=1)

        df = df[(df['Pclass'].isin(clase)) & (df['Age'].between(min_age, max_age))]

        sourvivre = [0, 1]
        choices1 = st.multiselect(label="Supervivencia",
                                  options=sourvivre,
                                  default=sourvivre,
                                  placeholder="Placeholder", )
        df = df[df['Survived'].isin(choices1)]

        nombre = st.text_area(label="Enter Text",
                              height=50,
                              max_chars=1000,
                              placeholder="Review")
        df = df[df['Name'].str.contains(nombre)]

        st.dataframe(df)

    elif choice == 'Gráficos':
        path = 'sources/titanic.csv'
        df = read_csv(path)

        # Seleccionador de filtros del df

        sex = ['male', 'female']
        choice = st.multiselect(label="Sexo",
                                options=sex,
                                default=sex,
                                placeholder="Placeholder", )

        df = df[df['Sex'].isin(choice)]

        clases = [1, 2, 3]
        clase = st.multiselect(label="Clase",
                               options=clases,
                               default=clases,
                               placeholder="Placeholder", )

        min_age = st.slider(label="Edad Mínima",
                            min_value=0,
                            max_value=80,
                            value=0,
                            step=1)

        max_age = st.slider(label="Edad Máxima",
                            min_value=0,
                            max_value=80,
                            value=80,
                            step=1)

        df = df[(df['Pclass'].isin(clase)) & (df['Age'].between(min_age, max_age))]

        sourvivre = [0, 1]
        choices1 = st.multiselect(label="Supervivencia",
                                  options=sourvivre,
                                  default=sourvivre,
                                  placeholder="Placeholder", )
        df = df[df['Survived'].isin(choices1)]

        nombre = st.text_area(label="Enter Text",
                              height=50,
                              max_chars=1000,
                              placeholder="Review")
        df = df[df['Name'].str.contains(nombre)]

        st.dataframe(df)

        graficas(df)

    else:
        st.title('Explicación')
        st.markdown('En esta app. web hemos creado tres opciones con los cuales el usuario puede selecionar'
                    'la base de datos de la que partimos, en este caso partimos de los datos obtenidos del registro de'
                    'viajeros del Titanic. La segunda opción se trata de unas gráficas y estadísticas sobre el viaje.'
                    'Y la tercera opción es una explicación.')
        st.markdown('El barco salió en el año x y fue construido en el puerto de Belfast')
        st.image(image='sources/img1.jpg',
                 caption='Imagen del Titanic',
                 use_column_width=True)
        st.markdown('En medio del océano atlántico a x días de llegar a New York se topó con un inceberg')
        st.image(
            image='sources/img2.png',
            caption='Imagen del Titanic',
            use_column_width=True)
        st.image(
            image='sources/img3.jpg',
            caption='Imagen del Titanic',
            use_column_width=True)

if __name__ == "__main__":
    main()