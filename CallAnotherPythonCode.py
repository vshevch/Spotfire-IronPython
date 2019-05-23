from Spotfire.Dxp.Application.Scripting import ScriptDefinition
from System.Collections.Generic import Dictionary
import clr

scriptDef = clr.Reference[ScriptDefinition]()
Document.ScriptManager.TryGetScript("fltResetDate", scriptDef) # fltResetDate should be replaced
params = Dictionary[str, object]()
Document.ScriptManager.ExecuteScript(scriptDef.ScriptCode, params)
