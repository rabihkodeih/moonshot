# Moonshot Test App

## Summary
This is the moon shot weather desktop app. Technolgies used are Python3.6 and Gtk+.


## Screen Shots
These are some screenshots for the app:


<img src="https://github.com/rabihkodeih/moonshot/blob/master/assets/screenshot_1.png" alt="alt text" width="270" >

<img src="https://github.com/rabihkodeih/moonshot/blob/master/assets/screenshot_2.png" alt="alt text" width="270" >

<img src="https://github.com/rabihkodeih/moonshot/blob/master/assets/screenshot_3.png" alt="alt text" width="270" >


## Architecture
The app is designed using a main windows class (main.py module) and a number of components each having its own class
(components.py and dialogs.py modules). Each window/widget/component has one and only one method to refresh its UI, 
namely __class__.refresh(). All Gtk UI operations are handled in the main Gtk thread. 

Network operations and API fetches are performed using separate Python threads with Gtk locking for thread safety. 
An important concept in the app is the use of the app_state.py module which models the app's state (which is persistent). 
It also serves as a caching mechanism for weather API calls. For data persistence operations, standard sqlite3 package was used 
(storage.py module). 

The weather API info is fetched from openweathermap.com using its free  account. In addition a number of helpers and 
decoratros (utils.py module) are used to simplify the code logic and readability.


## Installation (MacOS)

First make sure that `Python3`, `pip3` and `virtualenv` are all installed and working fine:

    brew update
    brew install gtk+3
    brew install pygobject3
    brew install libffi
    export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig"
    
Clone the repository into a destination directory, cd into it then create your virtual env using

    virtualenv -p python3 env
    
and activate it by

    . env/bin/activate
    
Now you can install the requirements by

    pip3 install -r requirements.txt


## Installation (Ubuntu)

First make sure that `Python3`, `pip3` and `virtualenv` are all installed and working fine:

    apt-get update
    apt-get dist-upgrade
    apt-get install -y python3-dev virtualenv gcc 

Clone the repository into a destination directory, cd into it then create your virtual env using

    virtualenv -p python3 env
    
and activate it by

    . env/bin/activate
    
Now you can install the requirements by

    pip3 install -r requirements.txt
        




## Tests

A standard django test suite was employed. There are two test cases, one for login sessions and db models, the other for the api section.
To run test, simply issue:

    ./manage.py test




