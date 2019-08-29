 #! python3

#multidownloadXkcd.py - uses multithreading to expedite scraping of xkcd images

import requests, os, bs4, threading
def downloadXkcd(startComic, endComic):
	for urlNumber in range(startComic, endComic):
		# Download page

		print("Downloading page http://xkcd.com/%s..." %(urlNumber))
		res = requests.get('http://xkcd.com%s' % (urlNumber))
		res.raise_for_status()

		soup = bs4.BeautifulSoup(res.text)

		#Find URL of image

		comicElem = soup.select('#comic img')
		if comicElem == []:
			print('Could not find image...')

		else:
			comicUrl = comicElem[0].get('src')

			#Download image.

			print('Downloading %s...' % (comicUrl))
			res = requests.get(comicUrl)
			res.raise_for_status()

			#Save image to ./xkcd

			imageFIle = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()

#TODO: Create/start Thread obj

downloadThreads = []		# List of all thread obj
for i in range(0, 1400, 100):		# Loops 14 times
	downloadThread = threading.Thread(target = downloadXkcd, args=(i,i+99))
	downloadThreads.append(downloadThread)
	downloadThread.start()

#TODO: Wait for all threads to end
for downloadThread in downloadThreads:
	downloadThread.join()
print('Done.')