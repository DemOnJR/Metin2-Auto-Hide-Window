#Find
		self.ctrlShadowQuality = 0

#Add
		if app.__BL_WINDOW_AUTO_HIDE__:
			self.autoHideModeButtonList = []

#Find
			self.tilingModeButtonList.append(GetObject("tiling_gpu"))

#Add
			if app.__BL_WINDOW_AUTO_HIDE__:
				self.autoHideModeButtonList.append(GetObject("auto_hide_on"))
				self.autoHideModeButtonList.append(GetObject("auto_hide_off"))

#Find
		self.tilingModeButtonList[1].SAFE_SetEvent(self.__OnClickTilingModeGPUButton)

#Add
		if app.__BL_WINDOW_AUTO_HIDE__:
			self.autoHideModeButtonList[0].SAFE_SetEvent(self.__OnClickAutoHideModeOnButton)
			self.autoHideModeButtonList[1].SAFE_SetEvent(self.__OnClickAutoHideModeOffButton)
			self.__ClickRadioButton(self.autoHideModeButtonList, 1)

#Find
	def __OnClickTilingModeGPUButton(self):
		...

#Add
	if app.__BL_WINDOW_AUTO_HIDE__:
		def __OnClickAutoHideModeOnButton(self):
			self.__ClickRadioButton(self.autoHideModeButtonList, 0)
			constInfo.AUTO_HIDE_OPTION = True

		def __OnClickAutoHideModeOffButton(self):
			self.__ClickRadioButton(self.autoHideModeButtonList, 1)
			constInfo.AUTO_HIDE_OPTION = False