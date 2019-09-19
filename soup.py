#!/usr/bin/env python3
import pages.portal as portal
import pages.estudios as estudios
import pages.cs as cs
import pages.directorio as directorio
import urls

import sys

separator_parts = '\n=============================================================================================================\n'
separator_items = '\n-------------------------------------------------------------------------------------------------------------\n'

if __name__ == "__main__":
    print('Lindsey\n')
    if len(sys.argv) == 1:
        print(urls.noArgcheckLines(portal.output, estudios.output, cs.output, directorio.output, "All_parts"))
    elif sys.argv[1] == '1':
        print(urls.checkLines(portal.output, 1))
    elif sys.argv[1] == '2':
        print(urls.checkLines(estudios.output, 2))
    elif sys.argv[1] == '3':
        print(urls.checkLines(cs.output, 3))
    else:
        print('invalid argument')

