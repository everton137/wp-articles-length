#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wp_articles_length.py
#
#  (C) 2011 Alchimista <alchimistawp@gmail.com>
#
#   Distributed under the terms of the GNU GPL license.
#

import wikipedia
import pagegenerators
import re


def main():

	def pageFromList(lx):
		for i in lx:
			yield wikipedia.Page(site, i)

	site = wikipedia.getSite()
	listPage = wikipedia.Page(site, u"Wikipédia:Wikipédia na Universidade/Verbetes")
	text = listPage.get()

	# Para criar a lista de artigos
	lr = re.compile(u'\#(?P<links>.*?)\s*(?:\\n|\|)', re.I | re.M | re.U)
	# Para obter a associação dos id's a cada artigo
	lr2 = re.compile(u'\#(?P<links>.*?)\s*\|\s*ids\s*\=\s*(?P<id1>\d{8})\,\s*(?P<id2>\d{8})', re.I | re.M | re.U)
	# Para obter a lista de id's
	lr3 = re.compile(u'\#(?:.*)\s*\|\s*ids\s*\=\s*(?P<id1>\d{8})\,\s*(?P<id2>\d{8})', re.I | re.M | re.U)

	links = lr.findall(text)
	ids = lr3.findall(text)
	ids = map(int, ids[0])

	gen = pageFromList(links)
	pages = pagegenerators.NamespaceFilterPageGenerator(gen, [0])

	for i in pages:
		print i
		for n in i.getVersionHistory():
			if n[0] in ids:
				#tit = i.title()
				print u"\n", i.title(), n[0], n[4], u"\n"
				#dict[tit][n[0]] = n[4]


if __name__ == "__main__":
	try:
		main()
	finally:
		wikipedia.stopme()
