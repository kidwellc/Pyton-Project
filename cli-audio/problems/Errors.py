import curses
import curses.textpad

import sys

class CLI_Audio_Exception(Exception):
    """Base class for other exceptions"""
    
    pass

class CLI_Audio_File_Exception (CLI_Audio_Exception):
    """Raised for file errors"""
    
    pass

class CLI_Audio_Screen_Size_Exception(CLI_Audio_Exception):
    """Raised for window size errors"""
    
    pass