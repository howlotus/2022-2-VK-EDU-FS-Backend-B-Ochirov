# 2022-2-VK-EDU-FS-Backend-B-Ochirov 
## Домашнее задание 2 
- Установить Nginx и Gunicorn

**Проверка установленных пакетов с помощью команд:**

    nginx -v    // проверяем, установлен ли nginx
    -----------
    gunicorn -v // проверяем, установлен ли gunicorn
- Создать папку public/ в корне директории с ДЗ, закинуть туда картиночку, настроить nginx для отдачи статических файлов из папки public/, показать, что картиночку получается открыть на http://localhost:8080/

**Запуск, перезагрузка и отключение nginx на MacOS:**

    launchctl load /usr/local/Cellar/nginx/1.23.1/homebrew.mxcl.nginx.plist
    ------
    nginx -s reload
    ------
    launchctl unload /usr/local/Cellar/nginx/1.23.1/homebrew.mxcl.nginx.plist
**Для проверки работы nginx использовать следующую команду:**

    brew services list
**Настройки для отдачи статических файлов есть в nginx.conf. Проверка работы по следующим ссылкам:**
http://localhost:8080/<some_filename>  <br>
Например: <br>
http://localhost:8080/photo1.jpg

- Создать простейшее WSGI приложение (можно взять с руководства по gunicorn) и запустить его с помощью Gunicorn. Настроить проксирование запросов на nginx на запущенный gunicorn.

**Запуск  WSGI приложения**

    gunicorn --workers=4 app:app
**Проксирование запросов настроено в nginx.conf. Все запросы проксируются по адресу:**
http://127.0.0.1:8080/api/

- Измерить производительность Nginx и Gunicorn c помощью ab или wrk. Добиться отказа системы.

**Осуществим тестирование производительности с помощью wrk:**

    wrk -t 4 -c 5000 http://localhost:8080/cat.gif
    -----
    wrk -t 4 -c 5000 http://localhost:8000
    -----
    wrk -t 4 -c 5000 http://localhost:8080/api