<img src="https://cdn2.hubspot.net/hubfs/100006/images/expanded_icons2f.png" title="SeleniumBase" align="left" padding="1px" height="100" margin="1px 1px" hspace="2px">

Browser automated testing with Python done efficiently.<br />

[![](https://img.shields.io/pypi/v/seleniumbase.svg)](https://pypi.python.org/pypi/seleniumbase) [![Build Status](https://travis-ci.org/seleniumbase/SeleniumBase.svg?branch=master)](https://travis-ci.org/seleniumbase/SeleniumBase)<br /><br>

<img src="https://cdn2.hubspot.net/hubfs/100006/images/new_logo_pre6c.png" title="SeleniumBase" height="40">

**A framework for all your UI testing:**<br />
SeleniumBase is a complete end-to-end testing solution for web apps. It extends Python's unittest framework by including the WebDriver APIs and adding functionality to make automation more efficient & reliable. It simplifies the process of setting up continuous integration and writing automated tests.

**No more repetitive WebDriver coding:**<br />
SeleniumBase automatically takes care of common WebDriver actions such as spinning up & closing web browsers, creating screenshots & logs for test failures, waiting for page objects to fully appear before acting on them, connecting to a Selenium Grid, using a proxy server, writing to a database, etc. (<i>[Read more](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/command_line.md)</i>)

**Simple Python syntax makes coding easy:**<br />
(<i>By default, [CSS Selectors](https://www.w3schools.com/cssref/css_selectors.asp) are used for finding page elements.</i>)

<img src="https://cdn2.hubspot.net/hubfs/100006/images/my_first_test_py_2.png" title="SeleniumBase Python Code" height="280">

**Run tests with Pytest or Nose in any browser:**

```bash
pytest my_first_test.py --browser=chrome

nosetests my_test_suite.py --browser=firefox
```

**Watch [my_first_test.py](https://github.com/seleniumbase/SeleniumBase/blob/master/examples/my_first_test.py) run in [Demo Mode](#seleniumbase_demo_mode):**<br>
![](https://cdn2.hubspot.net/hubfs/100006/images/sb_demo.gif "SeleniumBase")<br>
(<i>If you remove all the asserts from that test, you're left with [basic_script.py](https://github.com/seleniumbase/SeleniumBase/blob/master/examples/basic_script.py), which performs all the actions you can see when running the test.</i>)

**No more messy code:**<br />
This long line of standard WebDriver code,
```python
self.driver.find_element_by_css_selector("textarea").send_keys("text")
```
...becomes the following in SeleniumBase:
```python
self.update_text("textarea", "text")
```
(<i>You can still use ``self.driver`` in your code.</i>)

**No more flaky tests:**<br />
SeleniumBase methods automatically wait for page elements to finish loading before interacting with them (*up to a timeout limit*). This means you no longer need random ``time.sleep()`` statements in your code.

**Assist manual QA with automation:**<br />
SeleniumBase includes an automated/manual hybrid solution called **[MasterQA](https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/masterqa/ReadMe.md)**, which speeds up manual testing by having automation perform all the web browser actions while the manual tester only validates what is seen.

**Integrate with your favorite tools:**<br />
SeleniumBase is compatible with [Selenium Grid](https://github.com/seleniumbase/SeleniumBase/tree/master/integrations/selenium_grid), [MySQL](https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/core/testcase_manager.py), [Docker](https://github.com/seleniumbase/SeleniumBase/blob/master/integrations/docker/ReadMe.md), [NodeJS](https://github.com/seleniumbase/SeleniumBase/tree/master/integrations/node_js), [Google Cloud](https://github.com/seleniumbase/SeleniumBase/tree/master/integrations/google_cloud/ReadMe.md), and [AWS](#amazon_section).

**Comes with a business mindset:**<br />
SeleniumBase makes it easy to automate tedious business tasks. (*To learn about businesses using SeleniumBase, [Click Here](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/happy_customers.md).*)

**Extensively tested and made with love:**<br />
SeleniumBase was originally built for [testing HubSpot's platform](https://product.hubspot.com/blog/the-classic-qa-team-is-obsolete) and automating business processes. In 2014, SeleniumBase was open-sourced and spun off as its own independent entity to benefit users everywhere.

**Contains lots of additional features:**<br />
([Read more about SeleniumBase features here](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/features_list.md))

<br><img src="https://cdn2.hubspot.net/hubfs/100006/images/new_logo_pre6c.png" title="SeleniumBase" height="40">

## Get Started:

(Before installation, you'll need to **[install Python](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/install_python_pip_git.md)** and **[download Webdriver](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/webdriver_installation.md)**.)


### ![http://seleniumbase.com](https://cdn2.hubspot.net/hubfs/100006/images/super_logo_tiny.png "SeleniumBase") **Step 1:** Clone SeleniumBase

```bash
git clone https://github.com/seleniumbase/SeleniumBase.git

cd SeleniumBase
```

(<i>A [Git](https://git-scm.com/) GUI tool like [SourceTree](http://www.sourcetreeapp.com/) may help.</i>)


### ![http://seleniumbase.com](https://cdn2.hubspot.net/hubfs/100006/images/super_logo_tiny.png "SeleniumBase") **Step 2:** Create a Virtual Env.

(OPTIONAL) To learn how to create a Python virtual environment, [see the ReadMe](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/virtualenv_instructions.md).<br><br><i>[python-guide.org/en/latest/dev/virtualenvs](http://docs.python-guide.org/en/latest/dev/virtualenvs/) has more details.</i>

If you choose not to use a Python virtual environment, add the ``--user`` flag at the end of your pip and python install commands in *Step 3*. (This can help you evade issues with requiring root access on the machine you're using.)


### ![http://seleniumbase.com](https://cdn2.hubspot.net/hubfs/100006/images/super_logo_tiny.png "SeleniumBase") **Step 3:** Install SeleniumBase

Run the following command from the top-level SeleniumBase folder:
```bash
pip install -e .
```
If you already have an older version installed, you may need to add ``--upgrade`` to the command in order to update previously-installed Python packages. If you're not using a virtual environment, you may need to add ``--user`` to the end of your command. (<i>Only needed if you see errors during installation.</i>)

If you want to install the requirements seperately, use:
```
pip install -r requirements.txt

python setup.py develop
```

(<i>If you can't install ChromeDriver or GeckoDriver, you can use `server_requirements.txt` and `server_setup.py` to run tests using the older Selenium 2.53.6 on a version of Firefox that's older than 47.</i>)

To install SeleniumBase from the [Python Package Index](https://pypi.python.org/pypi/seleniumbase) use the following command. (You may need to add ``--upgrade`` if you have an older version already installed.):
```bash
pip install seleniumbase
```

(NOTE: If you're using Python 3.x instead of Python 2.7, use ``pip3`` in place of ``pip`` and ``python3`` in place of ``python`` in the above commands.)


<a id="seleniumbase_basic_usage"></a>
### ![http://seleniumbase.com](https://cdn2.hubspot.net/hubfs/100006/images/super_logo_tiny.png "SeleniumBase") **Step 4:** Run the Example Script

**Here's what the example script looks like:**

```python
from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_basic(self):
        self.open('http://xkcd.com/353/')
        self.assert_element('img[alt="Python"]')
        self.click('a[rel="license"]')
        text = self.get_text("div center")
        self.assertTrue("reuse any of my drawings" in text)
        self.open('http://xkcd.com/1481/')
        title = self.get_attribute('#comic img', 'title')
        self.assertTrue('connections to the server' in title)
        self.click_link_text('Blag')
        self.assert_text('The blag of the webcomic', 'h2')
        self.update_text('input#s', 'Robots!\n')
        self.assert_text('Hooray robots!', '#content')
        self.open('http://xkcd.com/1319/')
        self.assert_text('Automation', 'div#ctitle')
```
(<i>By default, [CSS Selectors](https://www.w3schools.com/cssref/css_selectors.asp) are used for finding page elements.</i>)

**Here's how to run the example script on various web browsers:**

(NOTE: You can interchange **nosetests** with **pytest** at anytime.)

```bash
cd examples/

pytest my_first_test.py --browser=chrome

nosetests my_first_test.py --browser=firefox
```
(<i>If no browser is specified, Chrome is used by default.</i>)

<a id="seleniumbase_demo_mode"></a>
If the example test is moving too fast for your eyes to see what's going on, you can run it in **Demo Mode** by adding ``--demo_mode`` on the command line, which pauses the browser briefly between actions, and highlights page elements being acted on:

```bash
pytest my_first_test.py --browser=chrome --demo_mode
```

You can override the default wait time by either updating [settings.py](https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/config/settings.py) or by using ``--demo_sleep={NUM}`` when using Demo Mode. (NOTE: If you use ``--demo_sleep={NUM}`` without using ``--demo_mode``, nothing will happen.)

```bash
nosetests my_first_test.py --browser=chrome --demo_mode --demo_sleep=1.2
```

You can also use the following in your scripts to slow down the tests:

```python
import time; time.sleep(5)  # sleep for 5 seconds (add this after the line you want to pause on)
import ipdb; ipdb.set_trace()  # waits for your command. n = next line of current method, c = continue, s = step / next executed line (will jump)
```

(NOTE: If you're using pytest instead of nosetests and you want to use ipdb in your script for debugging purposes, you'll either need to add ``--capture=no`` on the command line, or use ``import pytest; pytest.set_trace()`` instead of using ipdb. More info on that [here](http://stackoverflow.com/questions/2678792/can-i-debug-with-python-debugger-when-using-py-test-somehow).)

You may also want to have your test sleep in other situations where you need to have your test wait for something. If you know what you're waiting for, you should be specific by using a command that waits for something specific to happen.

If you need to debug things on the fly (in case of errors), use this:

```bash
nosetests my_first_test.py --browser=chrome --pdb --pdb-failures -s
```

The above code (with --pdb) will leave your browser window open in case there's a failure, which is possible if the web pages from the example change the data that's displayed on the page. (ipdb commands: 'c', 's', 'n' => continue, step, next). You may need the ``-s`` in order to see all console output.

Here are some other useful nosetest arguments for appending to your run commands:

```bash
--logging-level=INFO  # Hide DEBUG messages, which can be overwhelming.
-x  # Stop running the tests after the first failure is reached.
-v  # Prints the full test name rather than a dot for each test.
--with-id  # If -v is also used, will number the tests for easy counting.
```

During test failures you'll get detailed log files, which include screenshots, page source, and basic test info, which will get added to the logs folder at ``latest_logs/``. (Unless you have ARCHIVE_EXISTING_LOGS set to True in [settings.py](https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/config/settings.py), log files with be cleaned up at the start of the next test run. If the archive feature is enabled, those logs will get saved to the ``archived_logs/`` folder.) The ``my_test_suite.py`` collection contains tests that fail on purpose so that you can see how logging works.

```bash
cd examples/

pytest my_test_suite.py --browser=chrome

pytest my_test_suite.py --browser=firefox
```

If you want to run tests headlessly, use ``--headless``, which you'll need to do if your system lacks a GUI interface. Even if your system does have a GUI interface, it may still support headless browser automation.

For running tests outside of the SeleniumBase repo with **Pytest**, you'll want a copy of **[pytest.ini](https://github.com/seleniumbase/SeleniumBase/blob/master/pytest.ini)** on the root folder. (Subfolders should include a blank ``__init__.py`` file.)

For running tests outside of the SeleniumBase repo with **Nosetests**, you'll want a copy of **[setup.cfg](https://github.com/seleniumbase/SeleniumBase/blob/master/setup.cfg)** on the root folder. (Subfolders should include a blank ``__init__.py`` file.)

If you want to pass additional data from the command line to your tests, you can use ``--data=STRING``. Now inside your tests, you can use ``self.data`` to access that.

To run Pytest multithreaded on multiple CPUs at the same time, add ``-n NUM`` on the command line, where NUM is the number of CPUs you want to use.

<img src="https://cdn2.hubspot.net/hubfs/100006/images/logo_base_4b.png" title="SeleniumBase" height="120">

<a id="creating_visual_reports"></a>
### ![http://seleniumbase.com](https://cdn2.hubspot.net/hubfs/100006/images/super_logo_tiny.png "SeleniumBase") **Creating Visual Test Suite Reports:**

(NOTE: The command line args are different for Pytest vs Nosetests)

#### **Pytest Reports:**

Using ``--html=report.html`` gives you a fancy report of the name specified after your test suite completes.

```bash
pytest my_test_suite.py --html=report.html
```

You can also use ``--junitxml=report.xml`` to get an xml report instead. Jenkins can use this file to display better reporting for your tests.

```bash
pytest my_test_suite.py --junitxml=report.xml
```

![](https://cdn2.hubspot.net/hubfs/100006/images/PytestReport.png "Example Pytest Report")

#### **Nosetest Reports:**

The ``--report`` option gives you a fancy report after your test suite completes.

```bash
nosetests my_test_suite.py --report
```
<img src="https://cdn2.hubspot.net/hubfs/100006/images/Test_Report_2.png" title="Example Nosetest Report" height="420">

(NOTE: You can add ``--show_report`` to immediately display Nosetest reports after the test suite completes. Only use ``--show_report`` when running tests locally because it pauses the test run.)


### ![http://seleniumbase.com](https://cdn2.hubspot.net/hubfs/100006/images/super_logo_tiny.png "SeleniumBase") **Using a Proxy Server:**

If you wish to use a proxy server for your browser tests (Chrome and Firefox only), you can add ``--proxy=IP_ADDRESS:PORT`` as an argument on the command line.

```bash
pytest proxy_test.py --proxy=IP_ADDRESS:PORT
```

To make things easier, you can add your frequently-used proxies to PROXY_LIST in [proxy_list.py](https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/config/proxy_list.py), and then use ``--proxy=KEY_FROM_PROXY_LIST`` to use the IP_ADDRESS:PORT of that key.

```bash
pytest proxy_test.py --proxy=proxy1
```

<a id="utilizing_advanced_features"></a>
### ![http://seleniumbase.com](https://cdn2.hubspot.net/hubfs/100006/images/super_logo_tiny.png "SeleniumBase") **Production Environments & Integrations:**

Here are some things you can do to setup a production environment for your testing:

* You can setup a [Jenkins](https://jenkins.io/) build server for running tests at regular intervals. Jenkins has many plugins available, such as [the Xvfb headless browser plugin](https://wiki.jenkins-ci.org/display/JENKINS/Xvfb+Plugin) for running tests on a machine with no GUI. If you have Xvfb running in the background, you can add ``--headless`` to your run command in order to utilize it. For more info about the Xvfb plugin, [read this](http://qxf2.com/blog/xvfb-plugin-for-jenkins-selenium/). For a real-world Jenkins example of headless browser automation in action, check out [the SeleniumBase Google Cloud ReadMe](https://github.com/seleniumbase/SeleniumBase/blob/master/integrations/google_cloud/ReadMe.md).

* You can use [the Selenium Grid](https://github.com/SeleniumHQ/selenium/wiki/Grid2) to scale your testing by distributing tests on several machines with parallel execution. To do this, check out the SeleniumBase [selenium_grid folder](https://github.com/seleniumbase/SeleniumBase/tree/master/integrations/selenium_grid), which should have everything you need. The [Selenium Grid ReadMe](https://github.com/seleniumbase/SeleniumBase/blob/master/integrations/selenium_grid/ReadMe.md) will help you get started.

* If you're using the [SeleniumBase MySQL feature](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/mysql_installation.md) to save results from tests running on a server machine, you can install [MySQL Workbench](http://dev.mysql.com/downloads/tools/workbench/) to help you read & write from your DB more easily. You'll also need to install the MySQL-Python connector. Depending on your system, you may have to install this a bit differently from the command below:

```bash
pip install MySQL-python==1.2.5
```

* If you use [Slack](https://slack.com), you can easily have your Jenkins jobs display results there by using the [Jenkins Slack Plugin](https://github.com/jenkinsci/slack-plugin). Another way to send messages from your tests to Slack is by using [Slack's Incoming Webhooks API](https://api.slack.com/incoming-webhooks).

* If you use [HipChat](https://www.hipchat.com/), you can easily have your Jenkins jobs display results there by using the [Jenkins HipChat Plugin](https://wiki.jenkins-ci.org/display/JENKINS/HipChat+Plugin). Another way is by using the [hipchat_reporting plugin](https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/plugins/hipchat_reporting_plugin.py) (nosetests only).

<a id="amazon_section"></a>
* If you're using AWS, you can setup an [Amazon S3](http://aws.amazon.com/s3/) account for saving your log files and screenshots for future viewing. SeleniumBase already has [all the code you need to connect to S3](https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/plugins/s3_logging_plugin.py). You'll need to modify [settings.py](https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/config/settings.py) with connection details to your instance and the location in S3 where you want log files to be saved. You'll also need to add "``--with-s3_logging``" on the command line when you run your tests.

Here's an example of running tests with additional features enabled:
```bash
nosetests [YOUR_TEST_FILE].py --browser=chrome --with-db_reporting --with-s3_logging -s
```
(NOTE: If you haven't configured your MySQL or S3 connections in [settings.py](https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/config/settings.py), don't use ``--with-db_reporting`` or ``--with-s3_logging``.)

When the testing_base plugin is used, if there's a test failure, the basic_test_info plugin records test logs, the page_source plugin records the page source of the last web page seen by the test, and the screen_shots plugin records the image of the last page seen by the test where the failure occurred. Make sure you always include testing_base whenever you include a plugin that logs test data. The db_reporting plugin records the status of all tests run into your MySQL DB. The s3_logging plugin uploads basic test info, screenshots, and page source into your S3 storage folder.

To simplify that long run command, you can create a *.cfg file, such as the one provided in the example, and enter your plugins there so that you can run everything by typing:

```bash
nosetests [YOUR_TEST_FILE].py --config=[MY_CONFIG_FILE].cfg
```

You can simplify that even more by using a setup.cfg file, such as the one provided for you in the examples folder. If you kick off a test run from within the folder that setup.cfg is location in, that file will automatically be used as your configuration, meaning that you wouldn't have to type out all the plugins that you want to use (or include a config file) everytime you run tests.

If you tell nosetests to run an entire file, it will run every method in that python file that starts with "test". You can be more specific on what to run by doing something like:

```bash
nosetests [YOUR_TEST_FILE].py:[SOME_CLASS_NAME].test_[SOME_TEST_NAME] --config=[MY_CONFIG_FILE].cfg
```

Let's try an example of a test that fails:
```python
""" test_fail.py """
from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_find_army_of_robots_on_xkcd_desert_island(self):
        self.open("http://xkcd.com/731/")
        self.assert_element("div#ARMY_OF_ROBOTS", timeout=1)  # This should fail
```

You can run it from the ``examples`` folder like this:

```bash
nosetests test_fail.py
```

You'll notice that a logs folder, "latest_logs", was created to hold information about the failing test, and screenshots. Take a look at what you get. Remember, this data can be saved in your MySQL DB and in S3 if you include the necessary plugins in your run command (and if you set up the neccessary connections properly). For future test runs, past test results will get stored in the archived_logs folder if you have ARCHIVE_EXISTING_LOGS set to True in [settings.py](https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/config/settings.py).


<img src="https://cdn2.hubspot.net/hubfs/100006/images/logo_base_4b.png" title="SeleniumBase" height="120">

<a id="detailed_method_specifications"></a>
### ![http://seleniumbase.com](https://cdn2.hubspot.net/hubfs/100006/images/super_logo_tiny.png "SeleniumBase") **Detailed Method Specifications and Examples:**

#### Navigating to a web page (and related commands)

```python
self.open("https://xkcd.com/378/")  # This method opens the specified page.

self.go_back()  # This method navigates the browser to the previous page.

self.go_forward()  # This method navigates the browser forward in history.

self.refresh_page()  # This method reloads the current page.

self.get_current_url()  # This method returns the current page URL.

self.get_page_source()  # This method returns the current page source.
```

**ProTip™:** You may need to use the get_page_source() method along with Python's find() command to parse through the source to find something that Selenium wouldn't be able to. (You may want to brush up on your Python programming skills for that.)
Ex:
```python
source = self.get_page_source()
first_image_open_tag = source.find('<img>')
first_image_close_tag = source.find'</img>', first_image_open_tag)
everything_inside_first_image_tags = source[first_image_open_tag+len('<img>'):first_image_close_tag]
```

#### Clicking

To click an element on the page:

```python
self.click("div#my_id")
```

**ProTip™:** In most web browsers, you can right-click on a page and select ``Inspect Element`` to see the CSS selector details that you'll need to create your own scripts.

#### Typing Text

self.update_text(selector, text)  # updates the text from the specified element with the specified value. An exception is raised if the element is missing or if the text field is not editable. Example:

```python
self.update_text("input#id_value", "2012")
```

You can also use self.add_text() or the WebDriver .send_keys() command, but those won't clear the text box first if there's already text inside.
If you want to type in special keys, that's easy too. Here's an example:

```python
from selenium.webdriver.common.keys import Keys
self.find_element("textarea").send_keys(Keys.SPACE + Keys.BACK_SPACE + '\n')  # the backspace should cancel out the space, leaving you with the newline
```

#### Getting the text from an element on a page

```python
text = self.get_text("header h2")
```

#### Getting the attribute value from an element on a page

```python
attribute = self.get_attribute("#comic img", "title")
```

#### Asserting existance of an element on a page within some number of seconds:

```python
self.wait_for_element_present("div.my_class", timeout=10)
```
(NOTE: You can also use: ``self.assert_element_present(ELEMENT)``)

#### Asserting visibility of an element on a page within some number of seconds:

```python
self.wait_for_element_visible("a.my_class", timeout=5)
```
(NOTE: The short versions of this are ``self.find_element(ELEMENT)`` and ``self.assert_element(ELEMENT)``. The find_element() version returns the element)

Since the line above returns the element, you can combine that with .click() as shown below:

```python
self.find_element("a.my_class", timeout=5).click()

# But you're better off using the following statement, which does the same thing:

self.click("a.my_class")  # DO IT THIS WAY!
```

**ProTip™:** You can use dots to signify class names (Ex: ``div.class_name``) as a simplified version of ``div[class="class_name"]`` within a CSS selector. 

You can also use ``*=`` to search for any partial value in a CSS selector as shown below:

```python
self.click('a[name*="partial_name"]')
```

#### Asserting visibility of text inside an element on a page within some number of seconds:

```python
self.assert_text("Make it so!", "div#trek div.picard div.quotes")
self.assert_text("Tea. Earl Grey. Hot.", "div#trek div.picard div.quotes", timeout=3)
```
(NOTE: ``self.find_text(TEXT, ELEMENT)`` and ``self.wait_for_text(TEXT, ELEMENT)`` also do this. For backwords compatibility, older method names were kept, but the default timeout may be different.)

#### Asserting Anything

```python
self.assertTrue(myvar1 == something)

self.assertEqual(var1, var2)
```

#### Useful Conditional Statements (with creative examples in action)

is_element_visible(selector)  # is an element visible on a page
```python
import logging
if self.is_element_visible('div#warning'):
    logging.debug("Red Alert: Something bad might be happening!")
```

is_element_present(selector)  # is an element present on a page
```python
if self.is_element_present('div#top_secret img.tracking_cookie'):
    self.contact_cookie_monster()  # Not a real method unless you define it somewhere
else:
    current_url = self.get_current_url()
    self.contact_the_nsa(url=current_url, message="Dark Zone Found")  # Not a real method unless you define it somewhere
```
Another example:
```python
def is_there_a_cloaked_klingon_ship_on_this_page():
    if self.is_element_present("div.ships div.klingon"):
        return not self.is_element_visible("div.ships div.klingon")
    return False
```

is_text_visible(text, selector)  # is text visible on a page
```python
def get_mirror_universe_captain_picard_superbowl_ad(superbowl_year):
    selector = "div.superbowl_%s div.commercials div.transcript div.picard" % superbowl_year
    if self.is_text_visible("For the Love of Marketing and Earl Grey Tea!", selector):
        return "Picard HubSpot Superbowl Ad 2015"
    elif self.is_text_visible("Delivery Drones... Engage", selector):
        return "Picard Amazon Superbowl Ad 2015"
    elif self.is_text_visible("Bing it on Screen!", selector):
        return "Picard Microsoft Superbowl Ad 2015"
    elif self.is_text_visible("OK Glass, Make it So!", selector):
        return "Picard Google Superbowl Ad 2015"
    elif self.is_text_visible("Number One, I've Never Seen Anything Like It.", selector):
        return "Picard Tesla Superbowl Ad 2015"
    elif self.is_text_visible("""With the first link, the chain is forged.
                              The first speech censored, the first thought forbidden,
                              the first freedom denied, chains us all irrevocably.""", selector):
        return "Picard Wikimedia Superbowl Ad 2015"
    elif self.is_text_visible("Let us make sure history never forgets the name ... Facebook", selector):
        return "Picard Facebook Superbowl Ad 2015"
    else:
        raise Exception("Reports of my assimilation are greatly exaggerated.")
```

#### Switching Tabs

What if your test opens up a new tab/window and now you have more than one page? No problem. You need to specify which one you currently want Selenium to use. Switching between tabs/windows is easy:
Ex:

```python
self.switch_to_window(1)  # this switches to the new tab (0 is the first one)
```

**ProTip™:** iFrames follow the same principle as new windows - you need to specify the iFrame if you want to take action on something in there
Ex:

```python
self.switch_to_frame('ContentManagerTextBody_ifr')
# Now you can act inside the iFrame
# .... Do something cool (here)
self.switch_to_default_content()  # exit the iFrame when you're done
```

#### Handle Pop-Up Alerts

What if your test makes an alert pop up in your browser? No problem. You need to switch to it and either accept it or dismiss it:
Ex:

```python
self.wait_for_and_accept_alert()

self.wait_for_and_dismiss_alert()
```

If you're not sure whether there's an alert before trying to accept or dismiss it, one way to handle that is to wrap your alert-handling code in a try/except block. Other methods such as .text and .send_keys() will also work with alerts.

#### Executing Custom jQuery Scripts:

jQuery is a powerful JavaScript library that allows you to perform advanced actions in a web browser.
If the web page you're on already has jQuery loaded, you can start executing jQuery scripts immediately.
You'd know this because the web page would contain something like the following in the HTML:

```html
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
```

It's OK if you want to use jQuery on a page that doesn't have it loaded yet. To do so, run the following command first:

```python
self.activate_jquery()
```

Here are some examples of using jQuery in your scripts:
```python
self.execute_script('jQuery, window.scrollTo(0, 600)')  # Scrolling the page

self.execute_script("jQuery('#annoying-widget').hide()")  # Hiding elements on a page

self.execute_script("jQuery('#hidden-widget').show(0)")  # Showing hidden elements on a page

self.execute_script("jQuery('#annoying-button a').remove()")  # Removing elements on a page

self.execute_script("jQuery('%s').mouseover()" % (mouse_over_item))  # Mouse-over elements on a page

self.execute_script("jQuery('input#the_id').val('my_text')")  # Fast text input on a page

self.execute_script("jQuery('div#dropdown a.link').click()")  # Click elements on a page

self.execute_script("return jQuery('div#amazing')[0].text")  # Returns the css "text" of the element given

self.execute_script("return jQuery('textarea')[2].value")  # Returns the css "value" of the 3rd textarea element on the page
```

In the following example, JavaScript is used to plant code on a page that Selenium can then touch after that:
```python
start_page = "https://xkcd.com/465/"
destination_page = "https://github.com/seleniumbase/SeleniumBase"
self.open(start_page)
referral_link = '''<a class='analytics test' href='%s'>Free-Referral Button!</a>''' % destination_page
self.execute_script('''document.body.innerHTML = \"%s\"''' % referral_link)
self.click("a.analytics")  # Clicks the generated button
```
(Due to popular demand, this traffic generation example has been baked into SeleniumBase with the ``self.generate_referral(start_page, end_page)`` and the ``self.generate_traffic(start_page, end_page, loops)`` methods.)

#### Using delayed asserts:

Let's say you want to verify multiple different elements on a web page in a single test, but you don't want the test to fail until you verified several elements at once so that you don't have to rerun the test to find more missing elements on the same page. That's where delayed asserts come in. Here's the example:

```python
from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_delayed_asserts(self):
        self.open('http://xkcd.com/993/')
        self.wait_for_element('#comic')
        self.delayed_assert_element('img[alt="Brand Identity"]')
        self.delayed_assert_element('img[alt="Rocket Ship"]')  # Will Fail
        self.delayed_assert_element('#comicmap')
        self.delayed_assert_text('Fake Item', '#middleContainer')  # Will Fail
        self.delayed_assert_text('Random', '#middleContainer')
        self.delayed_assert_element('a[name="Super Fake !!!"]')  # Will Fail
        self.process_delayed_asserts()
```

``delayed_assert_element()`` and ``delayed_assert_text()`` will save any exceptions that would be raised.
To flush out all the failed delayed asserts into a single exception, make sure to call ``self.process_delayed_asserts()`` at the end of your test method. If your test hits multiple pages, you can call ``self.process_delayed_asserts()`` at the end of all your delayed asserts for a single page. This way, the screenshot from your log file will have the location where the delayed asserts were made.

#### Accessing raw WebDriver

If you need access to any commands that come with standard WebDriver, you can call them directly like this:
```python
self.driver.delete_all_cookies()
capabilities = self.driver.capabilities
self.driver.find_elements_by_partial_link_text("GitHub")
```
(In general, you'll want to use the SeleniumBase versions of methods when available.)

####  Checking Email: 
Let's say you have a test that sends an email, and now you want to check that the email was received:

```python
from seleniumbase.fixtures.email_manager import EmailManager, EmailException
num_email_results = 0
email_subject = "This is the subject to search for (maybe include a timestamp)"
email_manager = EmailManager("[YOUR SELENIUM GMAIL EMAIL ADDRESS]")  # the password for this is elsewhere (in the library) because this is a default email account
try:
    html_text = email_manager.search(SUBJECT="%s" % email_subject, timeout=300)
    num_email_results = len(html_text)
except EmailException:
    num_email_results = 0
self.assertTrue(num_email_results)  # true if not zero
```

Now you can parse through the email if you're looking for specific text or want to navigate to a link listed there.


####  Database Powers: 
Let's say you have a test that needs to access the database. First make sure you already have a table ready. Then try this example:

```python
from seleniumbase.core.mysql import DatabaseManager
def write_data_to_db(self, theId, theValue, theUrl):
    db = DatabaseManager()
    query = """INSERT INTO myTable(theId,theValue,theUrl)
               VALUES (%(theId)s,%(theValue)s,%(theUrl)s)"""
    db.execute_query_and_close(query, {"theId":theId,
                               "theValue":theValue,
                               "theUrl":theUrl})
```

Access credentials are stored in [settings.py](https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/config/settings.py) for your convenience (you have to add them first).

The following example below (taken from the Delayed Data Manager) shows how data can be pulled from the database.

```python
import logging
from seleniumbase.core.mysql import DatabaseManager

def get_delayed_test_data(self, testcase_address, done=0):
    """ Returns a list of rows """
    db = DatabaseManager()
    query = """SELECT guid,testcaseAddress,insertedAt,expectedResult,done
               FROM delayedTestData
               WHERE testcaseAddress=%(testcase_address)s
               AND done=%(done)s"""
    data = db.fetchall_query_and_close(query, {"testcase_address":testcase_address, "done":done})
    if data:
        return data
    else:
        logging.debug("Could not find any rows in delayedTestData.")
        logging.debug("DB Query = " + query % {"testcase_address":testcase_address, "done":done})
        return []
```

Now you know how to pull data from your MySQL DB.

Delayed Data usage example: If you scheduled an email to go out 3 hours from now and you wanted to check that the email gets received (but you don't want your test sitting idle for 3 hours) you can store the email credentials as a unique time-stamp for the email subject in the DB (along with a time for when it's safe for the email to be searched for) and then a later-running test can do the checking after the right amount of time has passed.


### ![http://seleniumbase.com](https://cdn2.hubspot.net/hubfs/100006/images/super_logo_tiny.png "SeleniumBase") Wrap-Up

**Congratulations** on learning how to use **SeleniumBase**!

<i>**Questions or Comments?**</i><br>
[![Join the chat at https://gitter.im/seleniumbase/SeleniumBase](https://badges.gitter.im/seleniumbase/SeleniumBase.svg)](https://gitter.im/seleniumbase/SeleniumBase?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)<br>

[https://github.com/mdmintz](https://github.com/mdmintz)<br>
[https://www.linkedin.com/in/mdmintz](https://www.linkedin.com/in/mdmintz)<br>

<img src="https://cdn2.hubspot.net/hubfs/100006/images/new_logo_pre6c.png" title="SeleniumBase" height="40"> <br> <img src="https://cdn2.hubspot.net/hubfs/100006/images/logo_base_4b.png" title="SeleniumBase" height="150">
