# Опис
Відеопробки з сайту [Videoprobki.ua](http://videoprobki.ua). Обговорення плагіну російською мовою [тут](https://forums.plex.tv/discussion/208066/release-videoprobki-plagin).

# Інсталяція

## Інсталяція через `git`

1. Зайти папку плугінів (правильний шлях див нижче). Для linux `cd /var/lib/plexmediaserver/Resources/Plug-ins or /var/lib/plex/Plex Media Server/Plug-ins`
2. Виконати команду `git clone https://github.com/solvek/videoprobki.bundle.git`
3. Для оновлення плагіна потрібно зайти в папку з плугіном і виконати команду `git pull`

## Інсталяція вручну

1. У вас має бути проінстальований Plex Media Server
2. Скачати архів з плагіном [звідси](https://github.com/solvek/videoprobki.bundle/archive/master.zip)
3. Розпкувати вміст у папку плагінів Plex сервера `Plug-ins` (див нижче)
4. Перейменувати каталог з плагіном з `videoprobki.bundle-master` в `videoprobki.bundle`
5. Додаткова інформація про інсталяцію Plex плугінів вручну
6. Перезапустити Plex Media Server (або комп’ютер)
7. У розділі каналів буде наш плагін

## Місцерозсташування папки Plug-ins
 * на Windows: `C:\Users\USERNAME\AppData\Local\Plex Media Server\Plug-ins`
 * на Mac: `~Library/Application Support/Plex Media Server/Plug-ins`
 * на Linux: `/var/lib/plexmediaserver/Resources/Plug-ins or /var/lib/plex/Plex Media Server/Plug-ins`
 * на FreeBSD `usr/pbi/plexmediaserver-amd64/plexdata/Plex\ Media\ Server/Plug-ins/`

# Програвачі
* Перевірено на [самсунг Plex Player](http://www.samsung.com/levant/smarthub/smartHub/apps_plex.html).
* Працює на андроїді через DLNA з використанням в якості зовнішнього відеоплеєра VLC.
* У мене не програється відео у нативному андроїд клієнті Plex.
* В браузері теж не програється

# Обмеження
* Для кожної камери відео показується в одну хвилину і припиняється. Після цього потрібно запускати цю камеру повторно.
* Перші кілька секунд відео будуть глючними

# Developers info
 * Cameras for city in json: http://videoprobki.com.ua/tmp/mralex/get.php?city=10
 * Request for current stream `curl 'http://videoprobki.ua/gplmod7' -H 'Content-Type: application/x-www-form-urlencoded'  --data 'p1=cam188&p2=2&p3=1&p4=1'`
