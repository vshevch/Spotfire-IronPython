# Call script without parameters
def callScript(scpName, permStatus):
	from Spotfire.Dxp.Application.Scripting import ScriptDefinition
	from System.Collections.Generic import Dictionary
	import clr
	# Code
	scriptDef = clr.Reference[ScriptDefinition]()
	Document.ScriptManager.TryGetScript(scpName, scriptDef)
	Document.ScriptManager.ExecuteScript(scriptDef.ScriptCode, Dictionary[str, object]())
callScript("scrTester")

# Call script with parameters
from System.Collections.Generic import Dictionary
from Spotfire.Dxp.Application.Scripting import ScriptDefinition
import clr

scriptDef = clr.Reference[ScriptDefinition]()
Document.ScriptManager.TryGetScript("Name of Script", scriptDef)
paramDict = {"MyParam":"Value1", 
	"Parameter2":"Value2"} 
params = Dictionary[str, object](paramDict)
Document.ScriptManager.ExecuteScript(scriptDef.ScriptCode, params)

# !! Important !!
# Your code will error out if it does not have a variable defined
# This code will create a variable if no code is defined
# Defining a variable in the target code will overwrite the parameter being passed

# - Method #1 -
try:
    var # Name of the variable
except NameError: # Empty variable generates NameError
    var = "variable value"

# - Method #2 -
for variable in ["value_EN", "ROM", "value_FR"]: # variables to check
	if variable not in locals(): 		 # if not local variable dictionary
		locals()[variable] = None 	 # Create a variable
