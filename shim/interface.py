from shim import Shim
import sys, json

# Functions to be overridden with the application logic for the extensions
class Interface(Shim):
    def install(self):
        pass
    
    def enable(self):
        pass
    
    def disable(self):
        pass
    
    def uninstall(self):
        pass
    
    def handle_cmd(self, cmd):
        if cmd == "install":
            self.pre_install()
            self.install()
            self.post_install()
        elif cmd == "enable":
            shouldProcess = self.sequence.check_sequence_number()
            if shouldProcess:
                self.pre_enable()
                self.enable()
                self.post_enable()
        elif cmd == "disable":
            self.pre_disable()
            self.disable()
            self.post_disable()
        elif cmd == "uninstall":
            self.pre_uninstall()
            self.uninstall()
            self.post_uinstall()

def main():
    assert len(sys.argv) == 2
    extension_interface = Interface()
    extension_interface.handle_cmd(sys.argv[1])

if __name__ == "__main__":
    main()