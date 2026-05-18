
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



st.title('Spotify Dashboard')



df = pd.read_csv(
    '../exports/analytical_dataset.csv'
)

st.header('Métricas Principales')
col1, col2 = st.columns(2)
with col1:
    st.metric(
        'Total canciones',
        len(df)
    )
with col2:
    st.metric(
        'Años analizados',
        df['release_year'].nunique()
    )

st.header('Vista Previa de los Datos')
st.dataframe(df.head())

st.header('Visualizaciones del Notebook')

# Gráfico 1: Energía a lo largo del tiempo
# Pregunta: ¿Cómo ha evolucionado la energía promedio de las canciones a lo largo de los años?
st.subheader('Energía de las canciones a lo largo del tiempo')
energy_by_year = (
    df.groupby('release_year')['energy']
    .mean()
    .reset_index()
)
fig_energy = px.line(
    energy_by_year,
    x='release_year',
    y='energy',
    title='Evolución de la Energía Promedio por Año',
    labels={
        'release_year': 'Año de Lanzamiento',
        'energy': 'Energía Promedio'
    }
)
st.plotly_chart(fig_energy, use_container_width=True)

# Gráfico 2: Popularidad vs Bailabilidad (Interactivo)
# Pregunta: ¿Existe una relación entre la "bailabilidad" y la popularidad de una canción?
st.subheader('Popularidad vs. Bailabilidad (Interactivo)')
fig_interactive = px.scatter(
    df,
    x='danceability',
    y='popularity',
    hover_data=['track_name', 'artist_name'],
    title='Popularidad vs. Bailabilidad',
    labels={
        'danceability': 'Bailabilidad',
        'popularity': 'Popularidad',
        'track_name': 'Canción',
        'artist_name': 'Artista'
    }
)
st.plotly_chart(fig_interactive, use_container_width=True)

# Pregunta: ¿Qué variables numéricas están correlacionadas entre sí?
# Gráfico 3: Matriz de Correlación
st.subheader('Mapa de Calor de Correlación')
corr_cols = ['popularity', 'danceability', 'energy', 'valence', 'tempo']
corr_df = df[corr_cols].rename(columns={
    'popularity': 'Popularidad',
    'danceability': 'Bailabilidad',
    'energy': 'Energía',
    'valence': 'Valencia',
    'tempo': 'Tempo'
})
corr = corr_df.corr()

fig_corr, ax_corr = plt.subplots(figsize=(10, 8))
sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    ax=ax_corr
)
ax_corr.set_title('Matriz de Correlación')
st.pyplot(fig_corr)

# Pregunta: ¿Cuál es la distribución de popularidad de las canciones?
# Gráfico 4: Distribución de la Popularidad
st.subheader('Distribución de la Popularidad de las Canciones')
fig_hist = px.histogram(
    df,
    x='popularity',
    nbins=50,
    title='Distribución de la Popularidad',
    labels={
        'popularity': 'Popularidad',
        'count': 'Cantidad de Canciones'
    }
)
st.plotly_chart(fig_hist, use_container_width=True)