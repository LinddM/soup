import urls as u
import soup as s

output = s.separator_parts + '1. Portal\n'

# title
output += 'Title:\n' + u.portal.title.string + s.separator_items

# address
output += 'Address:\n' + u.portal.find(id = 'footer').find('a').text + s.separator_items

# phone and email
phone_and_email = u.portal.find(id = 'footer').find_all('a')

output += 'Phone and email:\n' + phone_and_email[1].text + '\n' + phone_and_email[2].text + s.separator_items

# nav menu
nav_menu = u.portal.find(id = 'menu-table').findAll('td')
output += 'Nav menu items:\n'

for i in nav_menu:
    output += ' - ' + i.text.strip() + '\n'

output +=  s.separator_items

# all links
links = u.portal.find_all('a', href = True)
output += 'Links:\n'

for i in links:
    if i.text.isalpha() == True:
        output += ' - ' + i.text.strip() + '\n'

output += s.separator_items

# ufmail
output += u.portal.find(id = 'ufmail_').text + ':\n' + u.portal.find(id = 'ufmail_')['href']

output += s.separator_items

# miu
output += u.portal.find(id = 'miu_').text + ':\n' + u.portal.find(id = 'miu_')['href']

output += s.separator_items

# img
images = u.portal.find_all('img')

output += 'Images:\n'

for i in images:
    output += ' - ' + i['src'] +'\n'

output += s.separator_items

# count <a>
a_coincidences = u.portal.findAll('a')

output += "Count <a>:\n" + str(len(a_coincidences))