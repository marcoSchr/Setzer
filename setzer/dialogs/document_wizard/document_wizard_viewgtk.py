#!/usr/bin/env python3
# coding: utf-8

# Copyright (C) 2017-present Robert Griesel
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GLib, Gdk, GdkPixbuf

import os


class DocumentWizardView(object):
    ''' Create document templates for users to build on. '''

    def __init__(self, main_window):
        builder = Gtk.Builder.new_from_string('<?xml version="1.0" encoding="UTF-8"?><interface><object class="GtkDialog" id="dialog"><property name="use-header-bar">1</property></object></interface>', -1)

        self.dialog = builder.get_object('dialog')
        self.dialog.set_modal(True)
        self.dialog.set_transient_for(main_window)
        self.dialog.set_destroy_with_parent(True)
        self.dialog.set_default_size(750, 500)
        self.topbox = self.dialog.get_content_area()
        self.topbox.set_size_request(750, 450)
        self.center_box = Gtk.CenterBox()
        self.center_box.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.pages = list()

        self.title_label = Gtk.Label.new(_('Create a template document'))
        self.title_label.get_style_context().add_class('title')
        self.subtitle_label = Gtk.Label.new('')
        self.subtitle_label.get_style_context().add_class('subtitle')

        self.title_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        self.title_box.append(self.title_label)
        self.title_box.append(self.subtitle_label)

        self.title_widget = Gtk.CenterBox()
        self.title_widget.set_orientation(Gtk.Orientation.VERTICAL)
        self.title_widget.set_center_widget(self.title_box)

        self.headerbar = self.dialog.get_header_bar()
        self.headerbar.set_show_title_buttons(False)
        self.headerbar.set_title_widget(self.title_widget)

        self.cancel_button = self.dialog.add_button(_('_Cancel'), Gtk.ResponseType.CANCEL)
        self.cancel_button.set_can_focus(False)
        self.back_button = Gtk.Button.new_with_mnemonic(_('_Back'))
        self.back_button.set_can_focus(False)
        
        self.next_button = Gtk.Button.new_with_mnemonic(_('_Next'))
        self.next_button.set_can_focus(False)
        self.next_button.get_style_context().add_class('suggested-action')
        self.create_button = self.dialog.add_button(_('_Create'), Gtk.ResponseType.APPLY)
        self.create_button.set_can_focus(False)
        self.create_button.get_style_context().add_class('suggested-action')

        self.headerbar.pack_start(self.back_button)
        self.headerbar.pack_end(self.next_button)

        self.notebook = Gtk.Notebook()
        self.notebook.set_show_tabs(False)
        self.notebook.set_show_border(False)
        self.center_box.set_center_widget(self.notebook)
        self.topbox.append(self.center_box)


