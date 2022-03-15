#Find
	def OnChangeCurrentSkill(self, skillSlotNumber):
		...

#Add
	if app.__BL_WINDOW_AUTO_HIDE__:
		def IsOpenRightLeftMouseButtonWindow(self):
			wndMouseButtonMode = self.mouseModeButtonList[self.MOUSE_BUTTON_LEFT]
			if wndMouseButtonMode and wndMouseButtonMode.IsShow():
				return True

			wndMouseButtonMode = self.mouseModeButtonList[self.MOUSE_BUTTON_RIGHT]
			if wndMouseButtonMode and wndMouseButtonMode.IsShow():
				return True

			if self.mouseImage and self.mouseImage.IsShow():
				return True

			return False