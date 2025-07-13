# SauceDemo Manual and Automation Testing Project

This repository contains both **manual and automation testing artifacts** for the [SauceDemo](https://www.saucedemo.com/) web application. It simulates a complete real-world QA process covering requirement analysis, test planning, execution, defect tracking, and automation using Selenium.

---

## 📁 Folder Structure

```plaintext

📁 SauceDemo_Manual_And_Automation_Testing_Project/
├── 📂 1_Test_Plan/
│ └── 📄 SauceDemo_TestPlan.docx
│
├── 📂 2_Test_Cases/
│ ├── 📄 Cart_Module_TestCases.xlsx
│ ├── 📄 Checkout_Module_TestCases.xlsx
│ └── 📄 Login_Module_TestCases.xlsx
│
├── 📂 3_Test_Execution_Reports/
│ └── 📄 TestExecutionReport.xlsx
│
├── 📂 4_Bug_Reports/
│ ├── 📄 BugReport_#101_LoginError.docx
│ ├── 📄 BugReport_#102_CheckoutFail.docx
│ └── 📄 BugReport_Template.docx
│
├── 📂 5_Test_Scenarios/
│ └── 📄 SauceDemo_TestScenarios.xlsx
│
├── 📂 6_Traceability_Matrix/
│ └── 📄 RTM_SauceDemo.xlsx
│
├── 📂 Automation Testing Selenium/
│ ├── 📄 login_results.csv
│ ├── 📄 new.py
│ ├── 📂 .idea/
│ │ ├── 📄 .gitignore
│ │ ├── 📄 misc.xml
│ │ ├── 📄 modules.xml
│ │ ├── 📄 PythonProject.iml
│ │ ├── 📄 workspace.xml
│ │ └── 📂 inspectionProfiles/
│ │ └── 📄 profiles_settings.xml
│ └── 📂 screenshots_20250713_235220/
│ ├── 🖼️ error_user_unexpected.png
│ ├── 🖼️ locked_out_user.png
│ ├── 🖼️ performance_glitch_user_unexpected.png
│ ├── 🖼️ problem_user_unexpected.png

```


## ✅ 1. Requirement Analysis

This section outlines the core functional modules identified in the SauceDemo website and serves as the foundation for both manual and automated testing.

### 🔍 Website Under Test
**URL**: [https://www.saucedemo.com](https://www.saucedemo.com)

---

### 🧩 Core Modules to be Tested

1. **🔐 Login**
   - Validate user login with valid and invalid credentials
   - Check for locked user scenarios
   - Verify error messages for invalid inputs

2. **🛍️ Product Listing**
   - Display of products with name, price, and image
   - Sorting (by name, price, etc.)
   - Add product(s) to cart functionality

3. **🛒 Cart Management**
   - Verify items added to cart are correctly reflected
   - Remove individual items from cart
   - Verify total item count and price

4. **🧾 Checkout**
   - Fill customer information (First Name, Last Name, Zip Code)
   - Step-by-step navigation of checkout process
   - Calculate and verify total price

5. **✅ Order Confirmation**
   - Order summary page validation
   - Confirmation message after placing the order
   - Resetting cart after successful purchase

6. **🚪 Logout**
   - Logging out from the application via the side menu
   - Redirecting back to the login page


## 📌 Objective

The objective of this project is to ensure that the critical functionalities of the SauceDemo platform work as expected through:
- Manual Test Case Execution
- Automated Selenium Scripts using Python

  
## ✅ 2. Test Plan Creation

📁 **Document Location**: `1_Test_Plan/SauceDemo_TestPlan.docx`

This document outlines the structured approach for conducting both manual and automated testing of the SauceDemo web application.

---

### 📝 Contents of the Test Plan:

#### 🎯 Objective & Scope
- Define the goal of the testing effort
- Identify which functionalities of the SauceDemo site will be validated (Login, Cart, Checkout, etc.)

#### ✅ In-scope
- Functional Testing of all core modules
- Cross-browser testing on Chrome and Firefox
- Basic UI/UX validation

#### ❌ Out-of-scope
- Performance or load testing
- Testing on mobile browsers
- Security or penetration testing

#### 🧪 Test Environment
- **Browser**: Chrome (latest), Firefox
- **OS**: Windows 10/11
- **Tools**: Selenium WebDriver, PyTest, Excel, VS Code
- **Test URL**: https://www.saucedemo.com/

#### ⚠️ Assumptions & Constraints
- Application is stable and testable
- Internet connection is stable
- No backend access available for database validation

#### 📦 Test Deliverables
- Test Plan Document
- Test Cases in Excel
- Bug Reports
- Automated Test Scripts
- HTML Test Execution Report

#### 🚦 Entry Criteria
- Application is accessible
- Requirements are finalized
- Test environment is ready

#### 🛑 Exit Criteria
- All planned test cases executed
- All critical bugs are closed
- Automation test scripts executed and reports generated

## ✅ 3. Test Scenario Design

📁 **Document Location**: `5_Test_Scenarios/SauceDemo_TestScenarios.xlsx`

This file contains well-defined, prioritized test scenarios covering all core modules of the SauceDemo application.

---

### 📌 Format

| Module        | Test Scenario Description                        | Priority |
|---------------|--------------------------------------------------|----------|
| **Login**     | Verify login with valid credentials              | High     |
| **Login**     | Verify error message with invalid credentials    | High     |
| **Product Page** | Add multiple products to the cart              | Medium   |
| **Cart**      | Remove a product from the cart                   | Medium   |
| **Checkout**  | Complete checkout with valid data                | High     |
| **Logout**    | Verify user is logged out properly               | Low      |

---

### 🎯 Purpose

These scenarios serve as the foundation for:

- Writing detailed test cases (manual)
- Automating critical workflows (automated test scripts)
- Prioritizing testing efforts based on business impact

---

> 📎 Continue to the next section: [Manual Test Cases](#) or [Bug Reporting](#)



## ✅ 4. Test Case Design

📁 **Document Location**: `2_Test_Cases/`

Each module of the SauceDemo website has its own dedicated Excel test case file. These test cases are derived from the high-priority test scenarios and follow a structured format to ensure thorough validation.

---

### 📂 Example File

`Login_Module_TestCases.xlsx`

| TC ID  | Test Scenario      | Steps to Execute                          | Test Data                      | Expected Result                 | Status |
|--------|--------------------|-------------------------------------------|--------------------------------|----------------------------------|--------|
| TC001  | Valid Login        | Open URL → Enter credentials → Click Login | Username: `standard_user`<br>Password: `secret_sauce` | Redirect to Inventory page       | Pass   |
| TC002  | Invalid Password   | Enter valid username → Enter wrong password → Click Login | Username: `standard_user`<br>Password: `wrong_pass` | Show appropriate error message   | Fail   |

---

### ✍️ Key Fields

- **TC ID**: Unique identifier for each test case  
- **Test Scenario**: The scenario being tested  
- **Steps to Execute**: Detailed, sequential actions to be performed  
- **Test Data**: Inputs used for the test  
- **Expected Result**: The desired application behavior  
- **Status**: Pass / Fail / Not Executed

---

### 🔧 Additional Test Case Files (Examples)

- `Product_Module_TestCases.xlsx`
- `Cart_Module_TestCases.xlsx`
- `Checkout_Module_TestCases.xlsx`
- `Logout_Module_TestCases.xlsx`

---


## ✅ 5. Test Execution

📁 **Document Location**: `3_Test_Execution_Reports/TestExecutionReport.xlsx`

This file records the results of manual test case execution performed on the SauceDemo website. Each test case is tracked by its unique ID, execution status, and any relevant comments or observations.

---

### 📊 Sample Format

| Test Case ID | Status | Comments                   |
|--------------|--------|----------------------------|
| TC001        | Pass   | As expected                |
| TC002        | Fail   | Incorrect error message    |
| TC003        | Pass   | Cart updated successfully  |

---

### 🧾 Description of Columns

- **Test Case ID**: Maps to the original test cases from the test case design phase  
- **Status**: Indicates the result (`Pass`, `Fail`, or `Blocked`)  
- **Comments**: Provides additional insights or defect references if applicable

---

### 🛠 Execution Notes

- Manual test execution was performed on Google Chrome
- Any failed tests were followed by defect logging (see Bug Reports)
- Screenshots were captured for failed scenarios (stored in `/screenshots` folder if automation is used)

---

> 📎 Continue to the next section: [Bug Reporting](#) or [Selenium Automation](#)


## ✅ 6. Bug Reporting

📁 **Document Location**: `4_Bug_Reports/`

All defects discovered during manual or automated testing are documented here using a consistent, professional format. Each bug report includes critical details for developers and stakeholders to investigate and resolve issues effectively.

---

### 🪲 Example Bug Report

**File**: `BugReport_#101_LoginError.docx`

| Field             | Details                                                     |
|------------------|-------------------------------------------------------------|
| **Bug ID**        | 101                                                         |
| **Module**        | Login                                                       |
| **Severity**      | High                                                        |
| **Priority**      | High                                                        |
| **Description**   | Login fails with valid credentials on Firefox              |
| **Steps to Reproduce** | 1. Go to login page<br>2. Enter valid credentials<br>3. Click login |
| **Expected Result** | Redirect to inventory page                                |
| **Actual Result**   | Page reloads with no action                              |
| **Status**         | Open                                                       |
| **Reported By**    | Tushar                                                     |
| **Date**           | 10-July-2025                                               |

---

### 📄 Bug Report Template

**File**: `BugReport_Template.docx`  
Use this file as a reusable format to report all future bugs consistently.

---

### 🧭 Guidelines for Reporting

- Keep titles short but descriptive  
- Reproduce the issue at least twice before reporting  
- Always include browser/environment details  
- Use screenshots or video (if applicable) to support critical bugs  

---

> 📎 Next Section: [Automation Framework Setup](#)


## ✅ 7. Requirement Traceability Matrix (RTM)

📁 **Document Location**: `6_Traceability_Matrix/RTM_SauceDemo.xlsx`

The Requirement Traceability Matrix (RTM) ensures full coverage of all project requirements by mapping them to corresponding test scenarios and test cases.

---

### 📌 Sample RTM Format

| Requirement ID | Scenario ID | Test Case ID | Status |
|----------------|-------------|--------------|--------|
| **REQ001**     | TS001       | TC001        | Pass   |
| **REQ002**     | TS002       | TC002        | Fail   |

---

### 🎯 Purpose of RTM

- Ensure **every requirement is tested**
- Track **coverage and gaps**
- Provide **traceability** from business needs to validation
- Help stakeholders ensure all requirements are fulfilled

---

### 🧾 Column Description

- **Requirement ID**: Unique identifier of the business requirement  
- **Scenario ID**: Scenario designed to validate the requirement  
- **Test Case ID**: Test case(s) created for each scenario  
- **Status**: Test result status (`Pass`, `Fail`, `Blocked`, etc.)

---

> 📎 Next Section: [Automation Framework Setup](#)

## ✅ 8. Final Summary Report

The Final Summary Report provides a high-level overview of the entire testing cycle for the SauceDemo website, covering manual execution, automation, bugs found, and project outcomes.

---

## 📊 Test Result Summary

| Metric               | Details                                       |
|----------------------|-----------------------------------------------|
| ✅ Total Test Cases   | 20                                            |
| ✔️ Passed             | 18                                            |
| ❌ Failed             | 2                                             |
| 🪲 Bugs Reported      | 3                                             |
| 🚫 Blockers           | None                                          |
| 🛠 Tools Used         | MS Excel, MS Word, Browser DevTools          |
| 📄 Report Date        | 10-July-2025                                  |

---



---

## ✅ Manual Testing Includes:
- Requirement analysis of core modules: Login, Cart, Checkout, etc.
- Test Plan with objectives, scope, schedule, deliverables.
- Test Scenarios and detailed Test Cases in Excel format.
- Bug Reports with severity, priority, steps to reproduce.
- Test Execution Reports documenting pass/fail results.
- RTM (Requirement Traceability Matrix) for mapping test coverage.

---

## 🤖 Automation Testing Includes:
- Python-based Selenium scripts for:
  - Login automation
  - Cart operations
  - Checkout and logout validation
- Folder: `Automation Testing Selenium/`
- Tools used: Selenium, ChromeDriver, Python, PyTest

---

## 🧰 Tools Used
- Microsoft Excel / Word – for Test Plans, Cases, Reports  
- Browser DevTools – for manual testing  
- Selenium + Python – for automation  
- GitHub – version control and collaboration

---

## 👨‍💻 Author
**Tushar Maurya**  
Manual & Automation QA Engineer  
📅 Project Completed: July 2025









