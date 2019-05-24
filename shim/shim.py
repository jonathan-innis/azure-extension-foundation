from helper import log
from helper import status
from helper import settings
from helper import sequence
from abc import abstractmethod, ABCMeta
from ctypes import *

EXTENSION_NAME = "some extension"

class Shim(metaclass=ABCMeta):
    def __init__(self):
        lib = cdll.LoadLibrary("C:\\Users\\t-joinni\\go\\src\\github.com\\Azure\\azure-extension-foundation\\main\\main.so")
        ext_status = status.Status(lib)
        ext_sequence = sequence.Sequence(lib)
        ext_settings = settings.Settings(lib)

    """
    Install calls 
    """
    def pre_install(self):
        log.info("BEGIN Install Extension: %s"%(EXTENSION_NAME))
        ext_status.transitioning("BEGIN Install Extension: %s"%(EXTENSION_NAME), "BEGIN Install Extension: %s"%(EXTENSION_NAME))

    @abstractmethod
    def install(self):
        pass
    
    def post_install(self):
        log.info("END Install Extension %s"%(EXTENSION_NAME))
        ext_status.transitioning("END Install Extension: %s"%(EXTENSION_NAME), "END Install Extension: %s"%(EXTENSION_NAME)) 
    
    """
    Enable calls
    """
    def pre_enable(self):
        error = ext_sequence.update_sequence_number()
        if error is not None:
            log.error("Error updating the sequence number for the extension: %s"%(EXTENSION_NAME))
        log.info("BEGIN Enable Extension: %s"%(EXTENSION_NAME))
        ext_status.transitioning("BEGIN Enable Extension: %s"%(EXTENSION_NAME), "BEGIN Enable Extension: %s"%(EXTENSION_NAME))
        settings.update_settings()
    
    @abstractmethod
    def enable(self):
        pass
    
    def post_enable(self):
        log.info("END Enable Extension: %s"%(EXTENSION_NAME))
        ext_status.success("END Enable Extension: %s"%(EXTENSION_NAME), "END Enable Extension: %s"%(EXTENSION_NAME))
    
    """
    Disable calls
    """
    def pre_disable(self):
        log.info("BEGIN Disable Extension: %s"%(EXTENSION_NAME))
        ext_status.transitioning("BEGIN Disable Extension: %s"%(EXTENSION_NAME), "BEGIN Disable Extension: %s"(EXTENSION_NAME))
    
    @abstractmethod
    def disable(self):
        pass
    
    def post_disable(self):
        log.info("END Disable Extension %s"%(EXTENSION_NAME))
        ext_status.success("END Disable Extension: %s"%(EXTENSION_NAME), "END Disable Extension: %s"%(EXTENSION_NAME))

    """
    Uninstall calls
    """
    def pre_uninstall(self):
        log.info("BEGIN Uninstall Extension: %s"%(EXTENSION_NAME))
        ext_status.transitioning("BEGIN Uninstall Extension: %s"%(EXTENSION_NAME), "BEGIN Uninstall Extensions: %s"%(EXTENSION_NAME))
    
    @abstractmethod
    def uninstall(self):
        pass
    
    def post_uinstall(self):
        log.info("END Uninstall Extension: %s"%(EXTENSION_NAME))
        ext_status.transitioning("END Uninstall Extension: %s"%(EXTENSION_NAME), "END Uninstall Extension: %s"%(EXTENSION_NAME))

    def on_timeout(self):
        log.error("Extension install took to long for Extension: %s"%(EXTENSION_NAME))
        ext_status.error("Enabling failed for extension: %s"%(EXTENSION_NAME), "failed installing %s"%(EXTENSION_NAME))
    
    