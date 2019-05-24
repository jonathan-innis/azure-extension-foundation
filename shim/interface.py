from shim import Shim
import sys, json

def create_manifest(version_num = 1.0, reboot_after_install = False, report_heartbeat = True):
    data = {
        "version": float(version_num),
        "handler_manifest": {
            "installCommaned": "python %s install"%("interface.py"),
            "uninstallCommand": "python %s uninstall"%("interface.py"),
            "updateCommand": "python %s update"%("interface.py"),
            "enableCommand": "python %s enable"%("interface.py"),
            "disableCommand": "python %s disable"%("interface.py"),
            "rebootAfterInstall": reboot_after_install,
            "reportHearbeat": report_heartbeat,
        }
    }
    with open('HandlerManifest.json', 'w') as outfile:
        json.dump(data, outfile)



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
        if cmd == "create":
            create_manifest()
        elif cmd == "install":
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