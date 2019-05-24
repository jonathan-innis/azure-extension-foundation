from shim import Shim

class Override(Shim):
    def install(self):
        pass
    
    def enable(self):
        pass
    
    def disable(self):
        pass
    
    def uninstall(self):
        pass

def main():
    override = Override()

if __name__ == "__main__":
    main()