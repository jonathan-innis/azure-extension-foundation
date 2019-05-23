from shim import Shim

TIMEOUT = False

class Override(Shim):
    def install(self):
        self.pre_install()
        # application logic here
        self.post_install()
    
    def enable(self):
        self.pre_enable()
        # application logic here
        if TIMEOUT:
            self.on_timeout()
        else:
            self.post_enable()

def main():
    override = Override()
    override.install()
    override.enable()

if __name__ == "__main__":
    main()