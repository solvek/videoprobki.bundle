TITLE = 'Videoprobki'
WEB_PAGE = 'http://videoprobki.ua'
ART    = 'art-default.jpg'
ICON   = 'icon-default.png'

PREFIX = '/video/videoprobki'

####################################################################################################
def Start():

	ObjectContainer.title1 = TITLE
	ObjectContainer.art = R(ART)
	DirectoryObject.art = R(ART)
	DirectoryObject.thumb = R(ICON)

####################################################################################################
@handler(PREFIX, TITLE)
def MainMenu():

	oc = ObjectContainer()

	oc.add(VideoClipObject(
		url = 'http://videoprobki.ua/uk/camera/188-rozvyazka-prosp-bazhana-%D1%96-dn%D1%96provsko%D1%97-nab-metro-osokorki?c=Kyiiv',
		# url = 'http://vs7.videoprobki.com.ua/streams/cam188stream_1455527504.mp4',
		title = 'Osokorky',
		summary = 'Some summary',
		thumb = Callback(Thumb, url='http://maps.googleapis.com/maps/api/staticmap?center=50.3952,30.6184&zoom=15&size=300x150&markers=icon:http://videoprobki.ua/themes/videoprobki/images/icons/green_45_active.gif|50.3952,30.6184&sensor=true&language=uk')
	))

	return oc

####################################################################################################
def Thumb(url):

  try:
    data = HTTP.Request(url, cacheTime = CACHE_1MONTH).content
    return DataObject(data, 'image/jpeg')
  except:
    return Redirect(R(ICON))
