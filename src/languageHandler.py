import xml.etree.ElementTree as ET
import soundboardconstants
import logging

class Languages:
    #__loggingPrefix = "Languages    :"
    __languageTree = ""
    __languageRoot = ""

    def setlanguagetree(self, file):
        self.__languageTree = ET.parse(file)
        #if soundboardconstants.LOGGING:
        #    logging.info(f"{self.__loggingPrefix} Loading {file} file...")

    def getlanguagetree(self):
        return self.__languageTree

    def setlanguageroot(self, tree):
        self.__languageRoot = tree.getroot()
        #if soundboardconstants.LOGGING:
        #    logging.info(f"{self.__loggingPrefix} Setting {self.getlanguageroot()} as root...")

    def getlanguageroot(self):
        return self.__languageRoot

    def load(self, languagefile):
        self.setlanguagetree(languagefile)
        self.setlanguageroot(self.getlanguagetree())

        #if soundboardconstants.LOGGING:
        #    languageName = self.getlanguageroot().find("languageName").text
        #    logging.info(f"{self.__loggingPrefix} Loading {languageName}...")

    def getlanguagestr(self, id):
        return self.getlanguageroot().find(f'.//languageStr[@id="{id}"]').text
