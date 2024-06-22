import re

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


class Outlier:
    # Функция для проверки времени ответа
    def detect_time_outliers(self, df):
        outliers = df[(df['time'] < 2) | (df['time'] > 60)]
        return outliers

    # Функция для проверки символов в second_word
    def detect_invalid_characters(self, df):
        pattern = re.compile(r'[^а-яА-Я ]')
        invalid_chars = df[df['second_word'].apply(lambda x: bool(pattern.search(x)))]
        return invalid_chars

    def process(self, dataframe: pd.DataFrame):
        # Обнаружение выбросов по времени
        time_outliers = self.detect_time_outliers(dataframe)

        # Обнаружение неправильных символов в second_word
        invalid_chars = self.detect_invalid_characters(dataframe)

        # Объединение результатов
        return pd.concat([time_outliers, invalid_chars]).drop_duplicates().reset_index(drop=True)

    def visualise(self, dataframe):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(dataframe['id'], dataframe['time'], color='red', label='Time Outliers')
        ax.set_xlabel('ID')
        ax.set_ylabel('Time')
        ax.set_title('Time Outliers')
        ax.legend()
        st.pyplot(plt)
