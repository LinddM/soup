import soup as s

output = '1. Portal\n' + s.separator_parts + '\n'

# title
output += s.soup.title.string + '\n' + s.separator_items + '\n'

# address
output += s.soup.find(id = 'footer').find('a').text + '\n' + s.separator_items + '\n'

# phone and email
phone_and_email = s.soup.find(id = 'footer').find_all('a')

output += phone_and_email[1].text + '\n' + phone_and_email[2].text + '\n' + s.separator_items + '\n'

# nav menu
nav_menu = s.soup.find(id = 'menu-table').findAll('td')

for i in nav_menu:
    output += i.text.strip() + '     '

output += '\n' + s.separator_items + '\n'



# tip
# divs = soup.findAll("table", {"class": "an"})