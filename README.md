
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


    