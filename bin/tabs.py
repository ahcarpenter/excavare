#!/usr/bin/python
#Drew Carpenter & Jeff Gullett
#CS 4444
#Excavare 0.0
#March 28, 2011
import gtk
import pygtk
import sys
import os
import misc
import docx_to_text
import pdf
#from pyPdf import PdfFileWriter, PdfFileReader
import workspace

#def create_new_tab(self,filename):
#	num_pages=1
#	tabName = filename.split('/')
#	if len(tabName)==1:
#		tabName=filename.split('\\')
#	#get label name & apply
#	label = tabName[-1]
#	newTab = gtk.Label(label)
#	hbox = gtk.HBox(True, 6)
#	label2 = gtk.Label(label)
#	hbox.pack_start(label2)
#
#	#get a stock close button image
#	close_image = gtk.image_new_from_stock(gtk.STOCK_CLOSE, gtk.ICON_SIZE_MENU)
#	image_w, image_h = gtk.icon_size_lookup(gtk.ICON_SIZE_MENU)
#        
#	#make the close button
#	btn = gtk.Button()
#	btn.set_relief(gtk.RELIEF_NONE)
#	btn.set_focus_on_click(False)
#	btn.add(close_image)
#	hbox.pack_start(btn, False, False)
#        
#	#this reduces the size of the button
#	style = gtk.RcStyle()
#	style.xthickness = 0
#	style.ythickness = 0
#	btn.modify_style(style)
#
#	hbox.show_all()
#	
#	#now get the extension type
#	extension = tabName[-1].split('.')
#	#what kind of file is being opened?
#	imageTypes=["jpg","bmp","tif","gif","jpeg","png"]
#	saved_once=False
#	if extension[1] == "pdf":
#		#call pdf opening routine
#		num_pages=pdfRead.readPDF(newTab,filename,self)
#		#if textpdf is "":
#			#if num_pages>1:
#				#temp_tab=tabName[-1]
#				#temp_tab2=temp_tab.split(".")
#				#temp_tab=temp_tab2[0]+"0.pdf"
#				#tabName[-1]=temp_tab
#				#temp_filename=filename.split(".")
#				#filename=temp_filename[0]+"0.tif"
#		self.tab_nums+=1
#	elif extension[1] == "docx":
#		newScrolledWindow,newTextView=create_scrolled_window()
#		#get text buffer
#		text = newTextView.get_buffer()			
#		#call docx opening routine
#		docxRead.readDocx(text,filename)
#		self.notebook.append_page(newScrolledWindow,hbox)
#		btn.connect('clicked', self.on_closetab_button_clicked, newScrolledWindow)
#		self.tab_nums+=1
#		#put new textview in list of textviews
#		self.textviews.append(newTextView)
#		self.notebook.set_focus_child(newScrolledWindow)
#	elif extension[1]=="txt":
#		newScrolledWindow,newTextView=create_scrolled_window()
#		#get text buffer
#		text = newTextView.get_buffer()						
#		#open the file and read to a variable
#		file = open(filename,"r")
#		file_text = file.read()
#		#set text buffer to variable with file text, close file
#		text.set_text(file_text)
#		file.close()
#		self.notebook.append_page(newScrolledWindow,hbox)
#		btn.connect('clicked', self.on_closetab_button_clicked, newScrolledWindow)
#		self.tab_nums=self.tab_nums+1
#		#put new textview in list of textviews
#		self.textviews.append(newTextView)
#		saved_once=True
#		self.notebook.set_focus_child(newScrolledWindow)		
#	elif extension[1] in imageTypes:
#		drawable.image_view_event_box(self,filename,False)
#		self.tab_nums+=1
#	elif extension[1]=="wksp":
#		open_workspace.open_workspace(self,filename)
#		self.is_workspace=True
#		return
#	#append tabname,tab number, filename to our tree list
#	self.list_store.append([tabName[-1],self.tab_nums,filename,num_pages,0,saved_once])
#	#reset the tree attributes
#	self.column.set_attributes(self.cell, text=0)
#	self.notebook.show_all()

def get_tab_num(self):
	index = self.fileDisplayArea.get_current_page()
	return index

def remove_page(self, event):
	index = self.fileDisplayArea.get_current_page()
	remove_page(index)
	
