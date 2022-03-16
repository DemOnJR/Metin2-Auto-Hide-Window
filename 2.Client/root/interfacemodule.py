#Find
			self.wndEnergyBar = wndEnergyBar

#Add
		if app.__BL_WINDOW_AUTO_HIDE__:
			(xConstPosTaskbar, self.yConstPosTaskbar) = self.wndTaskBar.GetLocalPosition()
			(xConstPosEnergyBar, self.yConstPosEnergyBar) = self.wndEnergyBar.GetLocalPosition()

#Find
	def BUILD_OnUpdate(self):
		if not self.wndGuildBuilding:
			return

		if self.wndGuildBuilding.IsPositioningMode():
			import background
			x, y, z = background.GetPickingPoint()
			self.wndGuildBuilding.SetBuildingPosition(x, y, z)
			
#Change
	def BUILD_OnUpdate(self):
		if app.__BL_WINDOW_AUTO_HIDE__:
			xMouse, yMouse = wndMgr.GetMousePosition()
			xWidth = wndMgr.GetScreenWidth()
			yHeight = wndMgr.GetScreenHeight()

			if self.wndMiniMap:
				(xCurrentMinimap, yCurrentMinimap) = self.wndMiniMap.GetLocalPosition()
				if (xWidth - 150 <= xMouse <= xWidth and 0 <= yMouse <= 135) or \
						constInfo.AUTO_HIDE_OPTION == False:
					if xCurrentMinimap > xWidth - self.wndMiniMap.GetWidth():
						self.wndMiniMap.SetPosition(max(xCurrentMinimap - 10, xWidth - self.wndMiniMap.GetWidth()), yCurrentMinimap)
				else:
					if xCurrentMinimap < xWidth:
						self.wndMiniMap.SetPosition(min(xCurrentMinimap + 10, xWidth), yCurrentMinimap)

			if self.wndTaskBar and self.wndTaskBar.IsShow() and \
					self.wndExpandedTaskBar and \
					self.wndEnergyBar and \
					self.wndChat:
				(xCurrentTaskbar, yCurrentTaskbar) = self.wndTaskBar.GetLocalPosition()
				(xCurrentEnergyBar, yCurrentEnergyBar) = self.wndEnergyBar.GetLocalPosition()
				(xCurrentChat, yCurrentChat) = self.wndChat.GetLocalPosition()

				if yHeight - 90 <= yMouse <= yHeight or \
						self.IsOpenChat() or \
						self.wndExpandedTaskBar.IsShow() or \
						self.wndTaskBar.IsOpenRightLeftMouseButtonWindow() or \
						constInfo.AUTO_HIDE_OPTION == False:
					if yCurrentTaskbar > self.yConstPosTaskbar:
						self.wndTaskBar.SetPosition(xCurrentTaskbar, max(yCurrentTaskbar - 5, self.yConstPosTaskbar))
					if yCurrentEnergyBar > self.yConstPosEnergyBar:
						self.wndEnergyBar.SetPosition(xCurrentEnergyBar, max(yCurrentEnergyBar - 5, self.yConstPosEnergyBar))
					if yCurrentChat > yHeight - self.wndChat.EDIT_LINE_HEIGHT - 37:
						self.wndChat.SetPosition(xCurrentChat, max(yCurrentChat - 3, yHeight - self.wndChat.EDIT_LINE_HEIGHT - 37))
						self.wndChat.Refresh()
				else:
					if yCurrentTaskbar < self.yConstPosTaskbar + 65:
						self.wndTaskBar.SetPosition(xCurrentTaskbar, min(yCurrentTaskbar + 5, self.yConstPosTaskbar + 65))
					if yCurrentEnergyBar < self.yConstPosEnergyBar + 65:
						self.wndEnergyBar.SetPosition(xCurrentEnergyBar, min(yCurrentEnergyBar + 5, self.yConstPosEnergyBar + 65))
					if yCurrentChat < yHeight - self.wndChat.EDIT_LINE_HEIGHT:
						self.wndChat.SetPosition(xCurrentChat, min(yCurrentChat + 3, yHeight - self.wndChat.EDIT_LINE_HEIGHT))
						self.wndChat.Refresh()

		if not self.wndGuildBuilding:
			return

		if self.wndGuildBuilding.IsPositioningMode():
			import background
			x, y, z = background.GetPickingPoint()
			self.wndGuildBuilding.SetBuildingPosition(x, y, z)