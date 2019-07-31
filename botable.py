import argparse
import datetime
import signal
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as Firefox_Options
import os

running = True

def signal_handler(sig, frame):
    global running
    running = False

signal.signal(signal.SIGINT, signal_handler)

def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue

def start_test():
    global running
    parser = argparse.ArgumentParser(description='Tool to check how often a page can be called before blocking starts')
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument("-p", "--page", help="URL of the website to be tested", required=True)
    required.add_argument("-x", "--xpath", help="Xpath for an element on the page", required=True)
    optional.add_argument("-s", "--sleep", help="Sleep between calls in seconds", default=2, type=int)
    optional.add_argument("-hl", "--headless", help="Set browser in headless mode", action='store_true')
    optional.add_argument("-d", "--driver", help="Location of the geckodriver", default= os.getcwd() + "/geckodriver")
    optional.add_argument("-c", "--cycles", help="On how many cycles should an output occur", default=50, type=check_positive)
    args = parser.parse_args()

    firefox_options = Firefox_Options()
    if args.headless:
        firefox_options.add_argument('-headless')

    browser = webdriver.Firefox(options=firefox_options,executable_path=args.driver)
    count = 0
    start_time = datetime.datetime.now()
    print("Start testing...")
    while running:
        try:
            browser.get(url=args.page)
            sleep(args.sleep)
            browser.find_element_by_xpath(args.xpath)
            count+=1
            if count%args.cycles == 0:
                print(f"Current cycle: {str(count)}")
        except:
            running = False
            print("Stop testing...")

    end_time = datetime.datetime.now()
    runtime = end_time-start_time
    print(f"Result: Test running for {str(runtime)} and {str(count)} cycles")


if __name__ == "__main__":
    start_test()

