import os
import time
from object_repository import ObjectRepository
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver
from Selenium2Library import Selenium2Library
from prec_windowmanager import PrecedaWindowManager
from prec_browsermgr import PrecedaBrowserMgr


class PrecedaLibrary(Selenium2Library, PrecedaBrowserMgr):
    '''This is the main class for a library for RobotFramework that uses Selenium 2.0 WebDriver
    in the back-end.  It exposes the PrecedaLibrary to robot framework
    '''

    def __init__(self, timeout=0.0, run_on_failure='Capture Page Screenshot'):
        '''for the init function timeout will be used to set both javascript timeout and
        the implicit_wait functunality.
        run_on_failure is the robot framework keyword that is run when a keyword fails, by default it is
        set to capturing a page screenshot'''
        super( PrecedaLibrary, self).__init__()
        #setup an OR
        self.OR = ObjectRepository().default_OR
        Selenium2Library.__init__(self,timeout=timeout, implicit_wait=timeout,
                    run_on_failure=run_on_failure)

    def _element_find(self, locator, first_only, required, tag=None):
        ''' Override _element_find of Selenium2Library to insert handle for Object 
        Repository'''
        browser = self._current_browser()
        # Check if locator uses OR format
        # if OR is located in objectRepo then use that value else use
        # input locator value
        ORlocator = self.get_locator_from_OR(locator)
        elements = self._element_finder.find(browser, ORlocator, tag)
        if required and len(elements) == 0:
            raise ValueError("Element locator '" + ORlocator + "' did not match any elements.")
        if first_only:
            if len(elements) == 0: return None
            return elements[0]
        return elements
  
    def get_locator_from_OR(self,OR_name):
        '''gets a locator stored in the OR'''
        if OR_name and OR_name.lower().startswith("or:"):
            name = OR_name[3:].lower()
        elif OR_name:
            return OR_name
        return self.OR[name]
    
    def wait_for_manual_step(self,timeout=0.0):
        time.sleep(timeout)
              
    def preceda_Logon(self, browser, url, user_name, pwd, client):
        '''perfoms Login functionality, by opening browser, navigating to URL, and trying to login
        it should catch the new window launched by Preceda
        '''
        self.open_browser(url, browser)
        self.maximize_browser_window()
        #self.wait_until_page_contains_element(self.OR["login_username"])
        self.input_text("OR:login_username", user_name)
        self.input_text("OR:login_password", pwd)
        self.input_text("OR:login_client", client)
        self.click_element("OR:login_button")
        # wait until new window is launched not necessarily loaded
        self.wait_for_manual_step(10)
        #Switch Browsers
        self.preceda_switch_to_New_Window()
        self.wait_until_page_contains("Administration",300) 
        #self.click_element("OR:menu_administration")
        self.capture_page_screenshot