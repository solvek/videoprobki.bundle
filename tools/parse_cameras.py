import os
from lxml import etree
from io import StringIO
import codecs

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

filename = __location__ + "/html/allcameras.html"

file = codecs.open(filename, 'r', 'utf-8')

content = file.read()
file.close()

parser =etree.HTMLParser()

page = etree.parse(StringIO(content), parser).getroot()

cameras = page.xpath('//div[contains(@class, "pane")]/table//tr/td/table')

print("Found %s cameras" % len(cameras))

for camera in cameras:
    rows = camera.xpath('.//tr')
    # print("%s rows" % len(rows))

    url = rows[1].xpath('.//a')[0].get('href')

    print('Url: %s' % url)
