import pandas as pd
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier


# загрузка модели машинного обучения для СППР

def load_model():
    # Загрузка набора данных
    data = pd.read_excel(r'C:\TIP\flet\data_excel.xlsx')

    # Определение целевых и признаковых столбцов
    columns_target = 'Диаметр'
    columns_train = ['Тип орбитальной группировки', 'Частота', 'С\Ш']

    # Подготовка данных
    X = data[columns_train].copy()
    Y = data[columns_target]

    # Кодирование столбца
    X['Тип орбитальной группировки'] = X['Тип орбитальной группировки'].map({'GEO': 0})

    # Инициализация и обучение модели
    base_classifier = DecisionTreeClassifier()
    bagging_classifier = BaggingClassifier(estimator=base_classifier, n_estimators=50, random_state=42)
    bagging_classifier.fit(X, Y)

    return bagging_classifier, columns_train


def predict_diameter(model, feature_columns, freq, orbit, snr):
    """Возвращает строку с обозначением диаметра на основе предсказания модели"""
    user_data = pd.DataFrame([[orbit, freq, snr]], columns=feature_columns)
    # маппинг для всех типов орбит
    user_data['Тип орбитальной группировки'] = user_data['Тип орбитальной группировки'].map(
        {'GEO': 0, 'MEO': 1, 'LEO': 2}
    )

    prediction = model.predict(user_data)

    if prediction[0] == 1:
        return "Диаметр рефлектора: 0.98 м"
    elif prediction[0] == 2:
        return "Диаметр рефлектора: 1.2 м"
    elif prediction[0] == 3:
        return "Диаметр рефлектора: 1.8 м"
    else:
        return "Неизвестный диаметр"
