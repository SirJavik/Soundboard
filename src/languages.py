import xml.etree.ElementTree as ET

import soundboardconstants


class Languages:
    # __loggingPrefix = "Languages    :"
    __languageTree = ""
    __languageRoot = ""

    def setlanguagetree(self, file):
        try:
            self.__languageTree = ET.parse(file)
        except FileNotFoundError:
            if soundboardconstants.LOGGING:
                self.__languageTree = None
                print("Failed")
        # if soundboardconstants.LOGGING:
        #    logging.info(f"{self.__loggingPrefix} Loading {file} file...")

    def getlanguagetree(self):
        return self.__languageTree

    def setlanguageroot(self, tree):
        try:
            self.__languageRoot = tree.getroot()
        except AttributeError:
            self.__languageRoot = None

        # if soundboardconstants.LOGGING:
        #    logging.info(f"{self.__loggingPrefix} Setting {self.getlanguageroot()} as root...")

    def getlanguageroot(self):
        return self.__languageRoot

    def load(self, languagefile):
        self.setlanguagetree(languagefile)
        self.setlanguageroot(self.getlanguagetree())

        # if soundboardconstants.LOGGING:
        #    languageName = self.getlanguageroot().find("languageName").text
        #    logging.info(f"{self.__loggingPrefix} Loading {languageName}...")

    def getlanguagestr(self, id, default=None):
        if self.__languageTree is not None:
            return self.getlanguageroot().find(f'.//languageStr[@id="{id}"]').text
        else:
            return default
