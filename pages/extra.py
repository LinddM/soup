# From all (<a>) Create a csv file (logs/extra_as.csv) with Text and href
import csv

def extra (url):
    links = url.find_all('a')
    data = []
    for link in links:
        element = {'Text': link.text, 'href': link['href']}
        data.append(element)

    keys = ['Text', 'href']
    with open('logs/extra_as.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)