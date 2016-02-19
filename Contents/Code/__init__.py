TITLE = 'Videoprobki'
WEB_PAGE = 'http://videoprobki.ua'
ART    = 'art-default.jpg'
ICON   = 'icon-default.png'

PREFIX = '/video/videoprobki'

BASE_URL = 'http://mobile.videoprobki.ua%s'

PARSED = 'parsed'

################################################
def Start():

	ObjectContainer.title1 = TITLE
	ObjectContainer.art = R(ART)
	DirectoryObject.art = R(ART)
	DirectoryObject.thumb = R(ICON)

	Data.Remove(PARSED)

	Dict['city'] = None

#################################################
@handler(PREFIX, TITLE)
@route(PREFIX+'/cities/city')
def MainMenu():
	currentCity = Dict['city']

	# Log.Debug('Current city: '+currentCity)

	if not currentCity:
		return MenuCities()

	oc = MenuCity(currentCity)

	oc.add(DirectoryObject(
		            key = Callback(MenuCities),
		            title = L("Select city")
		        ))

	return oc

################################################
@route(PREFIX+'/cities')
def MenuCities():
	oc = ObjectContainer()

	for cityName in GetContent().keys():
		# cityName = cityName.decode()
		# Log.Debug('Listing cities, city: '+cityName)
		oc.add(DirectoryObject(
		            key = Callback(MenuCity, city = cityName),
		            title = cityName
		        ))

	return oc

################################################
@route(PREFIX+'/cities/{city}')
def MenuCity(city='dddd'):
	Log.Debug("Menu for city "+city)
	Dict['city'] = city

	if city == 'Київ':
		return CityDistricts(city)

	return CityCameras(city)

################################################
@route(PREFIX+'/cities/{city}/{district}')
def MenuDistrict(city, district):
	oc = ObjectContainer()

	district = GetContent().get(city).get(district)

	AppendDistrict(oc, district)

	return oc

################################################
@route(PREFIX+'/exact/{city}/districts')
def CityDistricts(city):
	oc = ObjectContainer()

	districts = GetContent().get(city)

	# Log.Debug('For city %s, districts: %s' % (city, JSON.StringFromObject(districts)))

	for districtName in districts.keys():
		oc.add(DirectoryObject(
		            key = Callback(MenuDistrict, city=city, district = districtName),
		            title = districtName
		        ))

	return oc

################################################
@route(PREFIX+'/exact/{city}/cameras')
def CityCameras(city):
	oc = ObjectContainer()

	districts = GetContent().get(city)
	for district in districts.values():
		AppendDistrict(oc, district)

	return oc

################################################
def AppendDistrict(oc, district):
	if not district:
		return

	for camera in district:
		Log.Debug('Camera url: %s' % camera.get('url'))
		oc.add(VideoClipObject(
			url = camera.get('url'),
			title = camera.get('place')+" "+camera.get('direction'),
			summary = camera.get('city')+", "+camera.get('district')
		))

################################################
def GetContent():
	if Data.Exists(PARSED):
		return Data.LoadObject(PARSED)

	parsed = {}

	content = HTML.ElementFromURL(BASE_URL % '/uk/all-cameras', encoding='utf-8')

	for camera in content.xpath('//div[contains(@class, "cam-info")]/div[2]'):
		url = BASE_URL % camera.xpath('.//a')[0].get('href')

		parts = [extractValue(part) for part in HTML.StringFromElement(camera).decode().split('<br>')]

		city = parts[0]
		district = parts[1]
		place = parts[2]
		direction = parts[3]

		# Log.Debug('Url: %s, city: "%s", district: %s, place: %s, direction: %s' % (url, city, district, place, direction))

		cityItems = parsed.get(city)

		if not cityItems:
			cityItems = {}
			parsed[city] = cityItems

		districtItems = cityItems.get(district)

		if not districtItems:
			districtItems = []
			cityItems[district] = districtItems

		districtItems.append({
		                     'city': city,
		                     'district': district,
		                     'place':place,
		                     'direction':direction,
		                     'url':url})

	Data.SaveObject(PARSED, parsed)

	# Log.Debug('Whole content %s' % JSON.StringFromObject(parsed))

	return parsed

def extractValue(s):
	s = String.StripTags(s)
	f = s.find(': ')
	return s[f+2:].strip()

################################################
# def Thumb(url):

#   try:
#     data = HTTP.Request(url, cacheTime = CACHE_1MONTH).content
#     return DataObject(data, 'image/jpeg')
#   except:
#     return Redirect(R(ICON))
