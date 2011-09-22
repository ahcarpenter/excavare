#!/usr/bin/python
#Drew Carpenter & Jeff Gullett
#CS 4444

import sys
import pygtk
import gtk
import gtk.gdk
import os
from PIL import Image
ocr_read = False
count = 0
x = 0
y = 0
h=0
w=0

def image_view_event_box(self,filename,is_pdf):
	#remove the notebook page
	#pop last item from textviews list
	#self.notebook.remove_page(self.tab_nums)
	#useless = self.textviews.pop()
	#create new scrolly window
	scrolly = gtk.ScrolledWindow()
	scrolly.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
	#create event box, add to scrolly
	eventBox = gtk.EventBox()
	scrolly.add_with_viewport(eventBox)
	eventBox.show()
	#create image, align top left corner
	image = gtk.Image()
	image.set_alignment(0,0)
	image.set_padding(0,0)
	#print "\npixbuf file: "+filename+"\n"
	picture = gtk.gdk.pixbuf_new_from_file(filename)
	w,h = picture.get_width(), picture.get_height()
	drawable = gtk.gdk.Pixmap(None, w, h, 24)
	gc = drawable.new_gc()
	drawable.draw_pixbuf(gc, picture, 0,0,0,0,-1,-1)
	image.set_from_pixmap(drawable,None)
	eventBox.add(image)
	tabName = filename.split('/')
	if len(tabName)==1:
		tabName=filename.split('\\')
	#since we are immediately converting pdf's to TIFF's for OCR
	#we will change the extension of .tif to say .pdf IF is_pdf is
	#True so that the user is not confused
	if is_pdf:
		extension = tabName[-1].split('.')
		if extension[1]=="tif":
			label=tabName[-1]
			label2=label.replace("0.tif",".pdf")
			newLabel = gtk.Label(label2)
	else:
		newLabel = gtk.Label(tabName[-1])
	#add page to notebook (index is correct already, so is listStore)
	
	#for the love of god change this in a minute
	#if is_pdf:
	self.notebook.append_page(scrolly,newLabel)
	#else:
	#	current_page=self.notebook.get_current_page()
	#	self.notebook.insert_page(scrolly,newLabel,current_page)
	eventBox.set_events(gtk.gdk.BUTTON_PRESS_MASK)
	eventBox.connect("button_press_event",button_press_event)
	kids = eventBox.get_children()
	pixm = kids[0].get_pixmap()
	self.notebook.show_all()

def button_press_event(widget,event):
	global count
	if count==0:
		global x
		x = event.x
		global y
		y = event.y
		count+=1
	else:
		flipped = False
		a = event.x
		b = event.y
		global w
		global h
		w = a-x
		if w<0:
			w=x-a
			flipped = True
		h = b-y
		if h<0:
			h=y-b
			if not flipped:
				flipped = True
		kid = widget.get_children()
		pixm = kid[0].get_pixmap()
		drawable = pixm[0]
		gc = drawable.new_gc()
		if not flipped:
			drawable.draw_rectangle(gc,False,int(x),int(y),int(w),int(h))
		else:
			drawable.draw_rectangle(gc,False,int(a),int(b),int(w),int(h))
		widget.queue_draw()
		global ocr_ready
		ocr_ready = True
		count = 0

def do_ocr(self,filename):
	current=self.notebook.get_current_page()
	tm=self.treeview.get_model()
	iter=tm.get_iter(current)
	number_pages=tm.get_value(iter,3)
	current_page=tm.get_value(iter,4)
	path_filename="\""+filename+"\""
	global ocr_ready
	if ocr_ready is True:
		global x
		global y
		global w
		global h
		temp_filename=filename.split(".")
		if number_pages>1:
			new_file=temp_filename[0]+str(current_page)+".tif"
			print "\nNew filename:"+new_file+"\n"
		else:
			new_file=temp_filename[0]+".tif"
		picture = gtk.gdk.pixbuf_new_from_file(new_file)
		path_new_file="\""+new_file+"\""
		pic_W,pic_H = picture.get_width(), picture.get_height()
		os.system("gm convert -size "+str(pic_W)+"x"+str(pic_H)+" -depth 8 -crop "+str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)+" \""+new_file+"\" newcropped.tif")
		os.system("tesseract newcropped.tif new_file")
	else:
		temp_filename=filename.split(".")
		if temp_filename[1] is ".tif":
			os.system("tesseract "+filename+" new_file")
		else:
			return

def next_page(filename):
		picture = gtk.gdk.pixbuf_new_from_file(filename)