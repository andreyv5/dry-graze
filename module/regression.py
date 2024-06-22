import pandas as pd
import seaborn as sns
import matplotlib as plt
import streamlit as st
import statsmodels.api as sm


class Regression:
    def __init__(self) -> None:
        self.results = None

    def process(self, dataframe: pd.DataFrame):
        # Преобразование категориальных переменных
        dataframe['floor'] = dataframe['floor'].map({'Мужской': 0, 'Женский': 1})

        # Подготовка данных для регрессионного анализа
        X = dataframe[['age', 'floor']]
        X = sm.add_constant(X)  # Добавляем константу
        y = dataframe['time']

        # Построение регрессионной модели
        model = sm.OLS(y, X).fit()

        self.results = model
        # Предсказание значений времени ответа
        dataframe['predicted_time'] = model.predict(X)

        # Вывод таблицы с фактическими и предсказанными значениями времени ответа
        return dataframe[['id', 'time', 'predicted_time']]
