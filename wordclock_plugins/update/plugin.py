import os
import time


class plugin:
    """
    A class to update the RPI software
    """

    def __init__(self, config):
        """
        Initializations for the startup of the current wordclock plugin
        """
        # Get plugin name (according to the folder, it is contained in)
        self.name = os.path.dirname(__file__).split('/')[-1]
        self.pretty_name = "Software aktualisieren"
        self.description = "Update the wordclock software"
        self.wordclock_path = os.path.dirname(os.path.realpath(__file__))

    def run(self, wcd, wci):
        """
        Git pull to update to the latest version
        """
        wcd.showText("Updating...       ")
        wcd.showIcon(plugin=self.name, iconName='logo')
        print(self.wordclock_path)
        os.system("cd " + self.wordclock_path + "&& cd ../../ && git pull")
        time.sleep(30)
        os.system("shutdown now -r")
        time.sleep(10)
        return
