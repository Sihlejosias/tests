###
# This small program checks if the use have Android SDK or Fastboot installed in the sytem then refer 
# The programe to check the Operattiong stsyem in use. 
####

import subprocess, platform

def sdk_checker(sdk_check):
    adb_fastboot = input("adb or fastboot: ")
    if adb_fastboot == "adb" or adb_fastboot == "fastboot":
        command = "where" if platform.system() == "Windows" else 'which'
        sdk_check = subprocess.run((command, adb_fastboot), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, universal_newlines=None)
        if sdk_check == sdk_check:
            # print(sdk_check.stdout.decode('utf-8'), end="")
            return sdk_check.stdout
        else: 
            return sdk_check.stderr
            # pass
    else: 
        return "ERROR: Please type adb or fastboot to check if  available in system."

sdk_check = sdk_checker

print(sdk_checker(sdk_check))

