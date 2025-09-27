# selenium-python

### Step 1: **Clone the project**

Open Terminal:

```bash
git clone git@github.com:Ehasn-testlab/selenium-python.git
```

---

### Step 2: **Create and Activate a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: **Install Selenium and WebDriver Manager**

```bash
pip install selenium webdriver-manager
```

### Step 4: **Install pytest and pytest html**

```bash
pip install pytest
pip install pytest-html
pip install pytest-dependency
pip install pytest-order

```


### Step 5: **Run the Script**

In Terminal: To run a specific file

```bash
pytest <file_name> --html=reports/report.html --self-contained-html

```

In Terminal: To run a all testcases

```bash
pytest --html=reports/report.html --self-contained-html

```