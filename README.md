# Enhanced Counter App - Automated UI Testing

## Overview
This repository contains an automated UI test suite for an Enhanced Counter Android application using Appium and Python's unittest framework. The test suite covers various functionalities of the counter app, including initial value verification, incrementing, resetting, and date selection.

## Prerequisites

### Software Requirements
- Python 3.8+
- Appium Server
- Android SDK
- UiAutomator2 Driver
- Android Device or Emulator

### Required Python Packages
- `appium-python-client`
- `selenium`
- `unittest`

## Test Cases

The test suite includes the following test cases:

1. **Initial Value Test** (`test_initial_value`)
   - Verifies that the counter starts at 0 when the app launches

2. **Increment Test** (`test_increment`)
   - Tests the functionality of incrementing the counter

3. **Reset Test** (`test_reset`)
   - Checks if the reset button works correctly

4. **Date Selection Test** (`test_select_date`)
   - Validates the date picker functionality

5. **Date Display Test** (`test_select_date_display`)
   - Tests selecting and confirming a specific date

6. **Date Selection Cancel Test** (`test_select_date_display_cancel`)
   - Verifies the cancel functionality in date picker

7. **Invalid Action Test** (`test_invalid_action`)
   - Handles potential edge cases or unexpected user interactions

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://your-repository-url.git
cd enhanced-counter-app-tests
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Appium
- Install Appium Server
- Ensure Android device/emulator is connected
- Update device capabilities in the test script if needed

### 4. Run Tests
```bash
python -m unittest CounterApp.py
```

## Test Report
The test suite generates a comprehensive test report after execution, displaying:
- Test Case Name
- Result (PASS/FAIL)
- Error Message (if applicable)

## Screenshot Capture
In case of test failures, screenshots are automatically captured in the `screenshots/` directory for debugging purposes.

## Device Configuration
- **Platform**: Android
- **Automation**: UiAutomator2
- **App Package**: `com.example.testapp`
- **App Activity**: `com.example.testapp.MainActivity`

## Error Handling
The test suite includes robust error handling with:
- WebDriverWait for element visibility
- Screenshot capture on test failure
- Detailed error logging


