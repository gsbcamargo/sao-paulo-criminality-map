# import libs

import streamlit as st
import pandas as pd
import pydeck as pdk

# load data
df = pd.read_csv('criminalidade_sp_2.csv')

# dashboard

st.title('Metropolitan Region of São Paulo Criminality Data')
st.markdown(
    """
    PT \n
    A criminalidade é um problema recorrente no Brasil. 
    Buscamos sempre formas de diminuir esses índices e 
    usando técnicas de Ciências de Dados 
    conseguimos entender melhor o que está acontecendo e 
    gerar insights que direcionem ações capazes 
    de diminuir os índices de criminalidade.
    
    EN \n
    Criminality is a known issue in Brazil.
    We're always looking for methods that are able to decrease
    those rates and, by using Data Science techniques, 
    we aim to better understand what is going on, creating
    insights that head to actions capable of 
    having a positive effect on São Paulo's criminality rate.
    """
)

# sidebar
st.sidebar.info('{} lines loaded.'.format(df.shape[0]))

if st.sidebar.checkbox('Show data table'):
    st.header('Raw Data')
    st.write(df)

df.time = pd.to_datetime(df.time)
selected_year = st.sidebar.slider('Please select a year', 2010, 2018, 2015)
df_selected = df[df.time.dt.year == selected_year]

st.map(df_selected)
# map
st.subheader('Criminality Map')
# st.map(df)
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=-23.567145	,
        longitude=-46.648936,
        zoom=8,
        pitch=50
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=df_selected[['latitude', 'longitude']],
            get_position='[longitude,latitude]',
            auto_highlight=True,
            elevation_scale=50,
            pickable=True,
            elevation_range=[0, 3000],
            extruded=True,
            coverage=1
        )
    ],
))
