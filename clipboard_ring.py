import sublime, sublime_plugin
from Default.paste_from_history import *

class CycleClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if (g_clipboard_history.empty()):
			return

		clipboard_value = ci.next()

		for selection in self.view.sel():
			self.view.replace(edit, selection, clipboard_value)


class CycleClipboardListener(sublime_plugin.EventListener):
	def on_selection_modified(self, view):
		if not ci.cycling:
			return

		for selection in view.sel():
			text = view.substr(selection)
			if (not text == ci.current()):
				g_clipboard_history.push_text(ci.current())
				ci.reset()


class ClipboardIterator():
	cycling = False
	def __init__(self):
		self.reset()

	def next(self):
		if (self.index == (len(g_clipboard_history.storage)-1)):
			self.reset()

		self.cycling = True
		self.index += 1

		return self.current()

	def current(self):
		return g_clipboard_history.storage[self.index][1]

	def reset(self):
		self.cycling = False
		self.index = -1


ci = ClipboardIterator()