#Add To End
import app
if app.__BL_WINDOW_AUTO_HIDE__:
	window["children"][0]["children"] += (
		{
			"name": "auto_hide",
			"type": "text",

			"x": 40 + TEXT_TEMPORARY_X,
			"y": 210 + 2,

			"text": uiScriptLocale.OPTION_AUTO_HIDE,
		},
		{
			"name": "auto_hide_on",
			"type": "radio_button",

			"x": 110,
			"y": 210,

			"text": uiScriptLocale.OPTION_AUTO_HIDE_ON,

			"default_image": ROOT_PATH + "middle_button_01.sub",
			"over_image": ROOT_PATH + "middle_button_02.sub",
			"down_image": ROOT_PATH + "middle_button_03.sub",
		},
		{
			"name": "auto_hide_off",
			"type": "radio_button",

			"x": 110 + 70,
			"y": 210,

			"text": uiScriptLocale.OPTION_AUTO_HIDE_OFF,

			"default_image": ROOT_PATH + "middle_button_01.sub",
			"over_image": ROOT_PATH + "middle_button_02.sub",
			"down_image": ROOT_PATH + "middle_button_03.sub",
		},
	)
