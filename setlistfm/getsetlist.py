

# URL library
import json, requests, pprint

url = 'http://api.setlist.fm/rest/0.1/search/setlists.json?artistName=metallica'

"""
params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)
"""
#resp = requests.get(url=url, params=params)
resp = requests.get(url=url)
data = json.loads(resp.text)

with open('metallica.txt', 'w') as outfile: 
        json.dump(data, outfile)
    
 # pprint.pprint(data)
