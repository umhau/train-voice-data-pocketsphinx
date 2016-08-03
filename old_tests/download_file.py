# get the file.

import urllib2  # the lib that handles the url stuff
target_url = 'http://festvox.org/cmu_arctic/cmuarctic.data'
data = urllib2.urlopen(target_url) # it's a file like object and works just like a file
for line in data: # files are iterable
    print line
    

