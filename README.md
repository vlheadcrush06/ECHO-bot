# 🗣️Асихронный эхо - бот #
[![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white)](https://www.jetbrains.com/pycharm/)
[![aiogram 3](https://img.shields.io/badge/aiogram-3.x-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://docs.aiogram.dev/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

## Автор: **Владимир**, начинающий _python_ - разработчик ##
### Ссылки на *другие* мои проекты: [ai reviever](https://github.com/vlheadcrush06/ai_reviever-v2-), [ETH - parser](https://github.com/vlheadcrush06/ETH-parser-bot)

**Вопрос - для чего он нужен?**
ОТВЕТ: ***Вы можете проверить:***
1) _Пинг сервера в логах бота_;
2) _Работоспособность сервера_
3) _Скорость отклика запроса_
4) _Устойчивость хостинга_

**Почему стоит выбрать именно _этого_ эхо - бота?**

Причина _1_: _этот_ бот может быть интегрирован в любой код, благодаря своей конструкции;

Причина _2_: **модульность бота** - подразумевается наделение его дополнительными функциями, которые в дальнейшем могут стать _отличным инструментом_ для тестирования сервера или хостинга.

# Как запустить? #
**1)** Для того, чтобы запустить бота, нам необходима среда программирования, например: **VS Code, PyCharm**;
а также **_самое_** главное: **Python v 3.10 +**.

**2)** Далее, перейдя в среду программирования, нам необходимо создать файл `.env` в корневой папке программы.
`.env` файл нам нужен для того, чтобы добавить туда нашего бота.
Пример того, как содержимое файла должно выглядеть:
```
BOT_TOKEN="ВАШ ТОКЕН"
```
Получить токен можно у [@BotFather](https://t.me/BotFather) в **Telegram** (с синей галочкой)

**3)** Следующим шагом нам небоходимо установить зависимости, для этого выполним комманду `pip install -r requirements.txt`  в _терминале_ среды программирования (ctrl + ` (windows/mac)  для VS Code,  alt + f12 (windows) или option + f12 (mac)  для PyCharm).

**4)** Затем запускаем бота коммандой `python main.py`. В терминале появится: `INFO:root:Эхо-бот запущен.`

C этого момента наш бот работаем! пишите ему любое сообщение, и он ответит вам ровно тем, что вы написали.

Приятного ревью =)
