//Find
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif

///Add
#if defined(__BL_WINDOW_AUTO_HIDE__)
	PyModule_AddIntConstant(poModule, "__BL_WINDOW_AUTO_HIDE__", true);
#else
	PyModule_AddIntConstant(poModule, "__BL_WINDOW_AUTO_HIDE__", false);
#endif