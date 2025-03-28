### Данный сервис предназначен для получения данных о состоянии кошелька сети TRON, его bandwidth, energy и баланс trx.

<details>
<summary>Стек</summary>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3)
</details>
<details>
<summary>Автор</summary>

[avdeevdmitrykrsk](https://github.com/avdeevdmitrykrsk)
</details>

### Сервис готов к запуску локально, для этого установите зависимости из requirements.txt, заполните `.env` файл по примеру из `.env.example`.
### Далее перейдите в корневую папку и выполните команду:
```sh
# Миграции alembic применятся автоматически.
docker-compose up
```

### Для получения информации о кошельке необходимо сделать `POST-запрос` на адрес `/api/wallet_info/`
```sh
# пример post-запроса.
{
    "wallet_id": "TXo4eRamGwY31gNFkDqLRTWWMjRoQ6ZwrRR"
}
# пример ответа.
{
    "wallet_id": "TXo4eRamGwY31gNFkDqLRTWWMjRoQ6ZwrRR",
    "trx_balance": 5,
    "energy_limit": 5,
    "free_net_limit": 5,
    "net_limit": 5,
    "free_net_used": 5,
    "net_used": 5
}
```

### После запроса данные о кошельке сохранятся в БД.

### Для получения списка записей из БД необходимо отправить `GET-запрос` на адрес `/api/wallet_info/` (Доступна пагинация с параметром запроса `?page=<page_number>&size=<records_amount>`)
```sh
# пример ответа.
{
    "items": [
        {
            "wallet_id": "TXo4eRamGwY31gNFkDqLRTWWMjRoQ6ZwrRR",
            "trx_balance": 5,
            "energy_limit": 5,
            "free_net_limit": 5,
            "net_limit": 5,
            "free_net_used": 5,
            "net_used": 5
        }
    ],
    "total": 1,
    "page": 1,
    "size": 50
}
```

### Для запуска тестов из корневой директории выполнить команду 
```sh
pytest
```
