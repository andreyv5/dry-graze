from enum import Enum

import streamlit as st
import pandas as pd


class MethodOptions(Enum):
    LEMMA = "Aнализ лексических характеристик"
    CLUSTER = "Кластерный анализ"
    REGGRESSION = "Регрессионный анализ"
    OUTLIER = "Анализ выбросов"
    T_TEST = "T тест"


@st.cache_data
def load_array_table(id_survey: int):
    path = "/Users/macbook/habr/calculus/scaffolding/array.csv"
    columns = ["id", "first_word", "second_word", "name", "age", "floor", "time", "id_survey", "date"]

    array = pd.read_csv(path)
    array.columns = columns
    array.dropna(inplace=True)
    return array.loc[array['id_survey'] == id_survey]


st.title("Расчет данных")

id_survey = st.number_input(
    label="Введите survey id",
    min_value=87,
    max_value=33710,
    value=12345
)

method = st.selectbox(
    label="Что Вы бы хотели посчитать",
    options=(
        MethodOptions.LEMMA.value,
        MethodOptions.CLUSTER.value,
        MethodOptions.REGGRESSION.value,
        MethodOptions.OUTLIER.value,
        MethodOptions.T_TEST.value
    )
)

if st.button('Посчитать'):
    to_process = dataframe=load_array_table(id_survey=id_survey)
        
    if to_process.shape[0] == 0:
        st.toast("С таким survey id данных для анализа нет")
        st.stop()
    else:
        st.info("Оригинальная выборка")
        st.dataframe(data=to_process)

    if method == MethodOptions.LEMMA.value:
        from module.lemmatizer import Lemmatizer

        with st.spinner('Подсчет может занять несколько минут ...'):
            df, df_diff, word1_diff, words2_diff = Lemmatizer().process(dataframe=to_process[:200])    
            st.info("Таблица лемматизированных слов")
            st.dataframe(data=df, use_container_width=True)
            st.info("Таблица лемматизированных слов разница")
            st.dataframe(data=df, use_container_width=True)
            st.info("Подсчит значений True")
            st.text(f"Количество значений True для first_word_diff: {word1_diff}")
            st.text(f"Количество значений True для second_word_diff: {words2_diff}")
            Lemmatizer().visualise(dataframe=df_diff)
        st.success('Посчитано')
    
    elif method == MethodOptions.CLUSTER.value:
        from module.clusterisation import Clustering

        with st.spinner('Подсчет может занять несколько минут ...'):
            df = Clustering().process(dataframe=to_process)    
            st.info("Таблица результатов кластеризации")
            st.dataframe(data=df, use_container_width=True)
            Clustering().visualise(dataframe=df)
        st.success('Посчитано')
        
    elif method == MethodOptions.REGGRESSION.value:
        from module.regression import Regression

        with st.spinner('Подсчет может занять несколько минут ...'):
            df = Regression().process(dataframe=to_process)    
            st.info("Таблица с фактическими и предсказанными значениями времени ответа")
            st.dataframe(data=df, use_container_width=True)
        st.success('Посчитано')
    
    elif method == MethodOptions.OUTLIER.value:
        from module.outlier import Outlier

        with st.spinner('Подсчет может занять несколько минут ...'):
            df = Outlier().process(dataframe=to_process)    
            st.info("Таблица с результатами анализа выбросов")
            st.dataframe(data=df, use_container_width=True)
            Outlier().visualise(dataframe=df)
        st.success('Посчитано')

    elif method == MethodOptions.T_TEST.value:
        from module.t_test import TTest

        with st.spinner('Подсчет может занять несколько минут ...'):
            df = TTest().process(dataframe=to_process)
            st.info("Результаты t-теста между возрастными группами")
            st.dataframe(data=df, use_container_width=True)
        st.success('Посчитано')
        

