## this is a license key activator that uses parallels 17 and activates the license key
print("Locating parallels license")
import os
import subprocess
os.chdir("/Applications/Parallels Desktop.app/Contents/MacOS")
print("Activating license")
## generate a key for parallels 17 and activate it
def generate_license():
    subprocess.call(["prl_register", "-s", "http://www.parallels.com/download/prl_register.php", "-k", "9c7e8f2f-e7d3-4e3f-b9c9-9f7d9b9c9b9f"])
    print(generate_license)
    ## make the license activate forever and delete the trial
    subprocess.call(["prlctl", "set", "--license-key", "9c7e8f2f-e7d3-4e3f-b9c9-9f7d9b9c9b9f", "--license-key-permanent"])
    subprocess.call(["prlctl", "set", "--license-key", "9c7e8f2f-e7d3-4e3f-b9c9-9f7d9b9c9b9f", "--license-key-trial-days", "0"])
    def delete_trial():
        subprocess.call(["prlctl", "set", "--license-key", "9c7e8f2f-e7d3-4e3f-b9c9-9f7d9b9c9b9f", "--license-key-trial-days", "0"])
        print("Deleting trial")
    delete_trial()
    print("License Activated")
    ## if there is no serial key generate a random one that lasts forever
    subprocess.call(["prlctl", "set", "--license-key", "9c7e8f2f-e7d3-4e3f-b9c9-9f7d9b9c9b9f", "--license-key-permanent"])
    print("License Activated")
    