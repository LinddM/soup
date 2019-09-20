import urls as u
import re
import json
import csv
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

        if address in keys:
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

output += 'Rows with same address in logs/4directorio_address.json' + separator_items

# JSON : Faculty Dean and Directors, and dump to logs/4directorio_deans.json
dean_and_directors = u.directorio.find_all('table',{'class':'tabla ancho100 col3'})[1].find_all('tr')
faculty = {}

for i in dean_and_directors:
    count = 0
    tdlist = i.find_all('td')
    fclty = ''
    name = ''
    email = ''

    for j in tdlist:
        if count == 0:
            fclty = j.text.strip()
        if count == 1:
            name = j.text.strip().split(',')[0]
        if count == 2:
            email = j.text.strip()
        count += 1
    
    profile = {'Dean/Director':f'{name}', 'email':f'{email}'}
    faculty[fclty] = profile
    
with open('logs/4directorio_deans.json', 'w') as profs:
    profs.write(json.dumps(faculty, indent=4, sort_keys=True))
    profs.close()

output += 'Faculty Dean and Directors in logs/4directorio_deans.json'

# directory of all 3 column table and generate a CSV, and dump to logs/4directorio_3column_tables.csv
array = []
three_column_table = u.directorio.findAll('table',{'class':'tabla ancho100 col3'})
for i in three_column_table:
    individual_table = i.find_all('tr')
    for j in individual_table:
        tdlist = j.find_all('td')
        column1 = ''
        column2 = ''
        column3 = ''

        count = 0
        for k in tdlist:
            if count == 0:
                column1 = k.text.strip()
            if count == 1:
                column2 = k.text.strip().split(',')[0]
            if count == 2:
                column3 = k.text.strip()
            count += 1
        data = {'Entity':f'{column1}', 'FullName':f'{column2}', 'Email':f'{column3}'}
        array.append(data)

keys_csv = array[0].keys()
with open('logs/4directorio_3column_tables.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys_csv)
    dict_writer.writeheader()
    dict_writer.writerows(array)