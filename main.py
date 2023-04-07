import requests
import json

data = [
  {
    "name": "Иван Иванов",
    "phone_number": "+79201234567",
    "required_amount": 5000,
    "telegram": "@ivan_ivanov",
    "position": "Менеджер по продажам",
    "message": "Нужна срочная финансовая помощь на лечение родственника. Буду очень благодарен за любую помощь."
  },
  {
    "name": "Мария Петрова",
    "phone_number": "+79191234567",
    "required_amount": 10000,
    "telegram": "@maria_petrova",
    "position": "Дизайнер",
    "message": "Мой друг попал в аварию, и ему срочно нужна операция. Помогите пожалуйста, если у вас есть возможность."
  },
  {
    "name": "Александр Сидоров",
    "phone_number": "+79051234567",
    "required_amount": 3000,
    "telegram": "@alex_sidorov",
    "position": "Программист",
    "message": "Моя семья попала в сложную ситуацию из-за потери работы. Любая помощь будет оценена на вес золота."
  },
]

for i in data:
    print(requests.post('http://127.0.0.1:8000/api/board/create/', json=i))