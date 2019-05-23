from Spotfire.Dxp.Application.Scripting import ScriptDefinition
from System.Collections.Generic import Dictionary
import clr

scriptDef = clr.Reference[ScriptDefinition]()
Document.ScriptManager.TryGetScript("fltResetDate", scriptDef) # fltResetDate should be replaced
params = Dictionary[str, object]()
Document.ScriptManager.ExecuteScript(scriptDef.ScriptCode, params)

#Example on how to call a script (Another Example)
from System.Collections.Generic import Dictionary
from Spotfire.Dxp.Application.Scripting import ScriptDefinition
import clr

scriptDef = clr.Reference[ScriptDefinition]()
Document.ScriptManager.TryGetScript("Name of Script", scriptDef)
paramDict = {"MyParam":"Value1", 
	"Parameter2":"Value2"} 
params = Dictionary[str, object](paramDict)
Document.ScriptManager.ExecuteScript(scriptDef.ScriptCode, params)
