#pylint: disable=C0301
'''Herein lies the object repository, it can be used to overwrite default functionality. Use it only if you know
what you are doing. The KEYS must be lower case!
'''
class ObjectRepository(object):

    def __init__(self):
        self.default_OR = {
            # Framework objects
            "login_username" :'css=#AUSERID',
            "login_password" : "//*[@id='AUSRPWD']",
            "login_client" : 'css=#ACLIENT',
            "login_button" : "css=#loginButton",
            "menu_administration" : "//*[@id='M000140']",
            #"login_banner" : "id=logOnBanner",
            #"login_info" : "css=.infoMessage",
            #"mainpage_banner" : "id=logoButton",

        }



