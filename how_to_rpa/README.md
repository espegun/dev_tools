# How to RPA

## The purpose
There are several RPA libraries for Python, but looking at [this](https://research.aimultiple.com/python-rpa/) in March 2021, you clearly want to use the one from Robot FrameWork Foundation.
An (unexplored) alternative is UiPath.

## How does it work?

## Useful commands
You may install the entire rpaframework or just Selenium (browser automation). Selenium is mostly meant for testing, but can be used for any browser automation.  
`$ pip install rpaframework`  
`$ pip install selenium`  
Se examples (using the full rpaframework).

## You may also deploy this on an EC2 instance
[Selenium and Chrome on an EC2 instance](https://praneeth-kandula.medium.com/running-python-scripts-on-an-aws-ec2-instance-8c01f9ee7b2f)  
`$ sudo yum install libX11` You may also have to install this if the chromedriver version can't be found.  

What to do on the EC2 instance (when logged in through SSH and having python and pip runnning, see [here](https://github.com/espegun/AWS/tree/main/how_to_EC2)).
```
cd /tmp/
wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo yum install libX11  # Install missing 
chromedriver --version
```
```
curl https://intoli.com/install-google-chrome.sh | bash
sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
google-chrome --version && which google-chrome
```

`pip install selenium/rpaframework` Preferably in a virtual environment





## Useful links
[RPA Framework main page](https://rpaframework.org/#)  
[RPA Framework GitHub](https://github.com/robotframework/foundation)  
[Selenium Webdriver](https://www.selenium.dev/documentation/en/getting_started/quick/)  

