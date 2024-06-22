import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

from sklearn.cluster import KMeans



class Clustering:
    def __init__(self) -> None:
        # Выбор числа кластеров (например, 3)
        self.num_clusters = 3

    def process(self, dataframe: pd.DataFrame):
        # Подготовка данных для кластеризации
        X = dataframe[['time']]

        # Применение K-means
        kmeans = KMeans(n_clusters=self.num_clusters, random_state=0).fit(X)
        dataframe['cluster'] = kmeans.labels_

        # Вывод результатов кластеризации
        return dataframe[['id', 'time', 'cluster']]

    def visualise(self, dataframe):
        # Визуализация кластеров
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='id', y='time', hue='cluster', data=dataframe, palette='Set1')
        plt.title('Кластеры участников по времени ответа')
        plt.xlabel('ID участника')
        plt.ylabel('Время ответа')
        plt.legend(title='Кластер')
        st.pyplot(plt)
