import re
import requests


def get_h3(link):
    response = requests.get(link)
    html = response.text

    pattern = r'<h3(?:\s+.*?)*?>(.*?)</h3>'
    h3 = re.findall(pattern, html)

    return h3


link = 'http://www.columbia.edu/~fdc/sample.html'
h3 = get_h3(link)
print(h3)