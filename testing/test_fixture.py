'''
@pytest.fixture(autouse=True,scope='function')
autous为True时，自动应用到每个方法里面,默认为False；scope默认就是function级别的，还有class/module/package/session
'''

import pytest


# @pytest.fixture()
# def login():
#     #相当于setup
#     print("登入")
#     yield ['Joshua','123456']
#     #相当于teardown
#     print(("登出"))
#
# @pytest.fixture()
# def conn_db():
#     print("连接数据库")
#     yield
#     print("退出数据库")

def test_case1(login):
    print("test case1")


def test_case2(login, conn_db):
    print("test case2")
    print(login)


@pytest.mark.usefixtures("login")
def test_case3():
    print("test case3")


def test_case4():
    print("test case4")
