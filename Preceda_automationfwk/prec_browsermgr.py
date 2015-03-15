from Selenium2Library.keywords import _BrowserManagementKeywords
from prec_windowmanager import PrecedaWindowManager

class PrecedaBrowserMgr(_BrowserManagementKeywords, PrecedaWindowManager):
    def preceda_switch_to_New_Window(self):
        self._preceda_select_new_Window(self._current_browser())