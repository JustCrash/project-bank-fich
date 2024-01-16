# project-bank-fich
IT-отдел крупного банка делает новую фичу для личного кабинета клиента. 
Это виджет, который показывает несколько последних успешных банковских операций клиента. 
Вам доверили реализовать алгоритм, который на бэкенде будет готовить данные для отображения в новом виджете.

По каждой операции есть следующие данные:

- `id` — id транзакциии
- `date` — информация о дате совершения операции
- `state` — статус перевода:
    - `EXECUTED`  — выполнена,
    - `CANCELED`  — отменена.
- `operationAmount` — сумма операции и валюта
- `description` — описание типа перевода
- `from` — откуда (может отсутстовать)
- `to` — куда

Для запуска проекта требуются.
Создать и активировать виртуальное окружение:
-poetry init
Установка зависимостей:
-poetry install
