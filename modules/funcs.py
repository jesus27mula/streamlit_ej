import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os
from PIL import Image



@st.cache_data
def read_csv(path):
    return pd.read_csv(path)

def graficas(df):
    fig = plt.figure()
    sns.countplot(x=df["Sex"], hue=df["Pclass"])
    st.pyplot(fig)

    fig1 = plt.figure()
    sns.barplot(x=df['Pclass'], y=df['Fare'], hue=df['Sex'])
    st.pyplot(fig1)

    fig2 = plt.figure()
    sns.countplot(x=df['Survived'], hue=df['Sex'])
    st.pyplot(fig2)

    fig_bar = px.bar(data_frame=df,
                     x="Pclass",
                     y="Fare",
                     color='Sex',
                     title="Gasto billetes por clase y sexo")
    st.plotly_chart(figure_or_data=fig_bar, use_container_width=True)

    fig_bar2 = px.histogram(data_frame=df,
                            x='Survived',
                            color='Sex',
                            title='Supervivencia por Sexo')
    st.plotly_chart(figure_or_data=fig_bar2, use_container_width=True)

    return [fig, fig1, fig2, fig_bar, fig_bar2]


