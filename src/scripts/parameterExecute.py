# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.
import webbrowser

def onPulse(par):
	if par.name == "Gotorepository":
		url = "https://github.com/JohnENoonan/touch-state-storage"
		webbrowser.open(url, new=2)

	elif par.name == "Createdefaults":
		defaults_op = "storage_defaults"
		base = parent()
		op.log.Debug(base)
		if (len(base.docked) == 0):
			op.log.Verbose("Create docked defaults")
			new_def_dat = base.parent().create(tableDAT, defaults_op)
			new_def_dat.nodeX = base.nodeX
			new_def_dat.nodeY = base.nodeY - 150
			new_def_dat.dock = base
			new_def_dat.viewer = True


