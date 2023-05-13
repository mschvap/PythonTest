from urllib.request import urlopen
from urllib.error import URLError,HTTPError

url = "https://www.google.com.ar/"

try:
    response = urlopen(url)
    print('Status code: ' + str(response.code))
    mensaje = str(response.code)
except HTTPError as err:
    print('Satus code: ' + str(err.code))
    mensaje = str(err.code)
except URLError as e:
    print('Status code: ' +str(e.reason))
    mensaje = str(e.reason)

if mensaje == '200':
    exit(0)
else:
    exit(1)


