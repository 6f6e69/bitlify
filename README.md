# Bitlify - обрезка ссылок с помощью bit.ly

Программа позволяет сокращать ссылки и получать информацию о количестве переходов
по уже сокращенным ссылкам с помощью сервиса [bit.ly](https://bitly.com/).

## Как установить

Убедитесь что в системе установлен интерпретатор языка Python 3.5+. 
```
python3 --version
```
Рекомендуется использовать [виртуальное окружение](https://docs.python.org/3/library/venv.html).
```
python3 -m venv env
source env/bin/activate # Unix-based
.\venv\Scripts\activate # Windows
```

Скачайте [архив](https://github.com/6f6e69/bitlify/archive/refs/heads/main.zip) с файлами проекта и разархивируйте в рабочую директорию.

Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей. 
```
pip install -r requirements.txt
```

Получите API-ключ.
- Зарегистрируйтесь в сервисе [bit.ly](https://bitly.com/)
- Сгенерируйте ключ в [профиле](https://app.bitly.com/settings/api/)

Разместите API-ключ в файл переменных среды.
- Создайте в рабочей директории файл `.env'
- Запишите переменную `BITLY_API_KEY` в .env файл
```
BITLY_API_KEY='полученный ключ'
```

## Использование

### Сокращение ссылки
```
$python3 bitlify.py --link 'https://www.linux.org.ru/`
Bitlink https://bit.ly/3Rqwl1t
```

### Количество переходов по ссылке
```
$python3 bitlify.py --link 'https://bit.ly/3Rqwl1t'
Clicks count 2
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).