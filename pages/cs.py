import urls as u
import urllib
import os
'''
import soup as s
from importlib import reload
reload(s)
reload(u)
'''

separator_parts = '\n=============================================================================================================\n'
separator_items = '\n-------------------------------------------------------------------------------------------------------------\n'

# title
output = separator_parts + '3. CS\n'

output += 'Title:\n' + u.cs.title.string + separator_items

# display href

# download "FACULTAD de CIENCIAS ECONOMICAS" logo
output += 'FACULTAD de CIENCIAS ECONOMICAS logo:\n'

logo = u.cs.find('img', {'class':'fl-photo-img wp-image-500 size-full'})['src']
try:
    urllib.request.urlretrieve(logo, os.path.basename(logo))
    output += 'Logo downloaded succesfully!\n' + separator_items
except:
    output += 'Unable to download logo\n' + separator_items

# get <meta>: "title", "description" ("og")

# count <a>

# count <div>