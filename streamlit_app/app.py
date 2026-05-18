
import streamlit as st
import pandas as pd

st.title('Spotify Dashboard')


df = pd.read_csv(
    '../exports/analytical_dataset.csv'
)

st.metric(
    'Total canciones',
    len(df)
)

st.metric(
    'Años analizados',
    df['release_year'].nunique()
)

st.dataframe(df.head())

energy_by_year = (
    df.groupby('release_year')['energy']
    .mean()
)

st.line_chart(energy_by_year)