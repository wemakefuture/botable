# botable
Simple tool to test after how many requests a website blocks access.

## Installation
1. Install python requirements.
1. Run `./get_geckodriver.sh`

## Usage
```
usage: botable.py [-h] -p PAGE -x XPATH [-s SLEEP] [-hl] [-d DRIVER]
                  [-c CYCLES]

required arguments:
  -p PAGE, --page PAGE  URL of the website to be tested
  -x XPATH, --xpath XPATH
                        Xpath for an element on the page

optional arguments:
  -s SLEEP, --sleep SLEEP
                        Sleep between calls in seconds
  -hl, --headless       Set browser in headless mode
  -d DRIVER, --driver DRIVER
                        Location of the geckodriver
  -c CYCLES, --cycles CYCLES
                        On how many cycles should an output occur
```