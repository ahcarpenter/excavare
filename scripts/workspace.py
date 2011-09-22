#!/usr/bin/python
#Drew Carpenter & Jeff Gullett
#CS 4444

import pygtk
import gtk
import sys
import create_tabs

def open_workspace(self,workspace):
	file = open(workspace,"r")
	line = file.readline()
	split_line = line.split("\t")
	file_location=split_line[-1]
	short_filename_list=file_location.split("/")
	if len(short_filename_list)==1:
		short_filename_list=file_location.split("\\")
	title=short_filename_list[-1]
	self.excavare.set_title(title)
	num_pages=self.notebook.get_n_pages()
	for i in range(0,num_pages):
		self.notebook.remove_page(-1)
		#self.notebook.show_all()
	self.list_store.clear()
	self.column.set_attributes(self.cell, text=0)
	self.notebook.show_all()
	self.tab_nums=-1
	tab_num_line=file.readline()
	#ignore = file.readline()
	for lines in workspace:
		filename=file.readline()
		if filename=="":
			break
		fix_filename=filename.split("\n")
		filename=fix_filename[0]
		create_tabs.create_new_tab(self,filename)
	self.notebook.show_all()
	file.close()