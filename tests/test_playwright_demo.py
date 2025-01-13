import pytest
import allure
from playwright.sync_api import Page, expect


def capture_screenshot(page: Page, step_name: str) -> None:
    """
    Captures a screenshot and attaches it to the Allure report.
    """
    screenshot_path = f"screenshots/{step_name}.png"
    page.screenshot(path=screenshot_path)
    allure.attach.file(
        screenshot_path,
        name=f"{step_name} - Failure Screenshot",
        attachment_type=allure.attachment_type.PNG
    )


def test_example2(page: Page) -> None:
    allure.dynamic.title("Test Authentication Failure")
    allure.dynamic.description(
        "This test attempts to log into the website using a wrong login and password. Fails if any error happens.\n\n"
        "Note that this test does not test Azure-AD Authentication."
    )
    allure.dynamic.tag("Essentials", "Authentication")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "Krishna_Raj")
    allure.dynamic.link("https://dev.bankbuddy.me/console/login", name="Website")
    allure.dynamic.issue("AUTH-123")
    allure.dynamic.testcase("TMS-456")

    allure.dynamic.parent_suite("Tests for web interface")
    allure.dynamic.suite("Tests for essential features")
    allure.dynamic.sub_suite("Tests for authentication")

    try:
        with allure.step("Navigate to login Page"):
            page.goto("https://beta1.studio.bankbuddy.me/console/login")
    except Exception as e:
        capture_screenshot(page, "Navigate to login Page")
        raise e

    try:
        with allure.step("Enter Username"):
            page.get_by_label("Username").click()
            page.get_by_label("Username").fill("...")
            page.get_by_label("Username").press("Tab")
    except Exception as e:
        capture_screenshot(page, "Enter Username")
        raise e

    try:
        with allure.step("Enter Password"):
            page.get_by_label("Password").fill("...")
    except Exception as e:
        capture_screenshot(page, "Enter Password")
        raise e

    try:
        with allure.step("Click the Submit button"):
            page.get_by_role("button", name="SUBMIT").click()
            page.get_by_role("button", name="arrow_right_alt default").click()
            page.get_by_role("button", name="N arrow_drop_down").click()
            page.locator("#main-menu-dropdown > .MuiBackdrop-root").click()
    except Exception as e:
        capture_screenshot(page, "Click the Submit button")
        raise e

    try:
        with allure.step("Verify elements on the page"):
            expect(page.get_by_role("heading", name="Welcome shubham_beta1!")).to_be_visible()
            expect(page.get_by_placeholder("Search Projects")).to_be_visible()
            expect(page.get_by_role("button", name="arrow_right_alt walletusdpng")).to_be_visible()
    except Exception as e:
        capture_screenshot(page, "Verify elements on the page")
        raise e

    try:
        with allure.step("LogOut"):
            page.get_by_role("button", name="N arrow_drop_down").click()
            page.get_by_text("Logout").click()
            page.get_by_role("button", name="Yes, I'm sure").click()
    except Exception as e:
        capture_screenshot(page, "LogOut Test")
        raise e
