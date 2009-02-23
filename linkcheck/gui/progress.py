# -*- coding: iso-8859-1 -*-
# Copyright (C) 2009 Bastian Kleineidam
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import os
from PyQt4 import QtCore, QtGui
from .linkchecker_ui_progress import Ui_ProgressDialog


def set_fixed_font (output):
    """Set fixed font on output widget."""
    if os.name == 'nt':
        output.setFontFamily("Courier")
    else:
        output.setFontFamily("mono")


class LinkCheckerProgress (QtGui.QDialog, Ui_ProgressDialog):
    """Show progress bar."""

    def __init__ (self, parent=None):
        super(LinkCheckerProgress, self).__init__(parent)
        self.setupUi(self)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        set_fixed_font(self.textBrowser)

    def log_status (self, checked, in_progress, queued, duration):
        self.label_checked.setText(u"%d" % checked)
        self.label_active.setText(u"%d" % in_progress)
        self.label_queued.setText(u"%d" % queued)

    def log_msg (self, msg):
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text+msg)
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)

    def reset (self):
        self.tabWidget.setCurrentIndex(0)
        self.textBrowser.setText(u"")
        self.label_active.setText(u"0")
        self.label_queued.setText(u"0")
        self.label_checked.setText(u"0")


class StatusLogger (object):
    """GUI status logger, printing to progress dialog."""

    def __init__ (self, widget):
        self.widget = widget

    def print_status (self, checked, in_progress, queued, duration):
        self.widget.emit(QtCore.SIGNAL("log_url(int,int,int,float)"), checked, in_progress, queued, duration)
