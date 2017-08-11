#EXAMPLE TO GET BLOCK FOR ADDRESS
http://geocoding.geo.census.gov/geocoder/geographies/address?street=4600+Silver+Hill+Rd&city=Suitland&state=MD&benchmark=Public_AR_Census2010&vintage=Census2010_Census2010&layers=14&format=json

#RESOURCES TO GET DATA BY BLOCKS
http://api.census.gov/data/2010/sf1.html

This code retrieves 2010-2014 5-Year Census Data: https://www.census.gov/data/developers/data-sets/acs-5year.2014.html

## Configuration and Setup

Setup virtual environment
```
$ virtualenv venv 
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Create a filed name key.ini as follows
```
[key]
value: YOUR_KEY
```
Replace YOUR_KEY with the key that you get from http://api.census.gov/data/key_signup.html

CSV 'addresses.csv' with fields ordered: id street city state zip

Create a postgres database locally (avoid names starting with 'census' or 'newcensus')
```
$  sudo -u postgres createdb database1census
```
Open models.py, and re-define correctly your engine variable (line 6): substitute with the name of the databse you just created after localhost/

Add the tables to your database
```
$ python models.py
```
Note: you might be prompted to install psycopg2 beforehand


## Usage

Get geography for the addresses listed in addresses.csv.  First import the addresses from csv to the DB.
Name the file "addresses.csv" and arrange the columns: id, street, city, state, zipcode
```
$ python import_addresses.py
```
Download query data for each address
```
$ python download_geography.py
```
Due to connection problems, not all entries might download (You will see 'Failed to Open' while the code is running). This can result in parsing errors in the next step. To avoid that, just repeat the download command until eveything is downloaded properly. 

Parse results and import to DB
```
$ python parse_geography.py
```
You might get a KeyError BLOCK associated to a particular .json file. Open the specific .json file and you might see 'Layer query encountered an error: java.lang.RuntimeException: Failed to return' at the beginning. Delete this .json file and re-run the 'python download_geography.py' command again. Repeat until all .json files have downloaded correctly.

Download and then parse block data
```
$ python download_blkdata.py
$ python parse_blkdata.py
```
Export to csv
```
$ python export.py
```





