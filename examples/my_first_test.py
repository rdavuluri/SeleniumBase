from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_basic(self):
        self.open('http://xkcd.com/353/')            # Navigate to the web page
        self.assert_element('img[alt="Python"]')       # Assert element on page
        self.click('a[rel="license"]')                  # Click element on page
        text = self.get_text("div center")        # Grab text from page element
        self.assertTrue("reuse any of my drawings" in text)
        self.open('http://xkcd.com/1481/')
        title = self.get_attribute('#comic img', 'title')   # Grab an attribute
        self.assertTrue('connections to the server' in title)
        self.click_link_text('Blag')              # Click on link with the text
        self.assert_text('The blag of the webcomic', 'h2')  # Assert text in h2
        self.update_text('input#s', 'Robots!\n')  # Fill in field with the text
        self.assert_text('Hooray robots!', '#content')
        self.open('http://xkcd.com/1319/')
        self.assert_text('Automation', 'div#ctitle')

        ####

        #######################################################################
        #
        #    ****  NOTES / USEFUL INFO  ****
        #
        # 1. By default, CSS Selectors are used to identify elements.
        #    You can use other identification options like PARTIAL_LINK_TEXT:
        #    [
        #        from selenium.webdriver.common.by import By
        #        ...
        #        self.click('Next', by=By.PARTIAL_LINK_TEXT)
        #    ]
        #    For the full list of `By` options, type ``dir(By)`` into a python
        #    command prompt after importing it (or in ipdb debugger mode). Ex:
        #    {
        #        >>> dir(By)
        #        ['CLASS_NAME', 'CSS_SELECTOR', 'ID', 'LINK_TEXT', 'NAME', ...
        #    }
        #    XPath is used by default if the arg starts with "/", "./", or "(":
        #    [
        #        self.click('/html/body/div[3]/div[4]/p[2]/a')
        #    ]
        #    But if you want XPath-clicking to be more clear in the code, use:
        #    [
        #        self.click_xpath('/html/body/div[3]/div[4]/p[2]/a')
        #    ]
        #
        #    If you're completely new to CSS selectors, right-click on a
        #    web page and select "Inspect Element" to see the CSS in the html.
        #
        # 2. Most methods have the optional `timeout` argument. Ex:
        #    [
        #        self.get_text('center', timeout=15)
        #    ]
        #    The `timeout` argument tells the method how many seconds to wait
        #    for an element to appear before raising an exception. This is
        #    useful if a web page needs additional time to load an element.
        #    If you don't specify a `timeout`, a default timeout is used.
        #    Default timeouts are configured in seleniumbase/config/settings.py
        #
        # 3. There's usually more than one way to do the same thing. Ex:
        #    [
        #        header_text = self.get_text('header h2')
        #        self.assertTrue('The blag of the webcomic' in header_text)
        #    ]
        #    Can be simplified to:
        #    [
        #        self.assert_text('The blag of the webcomic', 'header_text')
        #    ]
        #
        #    The following line:
        #    [
        #        title = self.get_attribute('#comic img', 'title')
        #    ]
        #    Can also be written as:
        #    [
        #        element = self.find_element('#comic img')
        #        title = element.get_attribute('title')
        #    ]
        #
        #    And the following line:
        #    [
        #        text = self.get_text("div center")
        #    ]
        #    Can also be written as:
        #    [
        #        text = self.find_element('div center').text
        #    ]
        #    ...and in many more ways!
        #
        #    For backwards-compatibilty, some methods have multiple names.
        #    Ex: wait_for_element_visible() is the same as find_element().
        #    Both search for and return the element, and raise an exception if
        #    the element does not appear on the page within the timeout limit.
        #    (See seleniumbase/fixtures/base_case.py for the full method list.)
