import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestTestdemo():
    def setup_method(self, method):
        # 复用浏览器：先手动登录，再复用浏览器继续后续操作
        # options = Options()
        # options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        # self.driver.quit()
        pass

    def test_cookie(self):
        # 先扫描登录，复用浏览器，get_cookies()
        # print(self.driver.get_cookies())
        cookie = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853135000230'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'S7yve8jCfy4LsogRKQdScc0T_YZoPjLqSlbZ2IUStPqI1YjM8Or3_OBnQzgl5bYvu2RTOoYgKBRsecMmswUYzKDlmRHpBUY7rANPytFAYpotu9NfYacw3-rzmLtU68Pq1HTvTdw-o_DuI8BDL4jbW2S_dqd3CBRYgP5nf78QHfWTv-EG4pntaEPbQehmrF-ft6RrbWwnJplk_-pS0ARO83WUzyqVfk3NOKef7FBA5iMkdHV_dkgwQP0PFtrNqoIC77YnljhLbwwwXjn6_MxJTA'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853135000230'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325070174894'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'x3--W-5M6iUFlhqBt68f6QQNwfKTU_SS_HWrd7_cpmYe88S4NfcX6iprCcstuEi4'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a7832369'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '19658774311041223'},
            {'domain': '.qq.com', 'expiry': 1666451872, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.939041501.1603372664'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1634905932, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'VHTozc39eb'},
            {'domain': '.qq.com', 'expiry': 1603466272, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.902134772.1603372664'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603401468, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '3abjoij'},
            {'domain': '.qq.com', 'expiry': 1880370473, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': '6023454011021e17'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '5383359488'},
            {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '25a154851d4c167bf6e91991f4edc4e55153caa5ed5a8b5e006ee5020538a6a0'},
            {'domain': '.qq.com', 'expiry': 1868153052, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_4402113077a0b'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '3547046976'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1634908663, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603372664'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1605971874, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # sleep(2)
        for i in cookie:
            self.driver.add_cookie(i)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.refresh()
        # sleep(2)

    def test_shelve(self):
        '''
        shelve是python的自带的模块， shelve类似于一个存储持久化对象的持久化字典，即字典文件
        :return:
        '''

        # cookie = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688853135000230'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'S7yve8jCfy4LsogRKQdScc0T_YZoPjLqSlbZ2IUStPqI1YjM8Or3_OBnQzgl5bYvu2RTOoYgKBRsecMmswUYzKDlmRHpBUY7rANPytFAYpotu9NfYacw3-rzmLtU68Pq1HTvTdw-o_DuI8BDL4jbW2S_dqd3CBRYgP5nf78QHfWTv-EG4pntaEPbQehmrF-ft6RrbWwnJplk_-pS0ARO83WUzyqVfk3NOKef7FBA5iMkdHV_dkgwQP0PFtrNqoIC77YnljhLbwwwXjn6_MxJTA'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688853135000230'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970325070174894'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'x3--W-5M6iUFlhqBt68f6QQNwfKTU_SS_HWrd7_cpmYe88S4NfcX6iprCcstuEi4'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a7832369'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '19658774311041223'},
        #     {'domain': '.qq.com', 'expiry': 1666451872, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.939041501.1603372664'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1634905932, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
        #      'value': 'VHTozc39eb'},
        #     {'domain': '.qq.com', 'expiry': 1603466272, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.902134772.1603372664'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1603401468, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '3abjoij'},
        #     {'domain': '.qq.com', 'expiry': 1880370473, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
        #      'secure': False, 'value': '6023454011021e17'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
        #      'secure': False, 'value': '5383359488'},
        #     {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
        #      'value': '25a154851d4c167bf6e91991f4edc4e55153caa5ed5a8b5e006ee5020538a6a0'},
        #     {'domain': '.qq.com', 'expiry': 1868153052, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
        #      'secure': False, 'value': '0_4402113077a0b'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': False, 'value': '3547046976'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1634908663, 'httpOnly': False,
        #      'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603372664'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1605971874, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'}]

        # 添加数据到shelve文件
        # db = shelve.open('cookie_data')
        # db['cookie_data'] = cookie
        # db.close()

        # with shelve.open('cookie_data') as db:
        #     db['cookie'] = cookie

        # 登录
        with shelve.open('cookie_data') as db:
            cookie = db['cookie_data']
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            for i in cookie:
                self.driver.add_cookie(i)
            self.driver.refresh()

        # 导入通讯录
        self.driver.find_element_by_css_selector('[class="ww_indexImg ww_indexImg_Import"]').click()
        sleep(2)
        # 文件路径有个坑，记得要用\\
        self.driver.find_element_by_css_selector('.ww_fileImporter_fileContainer_uploadInputMask').send_keys(
            'C:\\Users\\Joshua\\PycharmProjects\\hogwarts\\web\\uploadfile.xlsx')
        sleep(2)
        filename = self.driver.find_element_by_css_selector('.ww_fileImporter_fileContainer_fileNames').text
        assert filename == 'uploadfile.xlsx'
        sleep(4)
