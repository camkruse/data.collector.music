#
# Created By Cameron Krusemark
# Created 11/8/2015
import json
import requests


class Setlist:

    def __init__(self):
        self.base_url = "http://api.setlist.fm/rest/0.1/search/setlists.json?"

    def get_setlist(self, attribute, value):

        url = self.base_url + attribute + "=" + value
        resp = requests.get(url)
        self.data = json.loads(resp.text)

    def by_artist(self):

        return "artistName"

    def by_artist_mbid(self):

        return "artistMbid"

####################################################
# Below will be moved into the processing package

# Create Object from Class
objSetlistbyArtist = setlist()


# Call Method from Object
#objSetlistbyArtist.get_setlist_by_artist('Metallica')
objectSetlistbyArtist.get_setlist(objSetlistbyArtist.by_artist,"Metallica")

# Print JSON
print objSetlistbyArtist.data


# Example 2
objSetlistByArtistMbid = setlist()
objSetlistByArtistMbid.get_setlist(objSetlistbyArtist.by_artist_mbid,
    'a16e47f5-aa54-47fe-87e4-bb8af91a9fdd')
print objSetlistByArtistMbid.data
