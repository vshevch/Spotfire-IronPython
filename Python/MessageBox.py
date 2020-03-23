# Python Script for creating a Message Box in Spotfire

import clr
clr.AddReference("System.Windows.Forms")
 
from System.Windows.Forms import MessageBox
MessageBox.Show("This is a message box")
