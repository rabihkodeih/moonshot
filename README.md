# Moonshot Test App

## Summary
This is the moonshot weather desktop app. Technolgies used are Python3.6 and Gtk+.


## Screen Shots
These are some screenshots for the app:

<span>
<img src="https://github.com/rabihkodeih/moonshot/blob/master/assets/screenshot_1.png" alt="alt text" width="270" >
&nbsp&nbsp&nbsp&nbsp
<img src="https://github.com/rabihkodeih/moonshot/blob/master/assets/screenshot_2.png" alt="alt text" width="270" >
&nbsp&nbsp&nbsp&nbsp
<img src="https://github.com/rabihkodeih/moonshot/blob/master/assets/screenshot_3.png" alt="alt text" width="270" >
</span>

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

Here is a summary of important modules and packages:

    main.py         : implements the main window object and application launching logic
    storage.py      : implements the data storage engine (based on sqlite3)
    app_state.py    : the application state management module, get/save app state data
    settings.py     : holds the settings used by the app
    components      : package of all UI components
    dialogs         : package of all UI dialogs


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

Run the application:

    python main.py


## Installation (Ubuntu)

First make sure that `Python3`, `pip3` and `virtualenv` are all installed and working fine:

    sudo apt-get update
    sudo apt-get dist-upgrade
    sudo apt-get install -y python3-dev virtualenv gcc 
    sudo apt-get install libgtk-3-dev
    sudo apt-get install python3-gi
    sudo apt-get install libffi

Clone the repository into a destination directory, cd into it then create your virtual env using

    virtualenv -p python3 env
    
and activate it by

    . env/bin/activate
    
Now you can install the requirements by

    pip3 install -r requirements.txt

Run the application:

    python main.py
        


## Tests

To run test, simply issue:

    python tests.py
    
The output should be something like this:

    (tests.py:4597): Gtk-WARNING **: 15:08:25.502: Locale not supported by C library.
        Using the fallback 'C' locale.
    
    Test "storage_execute_query" passed.
    Test "storage_execute_scalar" passed.
    Test "storage_set_json_value" passed.
    Test "storage_set_txt_value" passed.
    ----------------------------------------------------------------------
    Ran 4 tests in 0.077s
    
    OK

(end of readme)




