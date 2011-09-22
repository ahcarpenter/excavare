#!/usr/bin/python
#Drew Carpenter & Jeff Gullett
#CS 4444

import sys
import gtk
import filter
import os
import misc
import pdf
import docx_to_text
from workspace import *
from tabs import *

class ExcavareMain:
	
	#Handlers
	
	def on_Excavare_destroy(self, widget, data=None):
	 	"""Destroys the excavare window"""
		gtk.main_quit()
	
	def on_widget_delete_event(self, widget, event):
		widget.hide()
		return True
	
	def key_press_event(self, widget, event):
		keyname = gtk.gdk.keyval_name(event.keyval)
		if "Return" in keyname or "Esc" in keyname:
			print "hello"
			
	def on_treeview1_row_activated(self,treeview,something,something2):
		"""This function is called when a row is clicked in the treeview"""
		list_sel = self.treeview.get_selection()
		(tm, ti) = list_sel.get_selected()
		self.notebook.set_current_page((tm.get_value(ti, 1)))
		self.notebook.show_all()
	
	def on_ocr_tool_clicked(self,ocr_tool):
		"""Performs OCR on current tab."""
		current=self.notebook.get_current_page()
		tm=self.treeview.get_model()
		iter=tm.get_iter(current)
		filename=tm.get_value(iter,2)
		drawable.do_ocr(self,filename)
	
	def on_ocr_activate(self,ocr_menu_item):
		"""Performs OCR on current tab."""
		current=self.notebook.get_current_page()
		tm=self.treeview.get_model()
		iter=tm.get_iter(current)
		filename=tm.get_value(iter,2)
		drawable.do_ocr(self,filename)
	
	def on_save_menu_item_activate(self,save_menu_item):
		current=self.notebook.get_current_page()
		tm=self.treeview.get_model()
		iter=tm.get_iter(current)
		saved_once=tm.get_value(iter,5)
		file1=tm.get_value(iter,2)
		if file1 is not None:
			extType=file1.split(".")
			if extType[-1] != "txt":
				warning = gtk.MessageDialog(parent=self.excavare, flags=0, type=gtk.MESSAGE_WARNING, buttons=gtk.BUTTONS_OK_CANCEL, message_format="You are trying to save a file of type "+extType[-1]+".\nExcavare cannot save this file type. If you would like to save what you have as a plain text file (.txt) press OK.\nThe original file has not been changed.")
				warn = warning.run()
				if warn ==gtk.RESPONSE_CANCEL:
					warning.destroy()
					return
				else:
					warning.destroy()
		if saved_once is False:
			filesel = gtk.FileChooserDialog(title='Save',parent=self.excavare,action=gtk.FILE_CHOOSER_ACTION_SAVE,buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE,gtk.RESPONSE_OK))
			filesel.set_default_response(gtk.RESPONSE_OK)
			file_action=filesel.run()
			if file_action==gtk.RESPONSE_OK:
				scrolly=self.notebook.get_focus_child()
				view=scrolly.get_child()
				texty=view.get_child()
				buffy=texty.get_buffer()
				start=buffy.get_start_iter()
				end=buffy.get_end_iter()
				all_text=buffy.get_text(start,end)
				name=filesel.get_filename()
				extension=name.split(".")
				if len(extension)==1:
					temp_name=name+".txt"
				if extension[-1]!=".txt":
					temp_name=extension[0]+".txt"
				else:
					temp_name=name
				finalNameList=temp_name.split("/")
				if len(finalNameList)==1:
					finalNameList=temp_name.split("\\")
				finalName=finalNameList[-1]
				if os.path.exists(finalName):
					warning = gtk.MessageDialog(parent=filesel, flags=0, type=gtk.MESSAGE_WARNING, buttons=gtk.BUTTONS_OK_CANCEL, message_format="The file already exists. Are you sure you want to repace it?")
					warn = warning.run()
					if warn ==gtk.RESPONSE_CANCEL:
						warning.destroy()
						return
					else:
						#erase the file
						erase = open(finalName,"w").close()
						warning.destroy()
				filesel.destroy()
				new_file = open(finalName,"w")
				new_file.write(all_text)
				new_file.close()
				current=self.notebook.get_current_page()
				tm=self.treeview.get_model()
				iter=tm.get_iter(current)
				tm.set_value(iter,0,finalName)
				tm.set_value(iter,2,finalName)
				tm.set_value(iter,5,True)
			if file_action == gtk.RESPONSE_CANCEL:
				#if cancel is clicked, destroy file chooser dialog
				filesel.destroy()
		else:
			scrolly=self.notebook.get_focus_child()
			view=scrolly.get_child()
			texty=view.get_child()
			buffy=texty.get_buffer()
			start=buffy.get_start_iter()
			end=buffy.get_end_iter()
			all_text=buffy.get_text(start,end)
			finalName=tm.get_value(iter,2)
			new_file = open(finalName,"w")
			new_file.write(all_text)
			new_file.close()
	
	def on_back_button_clicked(self,back_button):
		current=self.notebook.get_current_page()
		tm=self.treeview.get_model()
		iter=tm.get_iter(current)
		num_pages=tm.get_value(iter,3)
		self.current_page=tm.get_value(iter,4)
		if self.current_page==0:
			return
		else:
			self.current_page=self.current_page-1
			tm.set_value(iter,4,self.current_page)			
			filename=tm.get_value(iter,2)
			filename=filename+"x"
			temp_filename=list(filename)
			temp_filename[-5]=str(self.current_page)
			temp_filename[-4]="."
			temp_filename[-3]="t"
			temp_filename[-2]="i"
			temp_filename[-1]="f"
			filename="".join(temp_filename)
			scrolly=self.notebook.get_focus_child()
			view=scrolly.get_child()
			event=view.get_child()
			image = gtk.Image()
			image.set_alignment(0,0)
			image.set_padding(0,0)
			picture = gtk.gdk.pixbuf_new_from_file(filename)
			w,h = picture.get_width(), picture.get_height()
			drawable = gtk.gdk.Pixmap(None, w, h, 24)
			gc = drawable.new_gc()
			drawable.draw_pixbuf(gc, picture, 0,0,0,0,-1,-1)
			image.set_from_pixmap(drawable,None)
			child=event.get_child()
			event.remove(child)
			event.add(image)
			event.queue_draw()
			self.notebook.show_all()
	
	def on_forward_button_clicked(self,forward_button):
		current=self.notebook.get_current_page()
		tm=self.treeview.get_model()
		iter=tm.get_iter(current)
		num_pages=tm.get_value(iter,3)
		self.current_page=tm.get_value(iter,4)		
		if self.current_page==(num_pages-1):
			return
		else:
			self.current_page+=1
			tm.set_value(iter,4,self.current_page)
			filename=tm.get_value(iter,2)
			filename=filename+"x"
			temp_filename=list(filename)
			temp_filename[-5]=str(self.current_page)
			temp_filename[-4]="."
			temp_filename[-3]="t"
			temp_filename[-2]="i"
			temp_filename[-1]="f"
			filename="".join(temp_filename)
			scrolly=self.notebook.get_focus_child()
			view=scrolly.get_child()
			event=view.get_child()
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
			child=event.get_child()
			event.remove(child)
			event.add(image)
			event.queue_draw()
			self.notebook.show_all()
	
	def on_open_menu_item_activate(self,widget):
		self.fileNavigator.show()

	def on_save_workspace_item_activate(self,save_workspace_item):
		if self.is_workspace is False:
			filesel = gtk.FileChooserDialog(title='Save Workspace',parent=self.excavare,action=gtk.FILE_CHOOSER_ACTION_SAVE,buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE,gtk.RESPONSE_OK))
			filesel.set_default_response(gtk.RESPONSE_OK)
			file_action=filesel.run()
			if file_action==gtk.RESPONSE_OK:
				name=filesel.get_filename()
				extension=name.split(".")
				if len(extension)==1:
					temp_name=name+".wksp"
				if extension[-1]!="wksp":
					temp_name=extension[0]+".wksp"
				else:
					temp_name=name
				finalNameList=temp_name.split("/")
				if len(finalNameList)==1:
					finalNameList=temp_name.split("\\")
				finalName=finalNameList[-1]
				if os.path.exists(finalName):
					warning = gtk.MessageDialog(parent=filesel, flags=0, type=gtk.MESSAGE_WARNING, buttons=gtk.BUTTONS_OK_CANCEL, message_format="The file already exists. Are you sure you want to repace it?")
					warn = warning.run()
					if warn ==gtk.RESPONSE_CANCEL:
						warning.destroy()
						return
					else:
						#erase the file
						erase = open(finalName,"w").close()
						warning.destroy()
				filesel.destroy()
				workspace = open(finalName,"w")
				self.excavare.set_title(finalName)
				workspace.write("title\t"+temp_name)
				workspace.write("\ntab_numbers\t"+str(self.tab_nums))
				model=self.treeview.get_model()
				iter=model.get_iter_first()
				file_entry=model.get_value(iter,2)
				workspace.write("\n"+file_entry)
				#workspace.write("\nTextEditor\t"+str(model.get_value(iter,2)))
				if iter is not None:
					for i in range(0,self.tab_nums):
						iter=model.iter_next(iter)
						if iter is not None:
							workspace.write("\n")
							file_entry=model.get_value(iter,2)
							workspace.write(file_entry)
						else:
							break
				workspace.close()
				self.is_workspace=True
			else:
				filesel.destroy()
		else:
			finalName=self.excavare.get_title()
			file = open(finalName,"r")
			first_line=file.readline()
			line=first_line.split("\t")
			temp_name=line[-1]
			file.close()
			erase = open(finalName,"w").close()
			workspace = open(finalName,"w")
			workspace.write("title\t"+temp_name)
			workspace.write("tab_numbers\t"+str(self.tab_nums))
			model=self.treeview.get_model()
			iter=model.get_iter_first()
			workspace.write("\nTextEditor\t"+str(model.get_value(iter,2)))
			if iter is not None:
				for i in range(0,self.tab_nums):
					iter=model.iter_next(iter)
					if iter is not None:
						workspace.write("\n")
						file_entry=model.get_value(iter,2)
						workspace.write(file_entry)
					else:
						break
			workspace.close()			

	def on_new_menu_item_activate(self,new_menu_item):
		newScrolledWindow,newTextView=create_scrolled_window()
		newTab=gtk.Label("new")
		self.notebook.append_page(newScrolledWindow,newTab)
		self.tab_nums=self.tab_nums+1
		self.textviews.append(newTextView)
		self.list_store.append(["new",self.tab_nums,None,1,0,False])
		self.notebook.show_all()

	def __init__(self):
		builder = gtk.Builder()
		builder.add_from_file("interface.glade")
		
		#Interface configuration options
		
		settings = gtk.settings_get_default()
		settings.props.gtk_button_images = True
		self.excavare = builder.get_object("Excavare")
		self.excavare.set_title("Excavare")
		self.excavare.maximize()
		self.pdfda = builder.get_object("pdfda")
		self.pageIndicator = builder.get_object("pageIndicator")
		self.fileDisplayArea = builder.get_object("fileDisplayArea")
		self.pdfDisplayArea = builder.get_object("pdfDisplayArea")
		self.tab_name = builder.get_object("tab_name")
		self.tab_widget = builder.get_object("tab_widget")
		self.tabFileDictionary = {None:None}
		self.scrolledwindow2 = builder.get_object("scrolledwindow2")
		self.total_pages = 0
		self.current_selection = None
		self.treeview = builder.get_object("treeview1")
		self.pdfda = builder.get_object("pdfda")
		self.fileNavigator = builder.get_object("fileNavigator")
		self.list_store = gtk.ListStore(str,int,str,int,int,bool)
		self.treeview.set_model(self.list_store)
		self.notebook = builder.get_object("notebook1")
		self.column = gtk.TreeViewColumn('Files')
		self.treeview.append_column(self.column)
		self.cell = gtk.CellRendererText()
		self.column.pack_start(self.cell, True)
		self.column.set_attributes(self.cell, text=0)
		self.tab_nums = -1
		self.page=0
		self.scale = 1
		self.is_workspace=False
		builder.connect_signals(self)
		self.textviews = []
		
	#renders a PDF on screen when opened
		
	def pdf_render(self, widget, event):
		pdfRead.get_pdf(self, self.current_selection)
		pdfRead.on_expose(self, widget,event)
	
	def on_next(self, widget):

		pdfRead.on_next(self, widget)
	
	def on_previous(self, widget):
		
		pdfRead.on_previous(self, widget)
	
	def on_scale_increased(self, widget):
		self.scale = self.scale + .5
		pdfRead.on_scale_changed(self)
	
	def on_scale_decreased(self, widget):
		if self.scale > 1:
			self.scale = self.scale -.5
		pdfRead.on_scale_changed(self)
		
	def on_file_select_ok_clicked(self, widget):
		create_tabs.create_tab(self, self.fileDisplayArea, self.current_selection)
		self.fileNavigator.hide()
		
	def current_selection_update(self, widget):
		self.current_selection = widget.get_filename()

if __name__ == "__main__":
	program = ExcavareMain()
	program.excavare.show()
	gtk.main()