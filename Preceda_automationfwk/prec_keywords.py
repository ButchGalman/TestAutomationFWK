import os
import time
from object_repository import ObjectRepository
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from Selenium2Library.keywords import _browsermanagement
from Selenium2Library.keywords._element import _ElementKeywords

class PrecedaKeywords(_ElementKeywords):
    
    def wait_for_manual_step(self,timeout=0.0):
        time.sleep(float(timeout))
    
    def prec_navigate_click_tree_item(self,topmenu,submenu,action):
        menucount = self.get_matching_xpath_count("//div[contains(@class, 'top-nav')]/div/label")
        self._debug("menucount - %s" %(menucount))
        for index in range(1, int(menucount)+1):
            loc = "//div[contains(@class, 'top-nav')]/div/label" + "[" + str(index) + "]"
            menuvalue = self.get_element_attribute(loc + "@innerHTML")
            self._debug("menuvalue - %s" %(menuvalue))
            if menuvalue == topmenu:
                self._debug("Clicking topmenu - %s" %(topmenu))
                self.click_element(loc)
                
                submenucount = self.get_matching_xpath_count("//*[@id='treeview-1026']/table/tbody/tr")
                self._debug("submenucount - %s" %(submenucount))
                for index in range (2, int(submenucount) + 1 ):
                    loc = "//*[@id='treeview-1026']/table/tbody/tr" + "[" + str(index) + "]"
                    submenutitle = self.get_element_attribute(loc + "@textContent")
                    self._debug("submenutitle - %s" %(submenutitle))
                    if submenutitle == submenu:
                        self.click_element(loc)
                        actioncount = self.get_matching_xpath_count("//*[@id='treeview-1026']/table/tbody/tr[contains(@class,'x-grid-tree-node-leaf')]")
                        self._debug("actioncount - %s" %(actioncount))
                        for actionIndex in range(1, int(actioncount) + 1):
                            actionloc = "//*[@id='treeview-1026']/table/tbody/tr[contains(@class,'x-grid-tree-node-leaf')]" + "[" + str(actionIndex) + "]"
                            actionvalue = self.get_element_attribute(actionloc + "@textContent")
                            self._debug("actionvalue - %s" %(actionvalue))
                            if actionvalue == action:
                                self.click_element(actionloc)
                                return True
                        raise RuntimeError("Action Menu - %s not found!" %(action))     
                        return True
                raise RuntimeError("Sub Menu - %s not found!" %(submenu))
                return True
        raise RuntimeError("Top Menu - %s not found!" %(topmenu))