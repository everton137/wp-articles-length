#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      wp_articles_length.py
#
#      (C) 2011 Alchimista <alchimistawp@gmail.com>
#
#       Distributed under the terms of the GNU GPL license.

import wikipedia
import re


def main():
    site = wikipedia.getSite()
    listPage = wikipedia.Page(site, u"Wikipédia:Wikipédia na Universidade/Verbetes")
    text = listPage.get()
    lr = re.compile(u'\#(?P<links>.*?)\s*\\n', re.I | re.M | re.U)
    links = lr.findall(text)
    for link in links:
        pag = wikipedia.Page(site, link)
        print pag.title(), pag.getVersionHistory()[0][4]

if __name__ == "__main__":
    try:
        main()
    finally:
        wikipedia.stopme()
