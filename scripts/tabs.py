#!/usr/bin/python
#Drew Carpenter & Jeff Gullett
#CS 4444

import gtk
import pygtk
import sys
import os
import misc
import docx_to_text
import pdf
import workspace

def get_tab_num(self):
	index = self.fileDisplayArea.get_current_page()
	return index

def remove_page(self, event):
	index = self.fileDisplayArea.get_current_page()
	remove_page(index)

def addTabToDictionary(self, key1, key2):
	self.tabFileDictionary[key1] = key2

def create_tab(self, child, filename):
	
	newTab = gtk.Label(os.path.basename(filename))
	hbox = gtk.HBox(False, 3)
	label2 = gtk.Label(os.path.basename(filename))
	hbox.pack_start(label2)

	#get a stock close button image
	close_image = gtk.image_new_from_stock(gtk.STOCK_CLOSE, gtk.ICON_SIZE_MENU)
	image_w, image_h = gtk.icon_size_lookup(gtk.ICON_SIZE_MENU)
        
	#make the close button
	btn = gtk.Button()
	btn.set_relief(gtk.RELIEF_NONE)
	btn.set_focus_on_click(False)
	btn.add(close_image)
	btn.connect('clicked', remove_page, self.scrolledwindow2)
	hbox.pack_start(btn, False, False)
        
	#this reduces the size of the button
	style = gtk.RcStyle()
	style.xthickness = 0
	style.ythickness = 0
	btn.modify_style(style)
	hbox.show_all()
	addTabToDictionary(self, str(get_tab_num(self) + 1), filename)
	self.pdfDisplayArea.unparent()
	self.fileDisplayArea.append_page(self.pdfDisplayArea,hbox)
	self.fileDisplayArea.next_page()