import os
import time

import requests
from allure_commons._allure import step
from dotenv import load_dotenv
from selene import have
from selene.support.shared import browser

from utils.base_session import BaseSession

load_dotenv()

LOGIN = os.getenv("DEMOSHOP_LOGIN")
PASSWORD = os.getenv("DEMOSHOP_PASSWORD")
API_URL = os.getenv("DEMOSHOP_API_URL")
WEB_URL = os.getenv("DEMOSHOP_WEB_URL")

browser.config.base_url = WEB_URL


def test_add_product_to_cart(demoshop):
    response = demoshop.post(
        "/login",
        json={"Email": "qa_guru_3_14@gu.ru", "Password": "123456"},
        allow_redirects=False,
    )
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    browser.open("/Themes/DefaultClean/Content/images/logo.png")

    browser.driver.add_cookie(
        {"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie}
    )
    browser.open("")

    # browser.open("/register")
    # browser.element("#FirstName").type('Ivan')
    # browser.element("#LastName").type('Ivanov')
    # browser.element('#Email').type('testivanivanovtest@test.ru')
    # browser.element('#Password').type('123456')
    # browser.element('#ConfirmPassword').type('123456')
    # browser.element('#register-button').click()

    # browser.open("/build-your-cheap-own-computer")
    requests.post(
        "https://demowebshop.tricentis.com/addproducttocart/details/72/1",
        json={
            "product_attribute_72_5_18": 53,
            "product_attribute_72_6_19": 54,
            "product_attribute_72_3_20": 57,
            "addtocart_72.EnteredQuantity": 1,
        }
    )
    browser.element(".header-links #topcartlink").click()
    browser.element('.update-cart-button').click()
    browser.element("[name=itemquantity3081838]").should(have.size(2))



    # browser.open("/build-your-cheap-own-computer")
    # browser.element(".header-links #topcartlink").click()
    # browser.element('.update-cart-button').click()
    # browser.element("[name=itemquantity3081621]").should(have.size(13))
    # add_product_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    #
    # browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': add_product_cookie})
    # browser.open('')


# def test_login_though_api_with_base_session_fixture(demoshop):
#     response = demoshop.post(
#         "/login",
#         json={"Email": "qa_guru_3_14@gu.ru", "Password": "123456"},
#         allow_redirects=False,
#     )
#     authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
#
#     browser.open("/Themes/DefaultClean/Content/images/logo.png")
#
#     browser.driver.add_cookie(
#         {"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie}
#     )
#     browser.open("")
#
#     with step("Verify successful authorization"):
#         browser.element(".account").should(have.text(LOGIN))
