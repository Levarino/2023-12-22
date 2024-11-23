
## Requests позволяет очень легко отправлять запросы по протоколу HTTP/

import requests

# URL для поиска репозиториев на GitHub
url = "https://api.github.com/search/repositories"

# Параметры запроса
params = {
    'q': 'language:Python',  # Поиск по языку Python
    'sort': 'stars',  # Сортировка по звёздам
    'order': 'desc'  # Порядок - по убыванию
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Проверка статуса ответа
if response.status_code == 200:
    # Преобразование ответа в JSON
    data = response.json()
    # Вывод названий репозиториев
    for repo in data['items']:
        print(repo['name'], repo['html_url'])
else:
    print("Ошибка:", response.status_code)
print()


## Matplotlib — это обширная библиотека для создания статичных, анимированных и интерактивных визуализаций.
## Она предоставляет множество функций для построения графиков и диаграмм.

## NumPy — это библиотека для работы с массивами и матрицами.

import numpy as np
import matplotlib.pyplot as plt

# Создание массива данных
data = np.array([10, 15, 7, 20, 5, 12, 8, 10, 15, 25])

# Вычисление основных статистических показателей
mean = np.mean(data)  # Среднее
median = np.median(data)  # Медиана
std_dev = np.std(data)  # Стандартное отклонение

# Вывод результатов
print(f"Среднее: {mean}")
print(f"Медиана: {median}")
print(f"Стандартное отклонение: {std_dev}")

# Визуализация данных
plt.hist(data, bins=5, color='blue', alpha=0.7)
plt.title('Гистограмма данных')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.axvline(mean, color='red', linestyle='dashed', linewidth=1, label='Среднее')
plt.axvline(median, color='green', linestyle='dashed', linewidth=1, label='Медиана')
plt.legend()
plt.show()
