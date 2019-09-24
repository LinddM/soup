#!/usr/bin/env python3
import pages.portal as portal
import pages.estudios as estudios
import pages.cs as cs
import pages.directorio as directorio
import pages.extra as extra
import urls

import sys

separator_parts = '\n=============================================================================================================\n'
separator_items = '\n-------------------------------------------------------------------------------------------------------------\n'

if __name__ == "__main__":
    port = portal.portal(urls.portal, separator_items, separator_parts)
    studies = estudios.estudios(urls.estudios, separator_items, separator_parts)
    comp_sci = cs.cs(urls.cs, separator_items,separator_parts)
    directory = directorio.directorio(urls.directorio, separator_items, separator_parts)

    print('Lindsey\n')
    if len(sys.argv) == 1:
        print(urls.noArgcheckLines(port, studies, comp_sci, directory, "All_parts"))
        extra.extra(urls.portal)
    elif sys.argv[1] == '1':
        print(urls.checkLines(port, 1))
    elif sys.argv[1] == '2':
        print(urls.checkLines(studies, 2))
    elif sys.argv[1] == '3':
        print(urls.checkLines(comp_sci, 3))
    else:
        print('invalid argument')