import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from spacy_download import load_spacy


class Lemmatizer:
    def __init__(self) -> None:
        self.model = load_spacy("ru_core_news_sm")

    def lemmatize(self, word):
        doc = self.model(word)
        return " ".join([token.lemma_ for token in doc])

    def process(self, dataframe: pd.DataFrame):
        dataframe['first_word_lemma'] = dataframe['first_word'].apply(self.lemmatize)
        dataframe['second_word_lemma'] = dataframe['second_word'].apply(self.lemmatize)

        # Проверка различий между исходным словом и леммой
        dataframe['first_word_diff'] = dataframe['first_word'] != dataframe['first_word_lemma']
        dataframe['second_word_diff'] = dataframe['second_word'] != dataframe['second_word_lemma']

        # Подсчет процентов различий
        first_word_diff_percent = dataframe['first_word_diff'].mean() * 100
        second_word_diff_percent = dataframe['second_word_diff'].mean() * 100

        # Подсчет количества значений True
        first_word_diff_count = dataframe['first_word_diff'].sum()
        second_word_diff_count = dataframe['second_word_diff'].sum()

        # Применение лемматизации к словам
        dataframe['first_word_lemma'] = dataframe['first_word'].apply(self.lemmatize)
        dataframe['second_word_lemma'] = dataframe['second_word'].apply(self.lemmatize)

        # # Проверка различий между исходным словом и леммой
        dataframe['first_word_diff'] = dataframe['first_word'] != dataframe['first_word_lemma']
        dataframe['second_word_diff'] = dataframe['second_word'] != dataframe['second_word_lemma']

        # # Подсчет процентов различий
        first_word_diff_percent = dataframe['first_word_diff'].mean() * 100
        second_word_diff_percent = dataframe['second_word_diff'].mean() * 100

        # # Подсчет количества значений True
        first_word_diff_count = dataframe['first_word_diff'].sum()
        second_word_diff_count = dataframe['second_word_diff'].sum()

        # результат в виде таблицы
        result = dataframe[
            ['first_word', 'first_word_lemma', 'second_word', 'second_word_lemma', 'first_word_diff', 'second_word_diff']
        ]

        # процентов различий
        difference = pd.DataFrame(
            {
                'type': ['First Word', 'Second Word'],
                'percent_diff': [first_word_diff_percent, second_word_diff_percent],
                'count_true': [first_word_diff_count, second_word_diff_count]
            }
        )
        return result, difference, first_word_diff_count, second_word_diff_count

    def visualise(self, dataframe):
        plt.figure(figsize=(10, 6))
        sns.barplot(data=dataframe, x='type', y='percent_diff')
        plt.title('Процент различий между исходным словом и леммой')
        plt.xlabel('Тип слова')
        plt.ylabel('Процент различий (%)')
        plt.ylim(0, 100)
        st.pyplot(plt)
