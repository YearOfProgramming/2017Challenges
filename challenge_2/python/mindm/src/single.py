#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
from collections import defaultdict

try:
    j = json.loads(" ".join(sys.argv[1:]))
except json.decoder.JSONDecodeError as e:
    print("Invalid input, try JSON")
    exit(1)

ls = defaultdict(int)
for num in j:
    ls[num] += 1

res = []

for num, value in ls.items():
    if value == 1:
        res.append(num)

if len(res) == 1:
    print(res[0])
elif len(res) > 1:
    print("Found more than 1 single value")
else:
    print("No single values found")

