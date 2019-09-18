import soup as s
from importlib import reload
reload(s)

output = s.separator_parts + '2. Estudios\n'

# checkbox 1 *to do

# topmenu items (8)
output += 'Topmenu items:\n'

topmenu = s.soup.find('div', {'class':'dsuperior'}).find_all('li')

for i in topmenu:
    output += ' - ' + i.text.strip() + '\n'

output += s.separator_items
# all estudios *to do

# leftbar *to do

# social media links -- needs improvement --
output += 'social media links:\n'

media = s.soup.find_all('div', {'class':'social'})[2].find_all('a')
n = slice(0,5)

for i in media[n]:
    output += ' - ' + i['href'] + '\n'

output += s.separator_items