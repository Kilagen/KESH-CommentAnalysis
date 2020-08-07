"""
    Задача этого модуля -- обучение модели
"""
from sklearn.metrics import classification_report


def evaluation_model(mas, y_pred):
    """Здесь будет ваша модель"""
    y_true = []
    for i in mas:
        y_true.append(i[1])
    target_names = ['class 0 (positive)', 'class 1 (negative)', 'class 2 (neutral)']
    print(classification_report(y_true, y_pred, target_names=target_names))


# 0 - positive
# 1 - negative
# 2 - neutral
#mas = [('Ужасный товар!', 1), ('Рекомендую. Все супер!', 0), ('Здесь продают столы', 2)]
#evaluation_model(mas, y_pred)
