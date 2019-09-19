import urls as u
import re
import json
'''
import soup as s
from importlib import reload
reload(s)
reload(u)
'''

separator_parts = '\n=============================================================================================================\n'
separator_items = '\n-------------------------------------------------------------------------------------------------------------\n'

output = separator_parts + '4. Directorio\n'

# sort emails and dump to logs/4directorio_emails.txt
output += 'Sorted emails in logs/4directorio_emails.txt' + separator_items
mails = u.directorio.find_all('a', {'href':re.compile('@ufm.edu')})
mails_text = []
for i in mails:
    mails_text.append(i.text)

sorted_mails_list = list(dict.fromkeys(sorted(mails_text))) 

with open('logs/4directorio_emails.txt', 'w') as dirm:
    for i in sorted_mails_list:
        dirm.write(' - ' + i + '\n')
dirm.close()

# count emails that start with a vowel
vowel_emails = 0
for i in sorted_mails_list:
    if(i[0] in ['a', 'e', 'i', 'o', 'u']):
        vowel_emails = vowel_emails + 1

output += 'Vowel count:\n' + str(vowel_emails) + separator_items

# JSON : rows with Same Address and dump to logs/4directorio_address.json
table1 = u.directorio.find('table',{'class':'tabla ancho100'}).find_all('tr')
table2 = u.directorio.find_all('table',{'class':'tabla ancho100'})[1].find_all('tr') 

office = {}
keys = []
def getAddress (table):
    for i in table:
        count = 0
        tdlist = i.find_all('td')

        page = ''
        address = ''
        for j in tdlist:
            if count == 0:
                page = j.text.strip()
            if count == 4:
                address = j.text.strip().split(',')[0]
            count += 1

        if (address in keys):
            office.get(address).append(page)
        else:
            keys.append(address)
            arr = []
            arr.append(page)
            office[address] = arr

    return json.dumps(office, indent=4, sort_keys=True)
getAddress(table1)

with open('logs/4directorio_address.json', 'w') as addr:
    addr.write(getAddress(table2))
    addr.close()

# JSON : Faculty Dean and Directors, and dump to logs/4directorio_deans.json

# directory of all 3 column table and generate a CSV, and dump to logs/4directorio_3column_tables.csv