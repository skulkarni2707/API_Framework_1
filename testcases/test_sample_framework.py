import requests
import pytest
import json
from pageobjects.delete_resource import Del_res
from pageobjects.get_resource import Get_res
from pageobjects.post_resource import Post_res
from pageobjects.put_resource import Put_res
from utilities.customLogger import LogGen


with open('/home/shraddha/PycharmProjects/API_Framework_1/configuration/config.json', "r") as f1:
    data = json.load(f1)

GET_URL = data["geturl"]
POST_URL = data["posturl"]
PUT_URL = data["puturl"]
DELETE_URL = data["deleteurl"]

logger = LogGen.loggen()


def test_get_001():
    logger.info("*********_test_get_001********")
    g=Get_res(GET_URL)
    response=g.get_res()
    assert response.status_code == 200
    logger.info("*********_test_get_001 is Passed********")



def test_get_002():
    g=Get_res(GET_URL)
    response=g.get_res()
    #assert response.status_code == 201
    print(response.reason)
    assert response.reason == "OK"
    logger.info("*********_test_get_002 is passed********")


def test_post_003():
    g=Post_res(POST_URL)
    response=g.post_res()
    print(response.status_code)
    assert response.status_code == 201
    logger.info("*********_test_get_003 is Passed********")


def test_post_004():
    po = Post_res(POST_URL)
    response = po.post_res()
    print(response.headers.get('Content-Length'))
    assert response.headers.get('Content-Length') == "72"
    logger.info("*********_test_get_005 is Passed********")


def test_put_005():
    g=Put_res(PUT_URL)
    response=g.put_res()
    print(response.status_code)
    assert response.status_code == 200
    logger.info("*********_test_get_006 is Passed********")

def test_put_006():
    g=Put_res(PUT_URL)
    response=g.put_res()
    #print(response.status_code)
    #assert response.status_code == 201
    print(response.content)
    print(response.is_redirect)
    assert response.is_redirect == False
    logger.info("*********_test_get_007 is passed********")



def test_delete_007():
    g=Del_res(DELETE_URL)
    response=g.del_res()
    assert response.status_code == 200
    logger.info("*********_test_get_008 is Passed********")

def test_delete_008():
    g=Del_res(DELETE_URL)
    response=g.del_res()
    #assert response.status_code == 201
    print(response.ok)
    assert response.ok == True
    logger.info("*********_test_get_009 is passed********")















