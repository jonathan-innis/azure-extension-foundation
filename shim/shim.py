from helper import log
from helper import status
from helper import settings

EXTENSION_NAME = "some extension"

class Shim:
    def pre_install(self):
        log.info("BEGIN Install Extension: %s"%(EXTENSION_NAME))
        status.transitioning("Installing extension: %s"%(EXTENSION_NAME), "installing %s"%(EXTENSION_NAME))
        return

    def install(self):
        pass
    
    def post_install(self):
        log.info("END Install Extension %s"%(EXTENSION_NAME))
        status.success("successfully installed extension: %s"%(EXTENSION_NAME), "successfully installed %s"%(EXTENSION_NAME))
        return 
    
    def pre_enable(self):
        log.info("BEGIN Enable Extension: %s"%(EXTENSION_NAME))
        status.transitioning("Enabling extension: %s"%(EXTENSION_NAME), "enabling %s"%(EXTENSION_NAME))
        settings.update_settings()
    
    def enable(self):
        pass
    
    def post_enable(self):
        log.info("END Enable Extension %s"%(EXTENSION_NAME))
        status.success("succesfully enabled extension: %s"%(EXTENSION_NAME), "succesfully enabled %s"%(EXTENSION_NAME))
    
    def on_timeout(self):
        log.error("Extension install took to long for Extension: %s"%(EXTENSION_NAME))
        status.error("Enabling failed for extension: %s"%(EXTENSION_NAME), "failed installing %s"%(EXTENSION_NAME))