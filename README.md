# playwright-python

# 🎭 Playwright Python Automation Framework  

Welcome to the **Playwright Python Automation Framework**! 
This repository contains a **comprehensive automation framework** using **Playwright and Python**, covering everything from **UI and API testing to network interception and CI/CD integration**. 🚀  

## 📌 Key Features  

✅ **End-to-end UI automation** with Playwright  
✅ **API testing and network interception**  
✅ **Pytest framework for structured test execution**  
✅ **Visual testing and mobile device emulation**  
✅ **Integration with CI/CD and Docker**  
✅ **Industry-standard test framework with BDD support**  

---

## 📚 Project Structure  

```
playwright-python/
│── tests/                     # Test cases using Playwright & Pytest
│── pages/                     # Page Object Model (POM) structure
│── config/                    # Configuration files
│── reports/                   # Test reports & logs
│── requirements.txt           # Project dependencies
│── pytest.ini                 # Pytest configuration
│── README.md                  # Project documentation
```

---

## 🛠 Installation & Setup  

### 1️⃣ **Clone the repository**  
```sh
git clone https://github.com/shobhitha/playwright-python.git
cd playwright-python
```

### 2️⃣ **Create a virtual environment (Optional but recommended)**  
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ **Install dependencies**  
```sh
pip install -r requirements.txt
```

### 4️⃣ **Install Playwright browsers**  
```sh
playwright install
```

---

## 🚀 Running Tests  

### 🔹 Run all tests  
```sh
pytest
```

### 🔹 Run tests with detailed logging  
```sh
pytest -v
```

### 🔹 Run specific test file  
```sh
pytest tests/test_example.py
```

### 🔹 Generate test report  
```sh
pytest --html=reports/test_report.html --self-contained-html
```

---

## 🎯 Who Can Use This Framework?  

- **Software Testers & QA Engineers**  
- **Automation Testers & SDETs**  
- **Python Developers**  
- **Anyone interested in Playwright automation**  

---

## 🛠 Contributing  

Want to contribute? Follow these steps:  
1. **Fork this repository**  
2. **Create a new feature branch** (`git checkout -b feature-branch`)  
3. **Commit your changes** (`git commit -m "Add new feature"`)  
4. **Push to the branch** (`git push origin feature-branch`)  
5. **Create a Pull Request**  

---


### **How to Use This README?**  
1. Copy this content and paste it into a new **README.md** file in your repository (`playwright-python`).  
2. Commit the changes and push to GitHub.  

Let me know if you want additional sections like **badges**, **GitHub Actions for CI/CD**, or **example test cases**! 🚀

This projects automates the testing of order processing of a retail web application using playwright automation framework, python, pytest. 
