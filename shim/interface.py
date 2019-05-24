from shim import Shim
import sys

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
            self.pre_enable()
            self.enable()
            self.post_enable()
        elif cmd == "enable":
            self.pre_enable()
            self.enable()
            self.post_enable()
        elif cmd == "disable":
            self.pre_disable()
            self.disable()
            self.post_disable()
        elif cmd == "uninstall":
            self.pre_disable()
            self.disable()
            self.post_disable()
            self.pre_uninstall()
            self.uninstall()
            self.post_uinstall()

def main():
    assert len(sys.argv) == 2
    extension_interface = Interface()
    extension_interface.handle_cmd(sys.argv[1])


if __name__ == "__main__":
    main()