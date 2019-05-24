from shim import Shim

TIMEOUT = False

class Override(Shim):
    def install(self):
        print("installing")
    
    def enable(self):
        print("enabling")

def main():
    override = Override()
    override.install()
    override.enable()

if __name__ == "__main__":
    main()