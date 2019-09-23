def estudios (url, separator_items, separator_parts):

    output = separator_parts + '2. Estudios\n'

    # topmenu items (8)
    top = url.find('div',{'id':'topmenu'}).find_all('a')
    output += 'Topmenu items:\n'

    for i in top:
        output += ' - ' + i.text.strip() + '\n'

    output += separator_items

    # all estudios
    output += 'All estudios:\n'

    all_estudios = url.findAll('div', {'class': 'estudios'})
    
    for i in all_estudios:
        output += ' - ' + i.text + '\n'

    output += separator_items

    # leftbar
    output += "Leftbar items:\n"
    left_items = url.find('div', {'class':'leftbar'}).find_all('li')

    for i in left_items:
        output += ' - ' + i.text + '\n'

    output += separator_items

    # social media links
    output += 'Social media links:\n'

    social_media = url.find('div', {'class':'social pull-right'}).find_all('a')

    for i in social_media:
        output += ' - ' + i['href'] + '\n'

    output += separator_items

    # count <a>
    a_coincidences = url.findAll('a')

    output += "Count <a>:\n" + str(len(a_coincidences))

    return output