#def on_new_tab_focus(self):
#	print self.current_selection
#	self.current_selection = self.tabFileDictionary[str(self.fileDisplayArea.get_tab_num())]
#	print self.current_selection
	
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
#
#def create_scrolled_window():
#	#prepare the new tab	
#	newTextView = gtk.TextView(None)
#	newScrolledWindow = gtk.ScrolledWindow(None,None)
#	newScrolledWindow.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
#	newTextView.set_wrap_mode(gtk.WRAP_WORD)
#	newTextView.set_left_margin(50)
#	newTextView.set_right_margin(50)
#	newScrolledWindow.add_with_viewport(newTextView)
#	return newScrolledWindow,newTextView
#	
#def create_new_tab_from_treeview(self,filename,tm,ti):
#	num_pages=1
#	tabName = filename.split('/')
#	if len(tabName)==1:
#		tabName=filename.split('\\')
#	#get label name & apply
#	label = tabName[-1]
#	newTab = gtk.Label(label)
#	hbox = gtk.HBox(False, 0)
#	label2 = gtk.Label(label)
#	hbox.pack_start(label2)
#
#	#get a stock close button image
#	close_image = gtk.image_new_from_stock(gtk.STOCK_CLOSE, gtk.ICON_SIZE_MENU)
#	image_w, image_h = gtk.icon_size_lookup(gtk.ICON_SIZE_MENU)
#        
#	#make the close button
#	btn = gtk.Button()
#	btn.set_relief(gtk.RELIEF_NONE)
#	btn.set_focus_on_click(False)
#	btn.add(close_image)
#	hbox.pack_start(btn, False, False)
#        
#	#this reduces the size of the button
#	style = gtk.RcStyle()
#	style.xthickness = 0
#	style.ythickness = 0
#	btn.modify_style(style)
#
#	hbox.show_all()
#		
#	#now get the extension type
#	extension = tabName[-1].split('.')
#	#what kind of file is being opened?
#	imageTypes=["jpg","bmp","tif","gif","jpeg","png"]
#	saved_once=False
#	if extension[1] == "pdf":
#		#call pdf opening routine
#		num_pages=pdfRead.readPDF(newTab,filename,self)
#		#if textpdf is "":
#			#if num_pages>1:
#				#temp_tab=tabName[-1]
#				#temp_tab2=temp_tab.split(".")
#				#temp_tab=temp_tab2[0]+"0.pdf"
#				#tabName[-1]=temp_tab
#				#temp_filename=filename.split(".")
#				#filename=temp_filename[0]+"0.tif"
#		self.tab_nums+=1
#	elif extension[1] == "docx":
#		newScrolledWindow,newTextView=create_scrolled_window()
#		#get text buffer
#		text = newTextView.get_buffer()			
#		#call docx opening routine
#		docxRead.readDocx(text,filename)
#		self.notebook.append_page(newScrolledWindow,hbox)
#		btn.connect('clicked', self.on_closetab_button_clicked, newScrolledWindow)
#		self.tab_nums+=1
#		#put new textview in list of textviews
#		self.textviews.append(newTextView)								
#		self.notebook.set_focus_child(newScrolledWindow)
#	elif extension[1]=="txt":
#		newScrolledWindow,newTextView=create_scrolled_window()
#		#get text buffer
#		text = newTextView.get_buffer()						
#		#open the file and read to a variable
#		file = open(filename,"r")
#		file_text = file.read()
#		#set text buffer to variable with file text, close file
#		text.set_text(file_text)
#		file.close()
#		self.notebook.append_page(newScrolledWindow,hbox)
#		btn.connect('clicked', self.on_closetab_button_clicked, newScrolledWindow)
#		self.tab_nums=self.tab_nums+1
#		#put new textview in list of textviews
#		self.textviews.append(newTextView)
#		saved_once=True
#		self.notebook.set_focus_child(newScrolledWindow)
#	elif extension[1] in imageTypes:
#		drawable.image_view_event_box(self,filename,False)
#		self.tab_nums+=1
#	tm.set_value(ti,1,self.tab_nums)
#	tm.set_value(ti,3,num_pages)
#	tm.set_value(ti,4,0)
#	tm.set_value(ti,5,saved_once)
#	self.notebook.show_all()