# 
# Created By Cameron Krusemark
# Created 11/8/2015

class setlist:
    def getSetlistByArtist(self, artist):
        import json, requests

        # Get method parameter and build web service URL   
        #self.artist = artist  
        url = "http://api.setlist.fm/rest/0.1/search/setlists.json?artistName="+artist
        
        # Call Setlist.fm API using requests library
        resp = requests.get(url)
        
        # Format Request into JSON Object
        self.data = json.loads(resp.text)
        
    def getSetlistByArtistMbid(self, artistMbid):
        import json, requests

        # Get method parameter and build web service URL     
        url = "http://api.setlist.fm/rest/0.1/search/setlists.json?artistMbid="+artistMbid
        
        # Call Setlist.fm API using requests library
        resp = requests.get(url)
        
        # Format Request into JSON Object
        self.data = json.loads(resp.text)
    
####################################################
# Below will be moved into the processing package

# Create Object from Class
objSetlistbyArtist = setlist()

# Call Method from Object
objSetlistbyArtist.getSetlistByArtist('Metallica')

# Print JSON
print objSetlistbyArtist.data


# Example 2
objSetlistByArtistMbid = setlist()
objSetlistByArtistMbid.getSetlistByArtistMbid('a16e47f5-aa54-47fe-87e4-bb8af91a9fdd')
print objSetlistByArtistMbid.data




