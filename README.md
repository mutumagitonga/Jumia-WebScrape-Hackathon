
!["Jumia Kenya E-Commerce Website"](<https://i0.wp.com/mycoupontap.com/wp-content/uploads/2022/06/Jumia-Kenya-Voucher-Code.png> "Jumia Kenya")

# Jumia E-Commerce Webscrape Project

![GitHub commit activity](https://img.shields.io/github/commit-activity/t/mutumagitonga/Jumia-WebScrape-Hackathon)

![Static Badge](https://img.shields.io/badge/collaborators-2-orange)

![Static Badge](https://img.shields.io/badge/release-no_releases_found-orange)

![Static Badge](https://img.shields.io/badge/pull_requests-0%20open-orange)

![GitHub License](https://img.shields.io/github/license/mutumagitonga/Jumia-WebScrape-Hackathon?color=orange)







## Project Overview
This project involves scraping all products from the popular Kenyan e-commerce site Jumia. The project generally aims to identify general patterns of the listed products including price distribution, discount distribution, rating distribution, popular names in product labels, & relationships between all the numerical columns. 


## Installation

### Installation Step 1 - Clone project
Clone this project into your desired local machine folder as below: 
```bash
  git clone git@github.com:mutumagitonga/Jumia-WebScrape-Hackathon.git
```
Instead if ssh authentication is not already setup, use the method below: 
```bash
  git clone https://github.com/mutumagitonga/Jumia-WebScrape-Hackathon.git
```
### Installation Step 2 - Check python version
Before proceeding to the next stage, ensure python's installed in your machine, in any of the 3 platforms - Linux, Windows, or MacOS. Run the command `python -V` in your terminal to check python version - it should be returned if Python installed properly otherwise Python is not installed or there's a problem with your Python installation.

NB: Ensure you have Python 3.3 or above installed.

If Python is not installed, [click here](https://tinyurl.com/43k9evvv) for installation instructions for any of the 3 platforms. 

### Installation Step 3 - Install the virtual environment
Once that's cleared, install a virtual python environment within the cloned project folder:
```bash
  python3 -m venv my_env
```
In the above codeline, you can replace `my_env` with a name of your own for the virtual environment. 

**Purpose of virtual environment:** Isolates a project's dependencies (to be installed) from other projects and the system-wide Python installation. In other words, it contains:  
- A Python interpreter.
- A Python standard library.
- The 3rd party packages(to be installed).

### Installation Step 4 - Activating the virtual environment

On Windows: `my_env\Scripts\activate`

On MacOS/Linux: `source venv/bin/activate`

Once activated, the terminal path indicator changes indicating the virtual environment is now active. 

Still, one can confirm the activated virtual environment by running the command `which python` which displays a path to the python executable in the virtual environment. 


### Installation Step 5 - Installing dependencies in requirements.txt
With the virtual environment ready, it's time to install libraries (dependencies) in the requirements.txt file.

The command is shown below: 
```bash
  pip install -r requirements.txt
```
The -r flag instructs pip package manager to read requirements from a file instead of taking a package name argument on the commandline. 

As the command runs, it downloads and installs the required packages in the virtual environment `my_env`

Once done with the project work, the virtual environment can be deactivated by running the command: `deactivate` and when work resumes, one can reactivate it as described in installation step 4. 


    
## Data
### Source Data



### Data Acquisition 

Raw data is acquired via web scraping. The target website is a popular Kenyan online retailer Jumia. 

**NB:** The following data acquisition procedure is explained as exhaustively as possible to allow quick replication of the process. However, if any problems are encountered, run the cells in the jupyter notebook `notebooks/1_jumia_webscrape.ipynb` consecutively for clarification.  

Therefore, the first step is visiting the root url of the website, `https://www.jumia.co.ke/` and exploring further to discover the location of the products' endpoint. 

Keen exploration reveals that the endpoint of interest is `https://www.jumia.co.ke/all-products/`. However, a query string, `?page=`, is appended to this endpoint to make the scraping practical (so that its done pagewise). 

Thus, the url becomes `https://www.jumia.co.ke/all-products/?page=`. So one uses the navigation tabs at the bottom of the page to discover the last page, in this case the total page count is found to be 50.   

Now the scraping technique involves employing a for-loop within which page numbers are appended at the end of the query string consecutively. An IF-condition check is done to ensure the scraping is only done when the products are absent (to prevent repeat scraping).  
```python
# Declare the products’ url & the total webpage count
other_pages_url = "https://www.jumia.co.ke/all-products/?page="
webpage_num_total = 50

# If scraped products csv doesn't exist, run the scraper function below & save products to csv ELSE continue & read csv
if not os.path.exists('../data/raw/all_products_list_raw.csv'):
    for page in range(1, webpage_num_total+1, 1):
        other_pages_url = "https://www.jumia.co.ke/all-products/?page="
        page = str(page)
        other_pages_url = other_pages_url + page
        # Fetching HTML data
        response = fetch_html_data(other_pages_url)
        # Converting to soup object
        soup = convert_web_data_to_beautiful_soup_obj(response)
        # Appending each product dictionary to all_products list
        append_one_product_details_dictionary_to_list(page)
    
    # Convert scraped list to dataframe
    df = pd.DataFrame(all_products_list)
    # Save scraped dataframe to csv to prevent scraping each time I run the notebook
    df.to_csv('../data/raw/all_products_list_raw.csv')
```
**NB:** The last 2 lines of the code snippet above run after all the product pages have been scraped. The 2nd last line creates a pandas dataframe from the list of products' data attributes dictionaries while the last line saves the dataframe as a csv. The csv file is saved once to store the scraped data thus preventing the scraper from re-running each time the entire notebook is run.  

For each page, the url is passed to a function fetching the html data which is called `fetch_html_data` in the previous code snippet. The `fetch_html_data` is expounded below:
```python
def fetch_html_data(web_address):
    try:
        # print(f"\nFetching data from {web_address}...")
        res = req.get(web_address)
        return res
    except req.exceptions.RequestException as e:
        print('Stopped:', e)
    except TypeError as e:
        print('Stopped:', e)
```

The HTML data response is then passed into a function that converts it into a beautiful soup object. The `convert_web_data_to_beautiful_soup_obj` function code is shown below:
```python
def convert_web_data_to_beautiful_soup_obj(web_data):
    try:
        # print("Creating BeautifulSoup object...")
        soup_obj = BeautifulSoup(web_data.text, "html.parser")
        # print("Success! Object created!")
        return soup_obj
    except Exception as e:
        print("Stopped:", e)
```

The page's beautiful soup object is then passed into another function in which the appropriate HTML element selects all products in the page and loads them into a list. 

Looping through all the page's products list, the required data attributes are scraped from each product and are loaded into a dictionary. 
Below is the `append_one_product_details_dictionary_to_list` function:
```python
all_products_list = []

def append_one_product_details_dictionary_to_list(pg):
    # print(f"Appending page {pg} products' details to array")
    
    page_products_details_soup = soup.find_all("article", class_="prd _fb col c-prd")
    
    for detail in page_products_details_soup:
        details_dict = {"name": detail.find("h3", class_="name").text.strip(),
                        "new_price": detail.find("div", class_="prc").text.strip(),
                        "old_price": detail.find("div", class_="old").text.strip() if detail.find("div", class_="old") else None,
                        "discount": detail.find("div", class_="bdg _dsct _sm").text.strip() if detail.find("div", class_="bdg _dsct _sm") else None,
                        "rating": detail.find("div", class_="stars _s").text.strip() if detail.find("div", class_="stars _s") else None,
                        "votes": detail.find("div", class_="rev").text.strip() if detail.find("div", class_="rev") else None}
        all_products_list.append(details_dict)

```  

Each dictionary containing a product's details is then appended into a master list in the last line: `all_products_list.append(details_dict)` (in the code snippet above). The `all_products_list` (will/shall) contain the dictionaries of all the products, starting from the first page products through to the last page products. 

Remember after the for-loop is completed, the list of dictionaries are converted into a dataframe & then stored as a csv as previously discussed.  


### Data Preprocessing
Acquired data is not always squeaky clean, so preprocessing them are an integral part of any data analysis. In this section you can talk about the same.

The attributes of the raw acquired data acquired may require cleaning before the data analysis process. 

**NB:** For supplementary information on this preprocessing stage, please consult the data analysis notebook found in `notebooks/1_jumia_webscrape.ipynb` then run the cells in sequence.  

Firstly, read the csv file that was stored earlier to get a pandas dataframe:
```python
# Read csv and specify index column to prevent creation of another redundant index
products_df = pd.read_csv('../data/raw/all_products_list_raw.csv', index_col=0)  # Read products list from csv
```
Secondly, check the summary info of the data attributes as shown below:
```python
products_df.info()
```
The info summary of the data attributes obtained via `products_df.info()` is as below: 
```python
<class 'pandas.core.frame.DataFrame'>
Index: 2000 entries, 0 to 1999
Data columns (total 6 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   name       2000 non-null   object
 1   new_price  2000 non-null   object
 2   old_price  1907 non-null   object
 3   discount   1907 non-null   object
 4   rating     109 non-null    object
 5   votes      109 non-null    object
dtypes: object(6)
memory usage: 109.4+ KB
```
The summary above indicates the necessity for preprocessing the data. Although the data has 2000 rows, it's clear that some rows have a high count of null values i.e., rating and votes while old_price and discount have a small count of the same. 

Another point of concern is that all columns have the object/string data type yet we know that's not the ideal scenario. More specifically, all columns save for name should be numeric. 

Therefore, the two fundamental areas of concern in the preprocessing stage are imputation (replacing missing values), and changing the column data types to their ideal types. However, there may be other minor points of concern that might require attention during the cleaning process - so an open mind is key to the process. 

#### Cleaning columns before changing their data types & imputing null values
1) Cleaning the ***new_price*** column:

From the summary, the *new_price* column has no null values since it has a non-null count of 2000 while the dataframe has 2000 rows. 

- Firstly, remove the 'Ksh' prefix from the new_price values (e.g.: KSh 854) and by splitting the value at the space character and returning the second value (at position 1 of the 3 split values). The condition for this operation is that the row cell should not be null and value should be a string (to prevent the split from occuring during a notebook re-run when the new_price values are already in float format):
```python
# Remove currency denotation 'Ksh' 
products_df['new_price'] = products_df['new_price'].apply(lambda x: x.split(' ')[1] if x is not None and isinstance(x,str) else x) 
```
- Now running `products_df['new_price'].head()`, some new_price values (thousands) have commas in them (e.g.: 21,506). Therefore, this comma needs to be removed. The condition for the comma removal is that it must be present in the value and the value must be a string i.e., should not yet have been converted to float: 
```python
# Remove comma from thousands price values
products_df['new_price'] = products_df['new_price'].apply(lambda x: x.replace(',','') if ',' in x and isinstance(x,str) else x)
```
- The next step is converting the data values to float. Here, the condition for the conversion function is skipping the null values and performing a type conversion of the rest:
```python
# Convert new_price column to float
products_df['new_price'] = products_df['new_price'].apply(lambda x: float(x) if x is not None else x)
```
Checking the datatype of this column using `print(products_df['new_price'].dtype)` reveals that the data type is now `float64`.

- The final step in cleaning the *new_price* column is saving the progress in a csv file from where the next step's dataframe shall begin: 
```python
# Saving stage one (new_price) data cleaning file to csv
products_df.to_csv("../data/processed/1_all_products_new_price_cleaned.csv")
```

2. Cleaning the ***old_price*** column:
From the dataframe summary above, this attribute has only 93 null values (1907 non-null value count against a total count of 2000 rows).

- Firstly, create a dataframe from the csv created in preprocessing stage 1:
```python
# Read csv file cleaned in the previous stage (new_price column) & convert to dataframe
products_df = pd.read_csv("../data/processed/1_all_products_new_price_cleaned.csv", index_col=0)
```
- Check unique values in this column to inform the data cleaning decisions:
```python
# Use [:10] notation to print the first 10 values
products_df['old_price'].unique()[:10]
``` 
As was the case with the *new_price* column, the values here have a currency name, thousands values have commas, and nulls equally exist. 

- Therefore, removing the kenyan currency name 'Ksh' in the prefix of the data value. The condition is that the value shouldn't be null and the value must be a string (for reasons explained above in a similar step): 
```python
# Remove currency name 'Ksh'
products_df['old_price'] = products_df['old_price'].apply(lambda x: x.split(' ')[1] if x is not None and isinstance(x,str) else x)
```
- Now removing commas from thousands values. The condition is that the value shouldn't be null and the value should be a string: 
```python
# Remove commas from values
products_df['old_price'] = products_df['old_price'].apply(lambda x: x.replace(',','') if x is not None and isinstance(x,str) else x)
```
- Now convert the string values into floats (where values are present): 
```python
# Now convert the string values into floats
products_df['old_price'] = products_df['old_price'].apply(lambda x: float(x) if x is not None else x)
```
A confirmation with `print(products_df['old_price'].dtype)` returns `float64`. Hence the conversion from string to float is successful. 

- Now save the dataframe cleaned thus far into a new csv file like below: 
```python
# Saving stage two data (old_price column) cleaning dataframe to csv
products_df.to_csv("../data/processed/2_all_products_old_price_cleaned.csv")
```
3. Cleaning the ***discount*** column:
From the dataframe summary info, the *discount* column has a similar number of null values as the *old_price* column - 93 nulls (1907 non-nulls vs 2000 counts). 

- Read the csv file saved in the previous preprocessing/cleaning step to obtain a dataframe:
```python
# Read csv file from stage 2 (old_price column cleanup) & convert to dataframe
products_df = pd.read_csv("../data/processed/2_all_products_old_price_cleaned.csv", index_col=0)
```
- Check for unique values to inform the cleaning steps to take: 
```python
# Use [:10] notation to print the first 10 values
products_df['discount'].unique()[:10]
```
Running the above reveals there're 2 key types of data number percentages in string format (e.g. 34%) and null values. 

- Therefore, the first step is removing the percent sign at the suffix of the string values. The condition for removal is the value shouldn't be null and it should be a string:
```python
# Remove the percent sign
products_df['discount'] = products_df['discount'].apply(lambda x: x.replace('%','') if x is not None and isinstance(x,str) else x)
```
- Now the next step is converting the non-null string values into floats: 
```python
# Convert values into float & divide by 100 to represent the percentages as decimal values
products_df['discount'] = products_df['discount'].apply(lambda x: float(x)/100 if x is not None else x)
```
The percentages are converted to floats with a hundredths place value to ensure easier calculations later. 

- Saving the stage 3 preprocessed dataframe to a csv: 
```python
# Saving stage three data cleaning file to csv
products_df.to_csv("../data/processed/3_all_products_discount_cleaned.csv")
```

