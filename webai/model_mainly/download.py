from flickrapi import FlickrAPI 
from urllib.request import urlretrieve
import os, time, sys 

key = '5ce893e3d166a6950fbfe5e7b029e3ec'
secret = 'fc75466e29a1ca7c'
wait_time = 1

keyword = sys.argv[1]
savedir = './' + keyword

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = keyword,
    per_page = 500,
    media = 'photos',
    sort = 'interestingness-desc',
    safe_search = 1,
    extras = 'url_q, license'
)

photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): 
        time.sleep(wait_time) 
        continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)


