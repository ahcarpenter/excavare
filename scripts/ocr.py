#!/usr/bin/python
#Drew Carpenter & Jeff Gullett
#CS 4444

import pygtk
import gtk
import sys
import drawable

def ocr_initialize(self,widget):
                self.doing_ocr=True
                current=self.notebook.get_current_page()
                tm=self.treeview.get_model()
                iter=tm.get_iter(current)
                filename=tm.get_value(iter,2)
                self.filename=filename
                #drawable.do_ocr(self,filename)