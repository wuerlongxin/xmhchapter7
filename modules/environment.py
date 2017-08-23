# /usr/bin/env/python
# -*- coding:utf-8 -*-

import os

def run(**args):
    print "[*] In environment moudle."
    return str(os.environ)
