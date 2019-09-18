import soup as s
import urls as u
from importlib import reload
reload(s)
reload(u)

output = s.separator_parts + '2. Estudios\n'

# checkbox 1

# topmenu items (8)
top = u.estudios.find('div',{'id':'topmenu'}).find_all('a')
output += 'Topmenu items:\n'

for i in top:
    output += ' - ' + i.text.strip() + '\n'

output += s.separator_items

# all estudios
output += 'All estudios:\n'

all_estudios = u.estudios.findAll('div', {'class': 'estudios'})

for i in all_estudios:
    output += ' - ' + i.text + '\n'

output += s.separator_items

# leftbar
output += "Leftbar items:\n"
left_items = u.estudios.find('div', {'class':'leftbar'}).find_all('li')

for i in left_items:
    output += ' - ' + i.text + '\n'

output += s.separator_items

# social media links
output += 'Social media links:\n'

social_media = u.estudios.find('div', {'class':'social pull-right'}).find_all('a')

for i in social_media:
    output += ' - ' + i['href'] + '\n'

output += s.separator_items

# count <a>
a_coincidences = u.estudios.findAll('a')

output += "Count <a>:\n" + str(len(a_coincidences))