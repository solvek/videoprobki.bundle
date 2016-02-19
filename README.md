# Опис
Відеопробки з сайту [Videoprobki.ua](http://videoprobki.ua)

# Інсталяція

1. У вас має бути проінстальований Plex Media Server
2. Скачати архів з плагіном [звідси](https://github.com/solvek/videoprobki.bundle/archive/master.zip)
3. Розпкувати вміст у папку плагінів Plex сервера. Вона знаходиться за одним із шляхів
3.1. на Windows: `C:\Users\USERNAME\AppData\Local\Plex Media Server\Plug-ins`
3.2. на Mac: `~Library/Application Support/Plex Media Server/Plug-ins`
3.3. на Linux: `/usr/lib/plexmediaserver/Resources/Plug-ins or /var/lib/plex/Plex Media Server/Plug-ins`
3.4. на FreeBSD `usr/pbi/plexmediaserver-amd64/plexdata/Plex\ Media\ Server/Plug-ins/`
4. Перейменувати каталог з плагіном з `videoprobki.bundle-master` в `videoprobki.bundle`
5. Додаткова інформація про інсталяцію Plex плугінів вручну
6. Перезапустити Plex Media Server (або комп’ютер)
7. У розділі каналів буде наш плагін

# Програвачі
* Перевірено на [самсунг Plex Player](http://www.samsung.com/levant/smarthub/smartHub/apps_plex.html).
* Працює на андроїді через DLNA з використанням в якості зовнішнього відеоплеєра VLC.
* У мене не програється відео у нативному андроїд клієнті Plex.

# Обмеження
* Для кожної камери відео показується в одну хвилину і припиняється. Після цього потрібно запускати цю камеру повторно.
* Перші кілька секунд відео будуть глючними

# Developers info
 * Cameras for city in json: http://videoprobki.com.ua/tmp/mralex/get.php?city=10
 * Request for current stream `curl 'http://videoprobki.ua/gplmod7' -H 'Content-Type: application/x-www-form-urlencoded'  --data 'p1=cam188&p2=2&p3=1&p4=1'`
