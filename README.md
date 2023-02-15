# New Russian Wine

This is websie of author's wine store named "New Russian Wine".


## Requirements

 - python3
 - `Jinja2` library
 - `pandas` library
 - `openpyxl` library


## How to install

Get the source code of this repo:
```
git clone https://github.com/leksuss/wine.git
```

Open project folder:
```
cd wine
```

Then install dependencies:
```
# If you would like to install dependencies inside virtual environment, you should create it first.
pip3 install -r requirements.txt
```

## How to use

To run the script you need to prepare xlsx file with wine data. `wine.xlsx` is example of this file, you can find it in the root directory of this repo. Then run the script and pass the path to this file as an argument:

```
python3 main.py wine.xlsx
```

Then open webpage [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
