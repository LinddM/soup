def portal (url, separator_items, separator_parts):

    output = separator_parts + '1. Portal\n'

    # title
    output += 'Title:\n' + url.title.string + separator_items

    # address
    output += 'Address:\n' + url.find(id = 'footer').find('a').text + separator_items

    # phone and email
    phone_and_email = url.find(id = 'footer').find_all('a')

    output += 'Phone and email:\n' + phone_and_email[1].text + '\n' + phone_and_email[2].text + separator_items

    # nav menu
    nav_menu = url.find(id = 'menu-table').findAll('td')
    output += 'Nav menu items:\n'

    for i in nav_menu:
        output += ' - ' + i.text.strip() + '\n'

    output +=  separator_items

    # all links
    links = url.find_all('a', href = True)
    output += 'Links:\n'

    for i in links:
        if i.text.isalpha() == True:
            output += ' - ' + i.text.strip() + '\n'

    output += separator_items

    # ufmail
    output += url.find(id = 'ufmail_').text + ':\n' + url.find(id = 'ufmail_')['href']

    output += separator_items

    # miu
    output += url.find(id = 'miu_').text + ':\n' + url.find(id = 'miu_')['href']

    output += separator_items

    # img
    images = url.find_all('img')

    output += 'Images:\n'

    for i in images:
        output += ' - ' + i['src'] +'\n'

    output += separator_items

    # count <a>
    a_coincidences = url.findAll('a')

    output += "Count <a>:\n" + str(len(a_coincidences))

    return output