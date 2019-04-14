"""
Grab data from the twitter API and import it into the database
"""

import tweepy
from map.models import TrashTag


class tweets():
    def __init__(self):
        auth = tweepy.OAuthHandler('WTlR4vdaXPAx15eRKzarFFK5M', "V3stPYHjdQVCKEZE8dqzZNOzNJndaoX2rcI4pRAf090dBmLrf6")
        auth.set_access_token("1041353482794500097-T0WUVf07qWlHw13VG8t5gvpw24KwC0", "OHPDCoO6qHWpysPSMuO1L3HUi4ewY1l034VCeGWyqXR3Q")
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3,
                              retry_delay=60)

    def search_for_tweets(self, lowid):
        A = []
        if (lowid != None):  # if you dont have a previous itt,
            twt = self.api.search(q='#trashtag', count=100, max_id=lowid)
            for st in twt:
                coordinates = None
                A.append(st.id)
                if (st.coordinates):
                    lon = st.coordinates["coordinates"][0]
                    lat = st.coordinates["coordinates"][1]
                    url = st.entities["urls"][0]["url"]
                    print(lon)
                    print(lat)
                    print(url)

                    newTTag = TrashTag(lat, lon, url)
                    newTTag.save()

                    print(10 * '-')
        else:  # if you have a previous itt,
            twt = self.api.search(q="#trashtag", count=100)
            for st in twt:
                coordinates = None
                A.append(st.id)
                if (st.coordinates):
                    lon = st.coordinates["coordinates"][0]
                    lat = st.coordinates["coordinates"][1]

                    url = st.entities["urls"][0]["url"]

                    print(lon)
                    print(lat)
                    print(url)

                    newTTag = TrashTag(lat, lon, url)
                    newTTag.save()

                    print(10 * '-')

        return (min(A))

t = tweets()
a = None
for x in range(1, 100):
    a = t.search_for_tweets(a)