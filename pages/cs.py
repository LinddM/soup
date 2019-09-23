import urllib
import os

def cs(url, separator_items, separator_parts):

    separator_parts = '\n=============================================================================================================\n'
    separator_items = '\n-------------------------------------------------------------------------------------------------------------\n'

    # title
    output = separator_parts + '3. CS\n'

    output += 'Title:\n' + url.title.string + separator_items

    # download "FACULTAD de CIENCIAS ECONOMICAS" logo
    output += 'FACULTAD de CIENCIAS ECONOMICAS logo:\n'

    logo = url.find('img', {'class':'fl-photo-img wp-image-500 size-full'})['src']
    try:
        urllib.request.urlretrieve(logo, os.path.basename(logo))
        output += 'Logo downloaded succesfully!\n' + separator_items
    except:
        output += 'Unable to download logo\n' + separator_items

    # get <meta>: "title", "description" ("og")
    output += 'Get <meta> title and description:\n'

    meta_title = url.find('meta', {'property':'og:title'})['content']
    meta_description = url.find('meta', {'property':'og:description'})['content']

    output += meta_title + '\n' + meta_description + separator_items

    # count <a>
    a_coincidences = url.findAll('a')

    output += "Count <a>:\n" + str(len(a_coincidences)) + separator_items

    # count <div>
    div_coincidences = url.findAll('div')

    output += "Count <div>:\n" + str(len(div_coincidences))

    return output