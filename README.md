Благодаря этому проекту реализована возможность преобразования любого текста пользователя в аудио сообщение, на основе Telegram Бота

В виртуальном окружении отдельно создается папка DATA , в которой будет хранится файл * .mp3 входящего сообщения. Затем , благодаря (module) subprocess * .mp3 конвертируется в файл с расширением * . ogg ,который поддерживается в Telegram.

Был применен модуль Logging . (Журнал процессов)
Записывая полезные данные из нужных мест, вы можете не только легко отлаживать ошибки, но и использовать данные для анализа производительности приложения.

*** В созданном файле setting.py хранится API ключ Telegram Бота