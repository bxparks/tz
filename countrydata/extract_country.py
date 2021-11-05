#!/usr/bin/env python3
# Extract the country name from stdin, where the stdin is assumed to be the ISO
# 3166 country list from
# https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/slim-2/slim-2.csv
#
# Usage:
# $ python3 extract_country.py < iso-3166-countries.csv > raw_countries.list

import sys
import csv

reader = csv.reader(sys.stdin)
for row in reader:
    print(row[0])
