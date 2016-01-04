import sublime
import sublime_plugin
import re
import webbrowser

class FindPackageCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		region = view.sel()[0]
		if not region.empty():
			text = view.substr(region)
		else:
			selection = view.sel()[0]
			text = view.substr(view.line(selection))

		strings = re.findall(r"['\"](.*?)['\"]", text)
		if len(strings):
			package = strings[-1]
			url = "https://www.npmjs.com/package/{}".format(package)
			webbrowser.open_new_tab(url)
