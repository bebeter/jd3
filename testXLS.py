#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv

with open('egg2.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['a', '1', '1', '2', '2'])
    spamwriter.writerow(['b', '3', '3', '6', '4'])
    spamwriter.writerow(['c', '7', '7', '10', '4'])
    spamwriter.writerow(['d', '11', '11', '11', '1'])
    spamwriter.writerow(['e', '12', '12', '14', '3'])
csvfile.close()

with open('egg2.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
f.close()
