from ctypes import *

class Settings:
    def __init__(self, lib):
        self.lib = lib
        self.lib.GetProtectedSettings.argtypes = []
        self.lib.GetPublicSettings.argtypes = []
    
    def get_protected_settings(self):
        script, file_urls = self.lib.GetProtectedSettings()
        return {
            "script": script,
            "file_urls": file_urls
        }
    
    def get_public_settings(self):
        secret_string, secret_script, file_urls, storage_acct_name, storage_acct_key = self.lib.GetPublicSettings()
        return {
            "secret_string": secret_string,
            "secret_script": secret_script,
            "file_urls": file_urls,
            "storage_acct_name": storage_acct_name,
            "storage_acct_key": storage_acct_key
        }