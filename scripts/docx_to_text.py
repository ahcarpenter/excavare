#!/usr/bin/python
#Drew Carpenter & Jeff Gullett
#CS 4444

import zipfile
from docx import *

#extracts raw text from a docx file and places the text into a Gtk.TextBuffer
def extractRawText(buffer, filename):
	"""
	Read a docx file, RAW TEXT ONLY. Inserting a new line to get proper line breaks,
	keep this in mind as it may cause some issues later, possibly
	"""
	doc = opendocx(filename)
	paratextlist = getdocumenttext(doc)
	newparatextlist = []
	for paratext in paratextlist:
		newparatextlist.append(paratext.encode("utf-8"))
	buffer.set_text(newparatextlist[0])
	end = buffer.get_end_iter()
	for i in range(1,len(newparatextlist)):
		buffer.insert(end,("\n"+newparatextlist[i]))
		end = buffer.get_end_iter()