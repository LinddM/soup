import urls as u
import re
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
output += 'Sorted emails in logs/4directorio_emails.txt'
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

# JSON : rows with Same Address and dump to logs/4directorio_address.json

# JSON : Faculty Dean and Directors, and dump to logs/4directorio_deans.json

# directory of all 3 column table and generate a CSV, and dump to logs/4directorio_3column_tables.csv