# areator

> У меня стоит Python 3.12.3.

Склонируйте репозиторий и перейдите в директорию с проектом:
```
git clone https://github.com/shuygena/areator.git
cd areator
```

Создать и активировать виртуальное окружение:  
```
python3 -m venv .venv
source .venv/bin/activate
```

Установить пакет:
```
pip install .
```

Установить editable-версию пакета:
```
pip install -e .
```

Также можно собрать и установить wheel-пакет:
```
pip install wheel setuptools
python setup.py bdist_wheel
pip install dist/*
```

Запустить тесты:
```
pytest .
```