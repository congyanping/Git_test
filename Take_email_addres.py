#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
re_addres=re.compile(r'^(\s{8})@([\s\d]+)$')
print re_addres.match('bankonme@163.com').groups()
