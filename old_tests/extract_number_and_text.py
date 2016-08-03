# extract the number and the text

import re
import urllib2  # the lib that handles the url stuff
target_url = 'http://festvox.org/cmu_arctic/cmuarctic.data'
data = urllib2.urlopen(target_url) 
for line in data: 
    try:
        matches = re.findall('\(\sarctic_a(?P<number>\d\d\d\d)\s\"(?P<text>.+)"\s\)', line, re.DOTALL)
    except AttributeError:
        pass
    print(matches)


