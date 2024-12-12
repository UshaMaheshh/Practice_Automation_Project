**Project Title**: Automated Testing of Practice Website \- practice.automationtesting.in

 

**Project Overview:** This project involved extensive manual and automated testing of the practice.automationtesting.in website, a platform designed for practicing software testing skills. The focus was on implementing and verifying test cases for critical sections of the site, including the Homepage, My Account, My Account \- Login, My Account \- Registration, and Shop. The goal was to ensure that all functionalities of these sections work as expected and meet quality standards.

 

**Objective:** The main objective was to implement, execute, and validate all the test cases outlined in the Test Cases menu for the Homepage, My Account (login and registration), and Shop sections. The project aimed to ensure that the website's features were functional, responsive, and user-friendly while enhancing proficiency in automated testing practices.

 

**Testing Approach:**

Automated Testing: Utilized Selenium WebDriver for browser automation and Python as the primary scripting language. Pytest was used for running test cases and generating comprehensive test reports. The automation framework was structured using the Page Object Model (POM) design pattern, which ensured maintainability and scalability. Data-Driven Testing (DDT) was applied to handle user account and login data sourced from Excel, enabling comprehensive test coverage.

Integrated Development Environment (IDE): The automation scripts were developed using PyCharm (Community Edition), which provided an efficient and user-friendly environment for coding and managing the project.

Database Validation: Verified data consistency using MySQL to ensure that data submitted through the web application was accurately reflected in the backend.

 

**Tools and Technologies Used:**

Selenium WebDriver: Automated browser interactions and user actions.

Python: The primary language for scripting the automated test cases.

Pytest: Ran the test cases and generated test reports.

Excel: Managed test data for Data-Driven Testing (DDT).

MySQL: Validated database records and ensured data consistency.

Page Object Model (POM): Applied as a design pattern to organize test scripts, improving code reusability and maintainability.

Data-Driven Testing (DDT): Enabled testing with multiple data sets sourced from Excel.

PyCharm (Community Edition): Used as the IDE for developing, debugging, and managing the Python-based automation scripts.

GitHub: Used for version control and repository management to track changes and facilitate collaboration

 

**How to Run the Project**

**Prerequisites**

* Python 3.x installed on your system.  
* Required Python libraries: selenium, pytest, openpyxl, mysql-connector-python.

**Installation**

1. Clone the project repository:

git clone https://github.com/your-username/your-repository.git cd your-repository

2. Install the required libraries:

pip install selenium pytest openpyxl mysql-connector-python

3. Ensure that **ChromeDriver** is installed and added to your system's PATH if using Chrome for browser automation.

 

**Setup & configure WebDriver in Pycharm**

**Pre-requisites:**

o   Python 3.x

o   Pycharm (community edition)

 

1\) Download browser specific drivers using below links....

Chrome:      	https://chromedriver.chromium.org/downloads

Edge:           	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Firefox:        	https://github.com/mozilla/geckodriver/releases

 

Once you donwloaded, extract .zip files then you will see .exe files ( they are drivers)

2\) setup selenium webdriver

        	Appraoch\#1:

                    	pip install selenium==4.0.0.b4

                    	pip install selenium

        	Appraoch\#2:

                    	or through Pycharm project settings...

 

         	

**Run Tests on Desired Browser(Cross Browser Testing)/Parallel**

   
o   update conftest.py with required fixtures which will accept command line argument (browser).  
o   Pass browser name as argument in command line

 

**To Run tests on desired browser**

pytest \-s \-v .\\testCases\\path\\your test filename \--browser edge  
   
**To Run tests parallel**

pytest \-s \-v **\-n=3** .\\testCases\\path\\your test filename \--browser edge

   
**To Generate pytest HTML Reports**
 
Update conftest.py with pytest hooks

**pytest \-s \-v \--html=reports\\report.html \--capture=tee-sys .\\testCases\\your test file name \--browser chrome**

**Example Report**
http://localhost:63342/PracticeProject2/reports/02-11-2024%2012-42-01.html?_ijt=upqk99juqgke52qvc3hd2tsac0&_ij_reload=RELOAD_ON_SAVE&sort=result
   
