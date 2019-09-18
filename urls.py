from bs4 import BeautifulSoup
import requests,sys,csv,json

# Portal Page
url_portal="http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
try:
    html_content_portal = requests.get(url_portal).text
except:
    print(f"unable to get {url_portal}")
    sys.exit(1)
# Parse the html content
portal = BeautifulSoup(html_content_portal, "html.parser")


# Estudios page
url_estudios="http://ufm.edu/Estudios"
try:
    html_content_estudios = requests.get(url_estudios).text
except:
    print(f"unable to get {url_estudios}")
    sys.exit(1)
estudios = BeautifulSoup(html_content_estudios, "html.parser")


# CS page
url_cs="https://fce.ufm.edu/carrera/cs/"
try:
    html_content_cs = requests.get(url_cs).text
except:
    print(f"unable to get {url_cs}")
    sys.exit(1)
cs = BeautifulSoup(html_content_cs, "html.parser")

# Directorio page
url_directorio="https://www.ufm.edu/Directorio"
try:
    html_content_directorio = requests.get(url_directorio).text
except:
    print(f"unable to get {url_directorio}")
    sys.exit(1)
directorio = BeautifulSoup(html_content_directorio, "html.parser")


# check number of lines in each part
def noArgcheckLines(portal, estudios, cs, directorio):
    lines = portal.count('\n') + estudios.count('\n') + cs.count('\n') + directorio.count('\n')
    if lines > 30:
        # do something here
        return 'Output exceeds 30 lines, sending output to: <logfile>'
    else:
        return portal + estudios + cs + directorio

def checkLines(part):
    if part.count('\n') > 30:
        # do something here
        return 'Output exceeds 30 lines, sending output to: <logfile>'
    else:
        return part