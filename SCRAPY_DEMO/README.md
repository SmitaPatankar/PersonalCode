# Why to use Scrapy?
To fetch and filter source code of website

# What are additional features of Scrapy?
Follows the website's robot.txt instructions by default

# What is Scrapy project structure?
```
project folder
    project folder
        settings.py
            # bot name, robots txt obey, concurrent requests, user agent, auto throttle, 
            # middleware, delay, cache, cookies, pipelines priority, extensions, headers, telnet console etc
        items.py
            # project item class that inherits from scrapy Item class
            # scrapy field objects
        pipelines.py
            # db library imported by us
            # project pipeline class
            # process item function
            # init function created by us for db conn and curr init
        middlewares.py
            # project source middleware class
            # from crawler function that creates spider
            # process spider input function
            # process spider output function 
        spiders folder
            <<our spider name>>.py (imports items.py)
                # imports scrapy.http FormRequest class for login
                # imports open_in_browser
                # our spider class that inherits from scrapy Spider class
                # name variable
                # allowed domains variable
                # start urls variable
                # parse function that logs in and parses response and yields item and follows next pages
        scrapy.cfg
            # default settings file and project deployment url
```

# How to install Scrapy and its dependencies(automatically)?
Dependencies are for parsing, selectors, cryptography etc.
```
pip install scrapy
pip install scrapy-useragents
pip install scrapy-proxy-pool
```

# How to start Scrapy project?
```
scrapy startproject <<project name>>
```

# How to generate Scrapy spider?
```
cd <<project_dir>>
scrapy genspider <<spider name>> <<website domain>>
```

# How to execute Scrapy program?
```
scrapy crawl <<spider name>> -o <<output file name>>.json  # xml  # csv
```

# How to find css selectors for Scrapy?
```
scrapy shell "<<website domain>>"
<<command for parsing response>>
```

# How to form css selectors?
can use selector gadget extension on chrome if needed

combine these as needed
use space for child
```
tagname
.classname
#id
::text
::attr(href)
```

# How to form xpaths?
```
//tagname
[@class='classname']
[@id='id']
/text()
@href
```

# How to start with mysql?
- install mysql and go to UI(workbench)
- create connection
- connect
- create schema

# How to start with mongodb?
- install mongodb
- create C:/data/db folder
- Run C:/Program Files/MongoDB/Server/{version}/bin/mongod.exe

# How to see login parameters?
inspect and check networks tab while clicking on login button

# How to get CSRF token for login?
view page source from login page before logging in for csrf_token

# How to get browser user-agent?
Use google bot desktop link from below:
https://developers.google.com/search/docs/advanced/crawling/overview-google-crawlers

# How to get multiple user-agents to use on rotation?
Use these lines in settings.py as middleware:
https://pypi.org/project/scrapy-user-agents/

# How to get multiple IPs to use on rotation?
paste line from here in settings.py for middleware:
https://github.com/rejoiceinhope/scrapy-proxy-pool
