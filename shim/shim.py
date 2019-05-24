from helper import log, status, settings, sequence
from abc import abstractmethod, ABCMeta
from ctypes import *
import os

EXTENSION_NAME = "some extension"

class Shim(metaclass=ABCMeta):
    def __init__(self):
        lib = cdll.LoadLibrary(os.path.dirname(__file__) + "/main.so")
        self.status = status.Status(lib)
        self.sequence = sequence.Sequence(lib)
        self.settings = settings.Settings(lib)
        self.log = log.Log(lib)

        self.protected_settings = {}
        self.public_settings = {}

    """
    Install calls 
    """
    def pre_install(self):
        self.log.info("BEGIN Install Extension: %s"%(EXTENSION_NAME))
        self.status.transitioning("BEGIN Install Extension: %s"%(EXTENSION_NAME), "BEGIN Install Extension: %s"%(EXTENSION_NAME))

    @abstractmethod
    def install(self):
        pass
    
    def post_install(self):
        self.log.info("END Install Extension %s"%(EXTENSION_NAME))
        self.status.transitioning("END Install Extension: %s"%(EXTENSION_NAME), "END Install Extension: %s"%(EXTENSION_NAME)) 
    
    """
    Enable calls
    """
    def pre_enable(self):
        error = self.sequence.update_sequence_number()
        if error is not None:
            self.log.error("Error updating the sequence number for the extension: %s"%(EXTENSION_NAME))
        self.log.info("BEGIN Enable Extension: %s"%(EXTENSION_NAME))
        self.status.transitioning("BEGIN Enable Extension: %s"%(EXTENSION_NAME), "BEGIN Enable Extension: %s"%(EXTENSION_NAME))
        
        # Get settings to return back to the user to use in application logic
        self.protected_settings = self.settings.get_protected_settings()
        self.public_settings = self.settings.get_public_settings()
    
    @abstractmethod
    def enable(self):
        pass
    
    def post_enable(self):
        self.log.info("END Enable Extension: %s"%(EXTENSION_NAME))
        self.status.success("END Enable Extension: %s"%(EXTENSION_NAME), "END Enable Extension: %s"%(EXTENSION_NAME))
    
    """
    Disable calls
    """
    def pre_disable(self):
        self.log.info("BEGIN Disable Extension: %s"%(EXTENSION_NAME))
        self.status.transitioning("BEGIN Disable Extension: %s"%(EXTENSION_NAME), "BEGIN Disable Extension: %s"%(EXTENSION_NAME))
    
    @abstractmethod
    def disable(self):
        pass
    
    def post_disable(self):
        self.log.info("END Disable Extension %s"%(EXTENSION_NAME))
        self.status.success("END Disable Extension: %s"%(EXTENSION_NAME), "END Disable Extension: %s"%(EXTENSION_NAME))

    """
    Uninstall calls
    """
    def pre_uninstall(self):
        self.log.info("BEGIN Uninstall Extension: %s"%(EXTENSION_NAME))
        self.status.transitioning("BEGIN Uninstall Extension: %s"%(EXTENSION_NAME), "BEGIN Uninstall Extensions: %s"%(EXTENSION_NAME))
    
    @abstractmethod
    def uninstall(self):
        pass
    
    def post_uinstall(self):
        self.log.info("END Uninstall Extension: %s"%(EXTENSION_NAME))
        self.status.transitioning("END Uninstall Extension: %s"%(EXTENSION_NAME), "END Uninstall Extension: %s"%(EXTENSION_NAME))

    def on_timeout(self):
        self.log.error("Extension install took to long for Extension: %s"%(EXTENSION_NAME))
        self.status.error("Enabling failed for extension: %s"%(EXTENSION_NAME), "failed installing %s"%(EXTENSION_NAME))
    
    