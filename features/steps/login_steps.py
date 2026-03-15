import time
from asyncio import wait

from behave import given, when, then
import allure
from selenium import webdriver

from pages.login_page import LoginPage

@given(u'user navigates to login page')
@allure.step("Open login page")
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when(u'User enters username "{username}"')
@allure.step("Enter login username")
def step_impl(context, username):
     context.login_page.enter_username(username)

@when(u'user enters password "{password}"')
@allure.step("Enter login password")
def step_impl(context, password):
    context.login_page.enter_password(password)

@when("user clicks login button")
@allure.step("CLick login page")
def step_impl(context):
    context.login_page.click_login()

@then("user should see the dashboard")
@allure.step("verify dashboard")
def step_impl(context):
    assert context.login_page.is_dashboard_visible()

