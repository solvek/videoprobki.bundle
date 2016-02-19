import re

CAMID = re.compile('/camera/(?P<id>\d+)-')

if CAMID.match('http://videoprobki.ua/uk/camera/2-moskovskii-prospekt-16?c=Kyiiv'):
    print ('Yes!')
else:
    print('No')
