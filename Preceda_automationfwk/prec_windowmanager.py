from Selenium2Library.locators import WindowManager

class PrecedaWindowManager(WindowManager):
    def _preceda_select_new_Window(self, browser):
        starting_handle = browser.get_current_window_handle()
        for handle in browser.get_window_handles():
            if not (starting_handle == handle):
                browser.switch_to_window(handle)
