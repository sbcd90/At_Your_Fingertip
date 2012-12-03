import cgi
import json
from google.appengine.api import urlfetch
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Mainpage(webapp.RequestHandler):
	def get(self):
		self.response.out.write("""<html><body bgcolor="#E6E6FA"><h1 align="center">At Your Fingertip</h1><form action="/display" method ="post"><div align="center"><textarea name="search_engine" rows="1" cols="60"></textarea></div><div align="center"><input type="submit" value="Search"></div></form></body></html>""")
class SearchResult(webapp.RequestHandler):
	def post(self):
		search_string=self.request.get('search_engine')
		listing1=list(str(search_string))
		count1=0
		while(count1<len(listing1)):
			if listing1[count1]==' ':
				listing1[count1]='+'
			count1=count1+1	
		search_string="".join(listing1)				
		# api key to come in place of *
		url="https://maps.googleapis.com/maps/api/place/textsearch/json?query="+search_string+"&sensor=true&key=**********" 
		response=urlfetch.fetch(url)
		if response.status_code==200:
			decodedresponse=json.loads(response.content)
			count=0
			for part in decodedresponse['results']:
				for part1 in part['geometry']['location']:
					if count==0:
						a=part['geometry']['location']['lat']
						b=part['geometry']['location']['lng']
						a1=part['name']
					if count==2:
						c=part['geometry']['location']['lat']
						d=part['geometry']['location']['lng']
						c1=part['name']
					if count==4:
						e=part['geometry']['location']['lat']	
						f=part['geometry']['location']['lng']
						e1=part['name']
					if count==6:
						g=part['geometry']['location']['lat']
						h=part['geometry']['location']['lng']
						g1=part['name']
					if count==8:
						i=part['geometry']['location']['lat']
						j=part['geometry']['location']['lng']
						i1=part['name']		
#					mymap="""<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="content-type" content="text/html; charset=utf-8"/><title>Google Maps JavaScript API Example</title><script src="http://maps.google.com/maps?file=api&amp;v=2&amp;key=&sensor=true"type="text/javascript"></script><script type="text/javascript">function initialize() {if (GBrowserIsCompatible()) {var map = new GMap2(document.getElementById("map_canvas"));map.setCenter(new GLatLng("""+str(part['geometry']['location']['lat'])+""", """+str(part['geometry']['location']['lng'])+"""), 13);map.setUIToDefault();for (var i = 0; i < 10; i++) {var point = new GLatLng("""+str(part['geometry']['location']['lat'])+""","""+str(part['geometry']['location']['lng'])+""");map.addOverlay(new GMarker(point));}}}</script></head><body onload="initialize()" onunload="GUnload()"><div id="map_canvas" style="width: 500px; height: 300px"></div></body></html>"""
#					self.response.out.write(mymap)
					count=count+1
					if count==9:
						break
				if count==9:
					break					
				#api key to come in place of *
			mymap="""<!DOCTYPE html><html><head><meta name="viewport" content="initial-scale=1.0, user-scalable=no" /><style type="text/css">html { height: 100% }body { height: 100%; margin: 0; padding: 0 }#map_canvas { height: 100% }</style><script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=**********&sensor=true"></script><script type="text/javascript">function initialize() {var mapOptions = {center: new google.maps.LatLng("""+str(a)+""","""+str(b)+"""),zoom: 12,mapTypeId: google.maps.MapTypeId.ROADMAP};var map = new google.maps.Map(document.getElementById("map_canvas"),mapOptions);var string1 = '"""+a1+"""';var marker1 = new google.maps.Marker({position: new google.maps.LatLng("""+str(a)+""","""+str(b)+"""),map: map,title:string1});var string2 = '"""+c1+"""';var marker2 = new google.maps.Marker({position: new google.maps.LatLng("""+str(c)+""","""+str(d)+"""),map: map,title:string2});var string3 = '"""+e1+"""';var marker3 = new google.maps.Marker({position: new google.maps.LatLng("""+str(e)+""","""+str(f)+"""),map: map,title:string3});var string4 = '"""+g1+"""';var marker4 = new google.maps.Marker({position: new google.maps.LatLng("""+str(g)+""","""+str(h)+"""),map: map,title:string4});var string5 = '"""+i1+"""';var marker5 = new google.maps.Marker({position: new google.maps.LatLng("""+str(i)+""","""+str(j)+"""),map: map,title:string5});}</script></head><body onload="initialize()"><div id="map_canvas" style="width:100%; height:100%"></div></body></html>"""				
			self.response.out.write(mymap)
			
application=webapp.WSGIApplication(
								[('/',Mainpage),
								 ('/display',SearchResult)],
								 debug=True)
def main():
	run_wsgi_app(application)
if __name__ == "__main__":
	main()									 				