import soup as s

output = s.separator_parts + '\n' + '1. Portal\n'

# title
output += 'Title:\n' + s.soup.title.string + '\n' + s.separator_items + '\n'

# address
output += 'Address:\n' + s.soup.find(id = 'footer').find('a').text + '\n' + s.separator_items + '\n'

# phone and email
phone_and_email = s.soup.find(id = 'footer').find_all('a')

output += 'Phone and email:\n' + phone_and_email[1].text + '\n' + phone_and_email[2].text + '\n' + s.separator_items + '\n'

# nav menu
nav_menu = s.soup.find(id = 'menu-table').findAll('td')
output += 'Nav menu items:\n'

for i in nav_menu:
    output += ' - ' + i.text.strip() + '\n'

output +=  s.separator_items + '\n'

# all links
links = s.soup.find_all('a', href = True)
output += 'Links:\n'

for i in links:
    if i.text.isalpha() == True:
        output += ' - ' + i.text.strip() + '\n'

output += s.separator_items + '\n'

# ufmail
output += s.soup.find(id = 'ufmail_').text + ':\n' + s.soup.find(id = 'ufmail_')['href'] +'\n'

output += s.separator_items + '\n'

# miu
output += s.soup.find(id = 'miu_').text + ':\n' + s.soup.find(id = 'miu_')['href'] + '\n'

output += s.separator_items +'\n'

# img
images = s.soup.find_all('img')

output += 'Images:\n'

for i in images:
    output += ' - ' + i['src'] +'\n'

output += s.separator_items + '\n'

# count <a>
a_coincidences = s.soup.findAll('a')

output += "Count <a>:\n" + str(len(a_coincidences))