import pandas as pd
from scipy.stats import ttest_ind


class TTest:
    def process(self, dataframe: pd.DataFrame):
        # Создание возрастных групп
        dataframe['age_group'] = pd.cut(dataframe['age'], bins=[20, 22, 24, 26, 28], labels=['20-22', '22-24', '24-26', '26-28'])

        # Группировка данных по возрастным группам
        group_20_22 = dataframe[dataframe['age_group'] == '20-22']['time']
        group_22_24 = dataframe[dataframe['age_group'] == '22-24']['time']
        group_24_26 = dataframe[dataframe['age_group'] == '24-26']['time']
        group_26_28 = dataframe[dataframe['age_group'] == '26-28']['time']

        # T-тест между возрастными группами
        t_stat_20_22_22_24, p_val_20_22_22_24 = ttest_ind(group_20_22, group_22_24, equal_var=False)
        t_stat_22_24_24_26, p_val_22_24_24_26 = ttest_ind(group_22_24, group_24_26, equal_var=False)
        t_stat_24_26_26_28, p_val_24_26_26_28 = ttest_ind(group_24_26, group_26_28, equal_var=False)

        # Создание таблицы с результатами t-теста
        t_test_results = pd.DataFrame({
            'Group Comparison': ['20-22 vs 22-24', '22-24 vs 24-26', '24-26 vs 26-28'],
            't-statistic': [t_stat_20_22_22_24, t_stat_22_24_24_26, t_stat_24_26_26_28],
            'p-value': [p_val_20_22_22_24, p_val_22_24_24_26, p_val_24_26_26_28]
        })
        return t_test_results
