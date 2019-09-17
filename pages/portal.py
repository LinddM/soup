import soup as s

output = '1. Portal\n' + s.separator_parts + '\n'

output += s.soup.title.string + '\n' + s.separator_items + '\n'

output += s.soup.find(id = 'footer').find('a').text + '\n' + s.separator_items + '\n'

phone_and_email = s.soup.find(id = 'footer').find_all('a')

output += phone_and_email[1].text + '\n' + phone_and_email[2].text + '\n' + s.separator_items