# New Russian Wine

This is websie of author's wine store named "New Russian Wine".


## Requirements

 - python3
 - `Jinja2` library
 - `pandas` library


## How to install

Get the source code of this repo:
```
git clone https://github.com/leksuss/dvmn.git
```

Go to this script:
```
cd dvmn/wine
```

Then install dependencies:
```
# If you would like to install dependencies inside virtual environment, you should create it first.
pip3 install -r requirements.txt
```

## How to setup

To show actual goods at website you need to update file `wine.xlsx` with actual data. You can use this file as a template. After renaming file you should change `excel_file` variable in `main.py` file.

## How to use

Run script without arguments like this:
```
python3 bitly.py
```

Then open webpage [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
