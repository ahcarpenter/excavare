#!/usr/bin/python
#Drew Carpenter & Jeff Gullett
#CS 4444
#Excavare 0.0
#March 4,2011
import sys
import pygtk
import gtk

def filter_set (filesel):
	#create PDF Files filter
	filter = gtk.FileFilter()
	filter.set_name("PDF Files")
	filter.add_pattern("*.pdf")
	filesel.add_filter(filter)
	#create Text Files Filter
	filter = gtk.FileFilter()
	filter.set_name("Text Files")
	filter.add_pattern("*.txt")
	filesel.add_filter(filter)
	#create Image Files Filter
	filter = gtk.FileFilter()
	filter.set_name("Image Files")
	filter.add_pattern("*.jpeg")
	filter.add_pattern("*.jpg")
	filter.add_pattern("*.bmp")
	filter.add_pattern("*.gif")
	filesel.add_filter(filter)
	#create Word Files filter
	filter = gtk.FileFilter()
	filter.set_name("Word Files")
	filter.add_pattern("*.docx")
	filesel.add_filter(filter)	
	#create Workspace Filter
	filter = gtk.FileFilter()
	filter.set_name("Workspaces")
	filter.add_pattern("*.wksp")
	filesel.add_filter(filter)	
	#create All Files Filter
	filter = gtk.FileFilter()
	filter.set_name("All files")
	filter.add_pattern("*")
	filesel.add_filter(filter)