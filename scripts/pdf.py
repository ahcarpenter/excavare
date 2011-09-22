#!/usr/bin/python
#Drew Carpenter & Jeff Gullett
#CS 4444

import gtk
import poppler
import sys
import cairo
import os
import gobject

def get_pdf(self, uri):
    uri = self.tabFileDictionary[str(self.fileDisplayArea.get_current_page())]
    uri = "file://" + os.path.realpath(uri)
    self.document = poppler.document_new_from_file (uri, None)
    self.n_pages = self.document.get_n_pages()

    self.current_page = self.document.get_page(int(self.page))
    self.width, self.height = self.current_page.get_size()
    self.total_pages = self.document.get_n_pages()
    virtualThread(self)

def on_changed(self):
    self.current_page = self.document.get_page(int(self.page))
    self.pdfda.set_size_request(int(self.width) * self.scale, int(self.height) * self.scale)
    self.pdfda.queue_draw()
    
def on_scale_changed(self):
    print self.scale
    self.pdfda.set_size_request(int(self.width) * self.scale, int(self.height) * self.scale)
    self.pdfda.queue_draw()
    
def on_expose(self, widget, event):
    cr = widget.window.cairo_create()
    cr.set_source_rgb(1, 1, 1)
        
    if self.scale != 1:
        cr.scale(self.scale, self.scale)
        
    cr.rectangle(0, 0, self.width, self.height)
    cr.fill()
    self.current_page.render(cr)
    
def on_scan_fonts(self, widget):
    font_info = poppler.FontInfo(self.document)
    iter = font_info.scan(self.n_pages)
        
    print iter.get_full_name()
        
    while iter.next():
        print iter.get_full_name()
        
def on_next(self, widget):
    if self.page is not self.total_pages-1:
        self.page = self.page + 1
    
    on_changed(self)
    
def on_previous(self, widget):
    if self.page > 0:
        self.page = self.page - 1
    on_changed(self)
    
def updatePageIndex(self):
    #print self.pageIndicator.get_text()
    while ("(" + str(self.page) + str(self.total_pages) + ")" is not self.pageIndicator.get_label()): #place conditional here that checks whether temp file exists,
        self.pageIndicator.set_text("(" + str(self.page+1) + " of " + str(self.total_pages) + ")")     #while temp file !exist show progress bar animation
        #print "after" + self.pageIndicator.get_text()
        yield True
    self.excavare.show()
    
def virtualThread(self):
    task = updatePageIndex(self)   #place the function callback here for when it's idle
    gobject.idle_add(task.next)


