from helper import log
from helper import status
from helper import settings

EXTENSION_NAME = "some extension"

class Shim:
    def __init__(self):
        lib = cdll.LoadLibrary("c:\\Users\\t-joinni\\go\\src\\github.com\\Azure\\azure-extension-foundation\\main\\main.so")
        extension_status = status.Status(lib)

    """
    Install calls 
    """
    def pre_install(self):
        log.info("BEGIN Install Extension: %s"%(EXTENSION_NAME))
        extension_status.transitioning("Installing extension: %s"%(EXTENSION_NAME), "installing %s"%(EXTENSION_NAME))

    def install(self):
        pass
    
    def post_install(self):
        log.info("END Install Extension %s"%(EXTENSION_NAME))
        extension_status.success("successfully installed extension: %s"%(EXTENSION_NAME), "successfully installed %s"%(EXTENSION_NAME)) 
    
    """
    Enable calls
    """
    def pre_enable(self):
        log.info("BEGIN Enable Extension: %s"%(EXTENSION_NAME))
        extension_status.transitioning("Enabling extension: %s"%(EXTENSION_NAME), "enabling %s"%(EXTENSION_NAME))
        settings.update_settings()
    
    def enable(self):
        pass
    
    def post_enable(self):
        log.info("END Enable Extension %s"%(EXTENSION_NAME))
        extension_status.success("succesfully enabled extension: %s"%(EXTENSION_NAME), "succesfully enabled %s"%(EXTENSION_NAME))
    
    """
    Disable calls
    """
    def pre_disable(self):
        log.info("BEGIN Disable Extension: %s"%(EXTENSION_NAME))
        extension_status.transitioning("Disabling extension: %s"%(EXTENSION_NAME), "disabling %s"(EXTENSION_NAME))
    
    def disable(self):
        pass
    
    def post_disable(self):
        log.info("END Disable Extension %s"%(EXTENSION_NAME))
        extension_status.success("succesfully disabled extension: %s"%(EXTENSION_NAME), "succesfully disabled %s"%(EXTENSION_NAME))

    def on_timeout(self):
        log.error("Extension install took to long for Extension: %s"%(EXTENSION_NAME))
        extension_status.error("Enabling failed for extension: %s"%(EXTENSION_NAME), "failed installing %s"%(EXTENSION_NAME))
    
    