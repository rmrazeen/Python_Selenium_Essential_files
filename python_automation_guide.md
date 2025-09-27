# Python for Automation - Complete Guide

## Table of Contents
1. [Python Basics](#1-python-basics)
2. [Control Structures](#2-control-structures)
3. [Functions](#3-functions)
4. [Data Structures](#4-data-structures)
5. [String Manipulation](#5-string-manipulation)
6. [File Handling](#6-file-handling)
7. [Exception Handling](#7-exception-handling)
8. [Modules and Packages](#8-modules-and-packages)
9. [Object-Oriented Programming (OOP)](#9-object-oriented-programming-oop)
10. [HTML and XPath/CSS Selectors](#10-html-and-xpathcss-selectors)

---

## 1. Python Basics

### 1.1 Variables and Data Types

Python is dynamically typed, meaning you don't need to declare variable types explicitly.

```python
# Basic data types
name = "John Doe"           # String
age = 30                    # Integer
height = 5.9               # Float
is_employed = True         # Boolean
salary = None              # NoneType

# Type checking
print(type(name))          # <class 'str'>
print(isinstance(age, int)) # True

# Type conversion
age_str = str(age)         # "30"
price = float("99.99")     # 99.99
```

### 1.2 Operators

```python
# Arithmetic operators
a, b = 10, 3
print(a + b)    # 13 (Addition)
print(a - b)    # 7  (Subtraction)
print(a * b)    # 30 (Multiplication)
print(a / b)    # 3.33... (Division)
print(a // b)   # 3  (Floor division)
print(a % b)    # 1  (Modulus)
print(a ** b)   # 1000 (Exponentiation)

# Comparison operators
print(a > b)    # True
print(a == b)   # False
print(a != b)   # True

# Logical operators
x, y = True, False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Assignment operators
count = 0
count += 1      # count = count + 1
count *= 2      # count = count * 2
```

### 1.3 Input/Output

```python
# Input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Output formatting
print(f"Hello {name}, you are {age} years old")
print("Hello {}, you are {} years old".format(name, age))
print("Hello %s, you are %d years old" % (name, age))

# Print with different separators and endings
print("apple", "banana", "orange", sep=", ")
print("Loading", end="...")
print("Done!")
```

**Automation Example:**
```python
# Automated report generation
import datetime

def generate_report_header():
    current_time = datetime.datetime.now()
    report_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    header = f"""
    =================================
    AUTOMATION REPORT
    Generated on: {report_date}
    =================================
    """
    return header

print(generate_report_header())
```

---

## 2. Control Structures

### 2.1 Conditional Statements

```python
# Basic if-else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")

# Nested conditions
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Need license")
else:
    print("Too young to drive")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"
```

### 2.2 Loops

#### For Loops
```python
# Iterate over range
for i in range(5):          # 0, 1, 2, 3, 4
    print(f"Iteration {i}")

for i in range(2, 10, 2):   # 2, 4, 6, 8
    print(f"Even number: {i}")

# Iterate over collections
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Enumerate for index and value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Dictionary iteration
person = {"name": "John", "age": 30, "city": "NYC"}
for key, value in person.items():
    print(f"{key}: {value}")
```

#### While Loops
```python
# Basic while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop with condition
user_input = ""
while user_input.lower() != "quit":
    user_input = input("Enter command (or 'quit' to exit): ")
    if user_input.lower() != "quit":
        print(f"You entered: {user_input}")
```

#### Loop Control
```python
# Break and continue
for i in range(10):
    if i == 3:
        continue    # Skip iteration when i=3
    if i == 7:
        break      # Exit loop when i=7
    print(i)

# Else clause with loops
for i in range(5):
    print(i)
else:
    print("Loop completed normally")  # Executes if no break
```

**Automation Example:**
```python
# Automated file processing
import os
import time

def process_files_in_directory(directory_path):
    """Process all .txt files in a directory"""
    
    if not os.path.exists(directory_path):
        print(f"Directory {directory_path} does not exist")
        return
    
    files_processed = 0
    
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory_path, filename)
            
            try:
                with open(filepath, 'r') as file:
                    content = file.read()
                    word_count = len(content.split())
                    
                print(f"Processed {filename}: {word_count} words")
                files_processed += 1
                
                # Add delay to avoid overwhelming system
                time.sleep(0.1)
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                continue
    
    print(f"\nTotal files processed: {files_processed}")

# Usage
process_files_in_directory("/path/to/documents")
```

---

## 3. Functions

### 3.1 Basic Functions

```python
# Basic function definition
def greet(name):
    """This function greets a person"""
    return f"Hello, {name}!"

# Function call
message = greet("Alice")
print(message)

# Function with multiple parameters
def calculate_area(length, width):
    """Calculate rectangle area"""
    area = length * width
    return area

result = calculate_area(10, 5)
print(f"Area: {result}")
```

### 3.2 Advanced Function Concepts

```python
# Default parameters
def create_profile(name, age=25, city="Unknown"):
    return {
        "name": name,
        "age": age,
        "city": city
    }

profile1 = create_profile("John")
profile2 = create_profile("Jane", 30, "NYC")

# Keyword arguments
def send_email(to, subject, body, cc=None, bcc=None):
    print(f"Sending email to: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    if cc:
        print(f"CC: {cc}")

send_email(subject="Meeting", to="john@email.com", body="Let's meet at 3 PM")

# Variable arguments (*args, **kwargs)
def calculate_sum(*numbers):
    """Calculate sum of any number of arguments"""
    return sum(numbers)

def create_user(**user_info):
    """Create user with any number of keyword arguments"""
    return user_info

total = calculate_sum(1, 2, 3, 4, 5)
user = create_user(name="John", age=30, email="john@email.com")
```

### 3.3 Lambda Functions

```python
# Lambda functions (anonymous functions)
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(multiply(3, 4))  # 12

# Lambda in higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Squared: {squared}")
print(f"Even numbers: {even_numbers}")
```

### 3.4 Decorators

```python
# Simple decorator
def timing_decorator(func):
    """Decorator to measure function execution time"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Function completed"

result = slow_function()
```

**Automation Example:**
```python
# Automated data validation functions
import re
from datetime import datetime

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number format"""
    pattern = r'^\+?1?[-.\s]?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}$'
    return re.match(pattern, phone) is not None

def validate_date(date_string, date_format="%Y-%m-%d"):
    """Validate date format"""
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

def batch_validate_data(data_list):
    """Validate a batch of user data"""
    results = []
    
    for record in data_list:
        validation_result = {
            'record': record,
            'email_valid': validate_email(record.get('email', '')),
            'phone_valid': validate_phone(record.get('phone', '')),
            'date_valid': validate_date(record.get('birth_date', ''))
        }
        results.append(validation_result)
    
    return results

# Usage example
sample_data = [
    {'email': 'john@example.com', 'phone': '123-456-7890', 'birth_date': '1990-05-15'},
    {'email': 'invalid-email', 'phone': '123', 'birth_date': '1990-13-40'}
]

validation_results = batch_validate_data(sample_data)
for result in validation_results:
    print(result)
```

---

## 4. Data Structures

### 4.1 Lists

```python
# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]

# List operations
fruits.append("grape")              # Add to end
fruits.insert(1, "kiwi")           # Insert at index
fruits.remove("banana")            # Remove by value
popped = fruits.pop()              # Remove and return last item

# List slicing
print(numbers[1:4])                # [2, 3, 4]
print(numbers[:3])                 # [1, 2, 3]
print(numbers[2:])                 # [3, 4, 5]
print(numbers[-2:])                # [4, 5]

# List comprehensions
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])                # 6
```

### 4.2 Tuples

```python
# Creating tuples
coordinates = (10, 20)
person = ("John", 30, "Engineer")

# Tuple unpacking
x, y = coordinates
name, age, job = person

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)
```

### 4.3 Dictionaries

```python
# Creating dictionaries
student = {
    "name": "Alice",
    "age": 22,
    "grades": [85, 90, 78]
}

# Dictionary operations
student["email"] = "alice@email.com"    # Add key-value pair
age = student.get("age", 0)             # Get with default
del student["age"]                      # Delete key

# Dictionary methods
keys = student.keys()
values = student.values()
items = student.items()

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}

# Nested dictionaries
company = {
    "employees": {
        "001": {"name": "John", "department": "IT"},
        "002": {"name": "Jane", "department": "HR"}
    }
}
```

### 4.4 Sets

```python
# Creating sets
unique_numbers = {1, 2, 3, 4, 5}
colors = set(["red", "blue", "green", "red"])  # Duplicates removed

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2              # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2       # {3, 4}
difference = set1 - set2         # {1, 2}
symmetric_diff = set1 ^ set2     # {1, 2, 5, 6}

# Set methods
set1.add(7)
set1.remove(1)
set1.discard(10)  # Won't raise error if element doesn't exist
```

**Automation Example:**
```python
# Automated data processing with different data structures
import json
from collections import defaultdict, Counter

class DataProcessor:
    def __init__(self):
        self.data_cache = {}  # Dictionary for caching
        self.processed_items = set()  # Set for tracking processed items
        self.error_log = []  # List for error logging
        self.stats = defaultdict(int)  # Default dict for statistics
    
    def process_user_data(self, users_data):
        """Process user data and generate analytics"""
        
        for user_id, user_info in users_data.items():
            if user_id in self.processed_items:
                continue  # Skip already processed users
            
            try:
                # Extract user information
                age = user_info.get('age', 0)
                department = user_info.get('department', 'Unknown')
                
                # Update statistics
                self.stats['total_users'] += 1
                self.stats[f'department_{department}'] += 1
                
                if age >= 18:
                    self.stats['adults'] += 1
                
                # Cache processed data
                self.data_cache[user_id] = {
                    'processed_at': datetime.now(),
                    'age_group': 'adult' if age >= 18 else 'minor'
                }
                
                self.processed_items.add(user_id)
                
            except Exception as e:
                self.error_log.append({
                    'user_id': user_id,
                    'error': str(e),
                    'timestamp': datetime.now()
                })
    
    def get_department_summary(self):
        """Generate department-wise summary"""
        dept_stats = {k: v for k, v in self.stats.items() if k.startswith('department_')}
        return dict(dept_stats)
    
    def export_results(self, filename):
        """Export processing results to JSON"""
        results = {
            'statistics': dict(self.stats),
            'cache_size': len(self.data_cache),
            'errors': len(self.error_log),
            'processed_users': len(self.processed_items)
        }
        
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2, default=str)

# Usage
processor = DataProcessor()
sample_users = {
    'user001': {'age': 25, 'department': 'Engineering'},
    'user002': {'age': 17, 'department': 'Intern'},
    'user003': {'age': 30, 'department': 'Marketing'}
}

processor.process_user_data(sample_users)
print(processor.get_department_summary())
processor.export_results('processing_results.json')
```

---

## 5. String Manipulation

### 5.1 Basic String Operations

```python
# String creation and basic operations
text = "Hello, World!"
name = "Alice"

# String concatenation
greeting = "Hello, " + name + "!"
greeting = f"Hello, {name}!"  # f-strings (Python 3.6+)
greeting = "Hello, {}!".format(name)

# String methods
print(text.upper())        # "HELLO, WORLD!"
print(text.lower())        # "hello, world!"
print(text.title())        # "Hello, World!"
print(text.capitalize())   # "Hello, world!"

# String information
print(len(text))           # 13
print(text.count('l'))     # 3
print(text.startswith('Hello'))  # True
print(text.endswith('!'))  # True
```

### 5.2 String Searching and Replacement

```python
text = "The quick brown fox jumps over the lazy dog"

# Finding substrings
position = text.find('fox')        # Returns index or -1
position = text.index('fox')       # Returns index or raises error
contains = 'fox' in text           # Boolean check

# String replacement
new_text = text.replace('fox', 'cat')
new_text = text.replace('the', 'THE', 1)  # Replace only first occurrence

# String splitting and joining
words = text.split()               # Split by whitespace
words = text.split('the')          # Split by specific delimiter
sentence = ' '.join(words)         # Join list with separator
```

### 5.3 String Formatting

```python
name = "Alice"
age = 30
salary = 50000.50

# f-strings (recommended for Python 3.6+)
message = f"Name: {name}, Age: {age}, Salary: ${salary:,.2f}"

# format() method
message = "Name: {}, Age: {}, Salary: ${:,.2f}".format(name, age, salary)
message = "Name: {n}, Age: {a}, Salary: ${s:,.2f}".format(n=name, a=age, s=salary)

# % formatting (older style)
message = "Name: %s, Age: %d, Salary: $%.2f" % (name, age, salary)

# Advanced formatting
print(f"{salary:>10.2f}")     # Right align, width 10, 2 decimals
print(f"{name:^20}")          # Center align, width 20
print(f"{age:04d}")           # Zero pad to 4 digits
```

### 5.4 Regular Expressions

```python
import re

text = "Contact us at support@example.com or sales@company.org"

# Basic pattern matching
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(pattern, text)
print(emails)  # ['support@example.com', 'sales@company.org']

# Pattern compilation for reuse
email_pattern = re.compile(pattern)
matches = email_pattern.findall(text)

# Pattern substitution
cleaned_text = re.sub(r'\d+', '[NUMBER]', "Call 123-456-7890 or 987-654-3210")

# Pattern groups
phone_pattern = r'(\d{3})-(\d{3})-(\d{4})'
match = re.search(phone_pattern, "Call me at 123-456-7890")
if match:
    area_code = match.group(1)
    exchange = match.group(2)
    number = match.group(3)
```

**Automation Example:**
```python
# Automated text processing for data extraction
import re
from datetime import datetime

class TextProcessor:
    def __init__(self):
        # Compiled regex patterns for better performance
        self.email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        self.phone_pattern = re.compile(r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})')
        self.date_pattern = re.compile(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b')
        self.url_pattern = re.compile(r'https?://[^\s]+')
    
    def extract_contact_info(self, text):
        """Extract all contact information from text"""
        return {
            'emails': self.email_pattern.findall(text),
            'phones': self.phone_pattern.findall(text),
            'dates': self.date_pattern.findall(text),
            'urls': self.url_pattern.findall(text)
        }
    
    def clean_and_standardize(self, text):
        """Clean and standardize text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Standardize phone numbers
        text = re.sub(r'(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})', r'(\1) \2-\3', text)
        
        # Convert to title case for names
        words = text.split()
        cleaned_words = []
        
        for word in words:
            # Keep emails and URLs as-is
            if '@' in word or 'http' in word:
                cleaned_words.append(word)
            else:
                cleaned_words.append(word.title())
        
        return ' '.join(cleaned_words)
    
    def generate_report(self, text_data):
        """Generate a processing report"""
        report = {
            'processed_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'original_length': len(text_data),
            'word_count': len(text_data.split()),
            'contact_info': self.extract_contact_info(text_data)
        }
        
        # Calculate statistics
        contact_info = report['contact_info']
        report['statistics'] = {
            'email_count': len(contact_info['emails']),
            'phone_count': len(contact_info['phones']),
            'date_count': len(contact_info['dates']),
            'url_count': len(contact_info['urls'])
        }
        
        return report

# Usage example
processor = TextProcessor()
sample_text = """
Please contact John Doe at john.doe@company.com or call (555) 123-4567.
Meeting scheduled for 12/25/2023. Visit our website: https://example.com
Alternative contact: jane.smith@email.org, phone: 555.987.6543
"""

contact_info = processor.extract_contact_info(sample_text)
cleaned_text = processor.clean_and_standardize(sample_text)
report = processor.generate_report(sample_text)

print("Contact Info:", contact_info)
print("Cleaned Text:", cleaned_text)
print("Report:", report)
```

---

## 6. File Handling

### 6.1 Basic File Operations

```python
# Reading files
with open('example.txt', 'r') as file:
    content = file.read()           # Read entire file
    
with open('example.txt', 'r') as file:
    lines = file.readlines()        # Read all lines as list
    
with open('example.txt', 'r') as file:
    for line in file:               # Read line by line (memory efficient)
        print(line.strip())

# Writing files
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    
with open('output.txt', 'a') as file:  # Append mode
    file.write("Appended text\n")

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('output.txt', 'w') as file:
    file.writelines(lines)
```

### 6.2 File System Operations

```python
import os
import shutil
from pathlib import Path

# Working with paths
current_dir = os.getcwd()
file_path = os.path.join(current_dir, 'data', 'file.txt')

# Using pathlib (modern approach)
path = Path('data/file.txt')
parent_dir = path.parent
filename = path.name
extension = path.suffix

# File and directory operations
os.makedirs('new_directory', exist_ok=True)
os.rename('old_name.txt', 'new_name.txt')
os.remove('file_to_delete.txt')
shutil.copy('source.txt', 'destination.txt')
shutil.move('file.txt', 'new_location/')

# Directory listing
for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        print(filename)

# File information
import stat
file_stats = os.stat('example.txt')
print(f"Size: {file_stats.st_size} bytes")
print(f"Modified: {file_stats.st_mtime}")
```

### 6.3 Working with Different File Formats

```python
import json
import csv

# JSON files
data = {"name": "John", "age": 30, "city": "NYC"}

# Write JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)

# Read JSON
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

# CSV files
# Write CSV
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['John', 30, 'NYC'])
    writer.writerow(['Jane', 25, 'LA'])

# Read CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# CSV with DictReader
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}")
```

**Automation Example:**
```python
# Automated file processing system
import os
import json
import csv
import shutil
from datetime import datetime
from pathlib import Path

class FileProcessor:
    def __init__(self, input_dir, output_dir, log_dir):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.log_dir = Path(log_dir)
        
        # Create directories if they don't exist
        for directory in [self.input_dir, self.output_dir, self.log_dir]:
            directory.mkdir(parents=True, exist_ok=True)
        
        self.processing_log = []
    
    def process_text_files(self):
        """Process all .txt files in input directory"""
        for file_path in self.input_dir.glob('*.txt'):
            try:
                # Read and process file
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Process content (example: word count, line count)
                word_count = len(content.split())
                line_count = len(content.splitlines())
                
                # Create processed filename
                processed_filename = f"processed_{file_path.name}"
                output_path = self.output_dir / processed_filename
                
                # Write processed file with metadata
                processed_content = f"""
PROCESSING METADATA:
Original file: {file_path.name}
Processed on: {datetime.now()}
Word count: {word_count}
Line count: {line_count}

ORIGINAL CONTENT:
{content}
"""
                
                with open(output_path, 'w', encoding='utf-8') as file:
                    file.write(processed_content)
                
                # Log successful processing
                self.processing_log.append({
                    'file': file_path.name,
                    'status': 'success',
                    'word_count': word_count,
                    'line_count': line_count,
                    'processed_at': datetime.now().isoformat()
                })
                
                # Move original file to archive
                archive_dir = self.input_dir / 'archived'
                archive_dir.mkdir(exist_ok=True)
                shutil.move(str(file_path), str(archive_dir / file_path.name))
                
            except Exception as e:
                self.processing_log.append({
                    'file': file_path.name,
                    'status': 'error',
                    'error': str(e),
                    'processed_at': datetime.now().isoformat()
                })
    
    def generate_csv_report(self):
        """Generate CSV report of processed files"""
        report_path = self.log_dir / f"processing_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        with open(report_path, 'w', newline='', encoding='utf-8') as file:
            if self.processing_log:
                writer = csv.DictWriter(file, fieldnames=self.processing_log[0].keys())
                writer.writeheader()
                writer.writerows(self.processing_log)
    
    def generate_json_summary(self):
        """Generate JSON summary of processing"""
        successful_files = [log for log in self.processing_log if log['status'] == 'success']
        error_files = [log for log in self.processing_log if log['status'] == 'error']
        
        summary = {
            'processing_date': datetime.now().isoformat(),
            'total_files': len(self.processing_log),
            'successful': len(successful_files),
            'errors': len(error_files),
            'success_rate': len(successful_files) / len(self.processing_log) * 100 if self.processing_log else 0,
            'total_words_processed': sum(log.get('word_count', 0) for log in successful_files),
            'error_details': error_files
        }
        
        summary_path = self.log_dir / f"processing_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(summary_path, 'w', encoding='utf-8') as file:
            json.dump(summary, file, indent=2)
        
        return summary

# Usage example
processor = FileProcessor('input_files', 'processed_files', 'logs')
processor.process_text_files()
processor.generate_csv_report()
summary = processor.generate_json_summary()
print("Processing Summary:", summary)
```

---

## 7. Exception Handling

### 7.1 Basic Exception Handling

```python
# Basic try-except
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions in one block
try:
    # Some risky operation
    pass
except (ValueError, TypeError, KeyError) as e:
    print(f"An error occurred: {e}")

# Catch all exceptions (use sparingly)
try:
    # Some operation
    pass
except Exception as e:
    print(f"Unexpected error: {e}")
```

### 7.2 Advanced Exception Handling

```python
# Complete exception handling structure
try:
    file = open('data.txt', 'r')
    data = file.read()
    result = len(data) / 0  # This will cause an error
except FileNotFoundError:
    print("File not found!")
except ZeroDivisionError:
    print("Division by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No exceptions occurred")  # Runs only if no exceptions
finally:
    print("This always runs")  # Cleanup code
    if 'file' in locals():
        file.close()

# Using context managers (recommended for files)
try:
    with open('data.txt', 'r') as file:
        data = file.read()
        # File automatically closes even if error occurs
except FileNotFoundError:
    print("File not found!")
```

### 7.3 Custom Exceptions

```python
# Creating custom exceptions
class ValidationError(Exception):
    """Custom exception for validation errors"""
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

class InsufficientFundsError(Exception):
    """Custom exception for banking operations"""
    pass

# Using custom exceptions
def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("Age must be an integer", "INVALID_TYPE")
    if age < 0:
        raise ValidationError("Age cannot be negative", "INVALID_VALUE")
    if age > 150:
        raise ValidationError("Age seems unrealistic", "UNREALISTIC_VALUE")

def withdraw_money(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw ${amount}, balance is ${balance}")
    return balance - amount

# Using the custom exceptions
try:
    validate_age(-5)
except ValidationError as e:
    print(f"Validation failed: {e} (Code: {e.error_code})")

try:
    new_balance = withdraw_money(100, 150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
```

### 7.4 Exception Logging

```python
import logging
import traceback

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('error.log'),
        logging.StreamHandler()
    ]
)

def risky_operation(data):
    try:
        # Some complex operation
        result = data['value'] * 2
        return result
    except KeyError as e:
        logging.error(f"Missing key in data: {e}")
        raise
    except TypeError as e:
        logging.error(f"Type error in calculation: {e}")
        logging.error(f"Full traceback: {traceback.format_exc()}")
        raise
    except Exception as e:
        logging.critical(f"Unexpected error: {e}")
        logging.critical(f"Full traceback: {traceback.format_exc()}")
        raise
```

**Automation Example:**
```python
# Robust automation script with comprehensive error handling
import logging
import traceback
from datetime import datetime
from pathlib import Path
import json

class AutomationError(Exception):
    """Base exception for automation errors"""
    pass

class DataProcessingError(AutomationError):
    """Exception for data processing errors"""
    pass

class FileOperationError(AutomationError):
    """Exception for file operation errors"""
    pass

class RobustAutomationSystem:
    def __init__(self, config_file):
        # Configure logging
        self.setup_logging()
        
        try:
            self.load_configuration(config_file)
        except Exception as e:
            self.logger.critical(f"Failed to initialize system: {e}")
            raise AutomationError(f"System initialization failed: {e}")
    
    def setup_logging(self):
        """Set up comprehensive logging"""
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        
        # Create logs directory
        Path('logs').mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            handlers=[
                logging.FileHandler(f'logs/automation_{datetime.now().strftime("%Y%m%d")}.log'),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger(__name__)
    
    def load_configuration(self, config_file):
        """Load system configuration with error handling"""
        try:
            with open(config_file, 'r') as file:
                self.config = json.load(file)
            self.logger.info(f"Configuration loaded successfully from {config_file}")
        except FileNotFoundError:
            self.logger.error(f"Configuration file {config_file} not found")
            raise FileOperationError(f"Configuration file {config_file} not found")
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in configuration file: {e}")
            raise DataProcessingError(f"Invalid configuration format: {e}")
    
    def process_data_batch(self, data_list):
        """Process a batch of data with individual error handling"""
        results = {
            'successful': [],
            'failed': [],
            'summary': {
                'total': len(data_list),
                'success_count': 0,
                'error_count': 0
            }
        }
        
        for i, data_item in enumerate(data_list):
            try:
                processed_item = self.process_single_item(data_item)
                results['successful'].append({
                    'index': i,
                    'original': data_item,
                    'processed': processed_item
                })
                results['summary']['success_count'] += 1
                
            except DataProcessingError as e:
                self.logger.warning(f"Data processing error for item {i}: {e}")
                results['failed'].append({
                    'index': i,
                    'data': data_item,
                    'error': str(e),
                    'error_type': 'DataProcessingError'
                })
                results['summary']['error_count'] += 1
                
            except Exception as e:
                self.logger.error(f"Unexpected error processing item {i}: {e}")
                self.logger.error(f"Traceback: {traceback.format_exc()}")
                results['failed'].append({
                    'index': i,
                    'data': data_item,
                    'error': str(e),
                    'error_type': 'UnexpectedError'
                })
                results['summary']['error_count'] += 1
        
        # Log summary
        success_rate = (results['summary']['success_count'] / results['summary']['total']) * 100
        self.logger.info(f"Batch processing completed: {success_rate:.1f}% success rate")
        
        return results
    
    def process_single_item(self, item):
        """Process a single data item with validation"""
        try:
            # Validate input
            if not isinstance(item, dict):
                raise DataProcessingError(f"Expected dictionary, got {type(item)}")
            
            required_fields = ['id', 'value']
            for field in required_fields:
                if field not in item:
                    raise DataProcessingError(f"Missing required field: {field}")
            
            # Process the item
            processed = {
                'id': item['id'],
                'original_value': item['value'],
                'processed_value': item['value'] * 2,  # Example processing
                'processed_at': datetime.now().isoformat()
            }
            
            return processed
            
        except KeyError as e:
            raise DataProcessingError(f"Missing key: {e}")
        except (TypeError, ValueError) as e:
            raise DataProcessingError(f"Invalid data type or value: {e}")
    
    def safe_file_operation(self, operation, *args, **kwargs):
        """Wrapper for safe file operations"""
        try:
            return operation(*args, **kwargs)
        except PermissionError as e:
            self.logger.error(f"Permission denied: {e}")
            raise FileOperationError(f"Permission denied: {e}")
        except FileNotFoundError as e:
            self.logger.error(f"File not found: {e}")
            raise FileOperationError(f"File not found: {e}")
        except IOError as e:
            self.logger.error(f"IO error: {e}")
            raise FileOperationError(f"IO error: {e}")

# Usage example with error handling
def main():
    try:
        # Initialize system
        system = RobustAutomationSystem('config.json')
        
        # Sample data for processing
        sample_data = [
            {'id': 1, 'value': 10},
            {'id': 2, 'value': 20},
            {'id': 3},  # Missing 'value' field - will cause error
            {'id': 4, 'value': 'invalid'},  # Invalid value type
            {'id': 5, 'value': 50}
        ]
        
        # Process data with error handling
        results = system.process_data_batch(sample_data)
        
        # Save results
        with open('processing_results.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        print("Processing completed successfully!")
        print(f"Success rate: {results['summary']['success_count']}/{results['summary']['total']}")
        
    except AutomationError as e:
        print(f"Automation system error: {e}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
```

---

## 8. Modules and Packages

### 8.1 Importing Modules

```python
# Different ways to import
import math
import datetime as dt
from os import path, getcwd
from collections import defaultdict, Counter
from json import load, dump

# Import everything (use sparingly)
from math import *

# Using imported modules
print(math.pi)
current_time = dt.datetime.now()
current_dir = getcwd()
```

### 8.2 Creating Custom Modules

**math_utilities.py:**
```python
"""
Custom math utilities module
"""

def calculate_area(shape, **kwargs):
    """Calculate area of different shapes"""
    if shape == 'rectangle':
        return kwargs['length'] * kwargs['width']
    elif shape == 'circle':
        import math
        return math.pi * kwargs['radius'] ** 2
    elif shape == 'triangle':
        return 0.5 * kwargs['base'] * kwargs['height']
    else:
        raise ValueError(f"Unknown shape: {shape}")

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

# Module constants
PI = 3.14159265359
E = 2.71828182846

# Module initialization code
if __name__ == "__main__":
    # This runs only when module is executed directly
    print("Testing math_utilities module...")
    print(f"Rectangle area: {calculate_area('rectangle', length=5, width=3)}")
    print(f"Fibonacci(10): {fibonacci(10)}")
```

**Using the custom module:**
```python
import math_utilities
from math_utilities import fibonacci, PI

# Use module functions
area = math_utilities.calculate_area('circle', radius=5)
fib_sequence = fibonacci(10)
print(f"Pi constant: {PI}")
```

### 8.3 Creating Packages

**Package structure:**
```
automation_tools/
    __init__.py
    file_handler/
        __init__.py
        processor.py
        validator.py
    data_analyzer/
        __init__.py
        statistics.py
        reporter.py
    utils/
        __init__.py
        helpers.py
```

**automation_tools/__init__.py:**
```python
"""
Automation Tools Package
"""

__version__ = "1.0.0"
__author__ = "Your Name"

# Import main classes/functions for easy access
from .file_handler.processor import FileProcessor
from .data_analyzer.statistics import DataAnalyzer
from .utils.helpers import log_operation

# Package-level constants
DEFAULT_ENCODING = 'utf-8'
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
```

**automation_tools/file_handler/processor.py:**
```python
"""
File processing utilities
"""

import os
from pathlib import Path
from ..utils.helpers import log_operation

class FileProcessor:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
    
    @log_operation
    def process_files(self, pattern="*.txt"):
        """Process files matching pattern"""
        files_processed = []
        for file_path in self.base_path.glob(pattern):
            # Process file logic here
            files_processed.append(str(file_path))
        return files_processed
```

**automation_tools/utils/helpers.py:**
```python
"""
Utility helper functions
"""

import functools
from datetime import datetime

def log_operation(func):
    """Decorator to log function operations"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[{datetime.now()}] Completed {func.__name__}")
        return result
    return wrapper

def validate_file_size(file_path, max_size_mb=10):
    """Validate file size"""
    from pathlib import Path
    file_size = Path(file_path).stat().st_size
    max_size_bytes = max_size_mb * 1024 * 1024
    return file_size <= max_size_bytes
```

**Using the package:**
```python
# Import from package
from automation_tools import FileProcessor, DataAnalyzer
from automation_tools.utils.helpers import validate_file_size

# Use package components
processor = FileProcessor('/data/files')
files = processor.process_files('*.csv')
```

### 8.4 Standard Library Modules

```python
# Common standard library modules for automation

# Operating system interface
import os
import sys
import shutil
from pathlib import Path

# Date and time
import datetime
import time

# Data handling
import json
import csv
import sqlite3

# Internet and networking
import urllib.request
import http.client
import smtplib

# Regular expressions
import re

# Logging
import logging

# Threading and multiprocessing
import threading
import multiprocessing

# Configuration
import configparser

# Command line arguments
import argparse
```

**Automation Example:**
```python
# Complete automation package example
"""
automation_suite/__init__.py
"""

import logging
from datetime import datetime
from pathlib import Path

class AutomationSuite:
    def __init__(self, config_path=None):
        self.setup_logging()
        self.config = self.load_config(config_path) if config_path else {}
        self.logger = logging.getLogger(__name__)
    
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('automation.log'),
                logging.StreamHandler()
            ]
        )
    
    def load_config(self, config_path):
        """Load configuration from JSON file"""
        import json
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Failed to load config: {e}")
            return {}

# Create a complete automation module
"""
automation_suite/file_automation.py
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import json

class FileAutomation:
    def __init__(self, base_directory):
        self.base_directory = Path(base_directory)
        self.processed_files = []
        self.errors = []
    
    def organize_by_extension(self):
        """Organize files by their extensions"""
        for file_path in self.base_directory.iterdir():
            if file_path.is_file():
                try:
                    extension = file_path.suffix.lower()
                    if extension:
                        # Create directory for extension
                        ext_dir = self.base_directory / extension[1:]  # Remove the dot
                        ext_dir.mkdir(exist_ok=True)
                        
                        # Move file
                        new_path = ext_dir / file_path.name
                        shutil.move(str(file_path), str(new_path))
                        
                        self.processed_files.append({
                            'original': str(file_path),
                            'new': str(new_path),
                            'timestamp': datetime.now().isoformat()
                        })
                        
                except Exception as e:
                    self.errors.append({
                        'file': str(file_path),
                        'error': str(e),
                        'timestamp': datetime.now().isoformat()
                    })
    
    def generate_report(self):
        """Generate processing report"""
        report = {
            'processing_date': datetime.now().isoformat(),
            'files_processed': len(self.processed_files),
            'errors_encountered': len(self.errors),
            'details': {
                'processed_files': self.processed_files,
                'errors': self.errors
            }
        }
        
        report_path = self.base_directory / 'organization_report.json'
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        return report

# Usage
if __name__ == "__main__":
    from automation_suite import AutomationSuite
    from automation_suite.file_automation import FileAutomation
    
    # Initialize automation suite
    suite = AutomationSuite('config.json')
    
    # Run file organization
    file_automator = FileAutomation('/path/to/messy/directory')
    file_automator.organize_by_extension()
    report = file_automator.generate_report()
    
    print("File organization completed!")
    print(f"Files processed: {report['files_processed']}")
    print(f"Errors: {report['errors_encountered']}")
```

---

## 9. Object-Oriented Programming (OOP)

### 9.1 Classes and Objects

```python
# Basic class definition
class Car:
    # Class attribute (shared by all instances)
    wheels = 4
    
    def __init__(self, make, model, year):
        # Instance attributes (unique to each object)
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.engine_running = False
    
    # Instance methods
    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            return f"{self.make} {self.model} engine started!"
        return "Engine is already running."
    
    def drive(self, miles):
        if self.engine_running:
            self.odometer += miles
            return f"Drove {miles} miles. Total: {self.odometer}"
        return "Start the engine first!"
    
    def stop_engine(self):
        self.engine_running = False
        return "Engine stopped."
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    def __repr__(self):
        return f"Car('{self.make}', '{self.model}', {self.year})"

# Creating objects
my_car = Car("Toyota", "Camry", 2022)
print(my_car)  # Uses __str__ method
print(repr(my_car))  # Uses __repr__ method

# Using methods
print(my_car.start_engine())
print(my_car.drive(50))
print(my_car.stop_engine())
```

### 9.2 Inheritance

```python
# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def drive(self, miles):
        self.odometer += miles
        return f"Drove {miles} miles"
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

# Derived class
class Car(Vehicle):
    def __init__(self, make, model, year, doors=4):
        super().__init__(make, model, year)  # Call parent constructor
        self.doors = doors
        self.trunk_open = False
    
    def open_trunk(self):
        self.trunk_open = True
        return "Trunk opened"
    
    def get_info(self):  # Override parent method
        base_info = super().get_info()
        return f"{base_info} ({self.doors} doors)"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size
    
    def wheelie(self):
        return "Performing wheelie!"
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} ({self.engine_size}cc)"

# Using inheritance
car = Car("Honda", "Civic", 2023, doors=2)
bike = Motorcycle("Yamaha", "R1", 2023, engine_size=998)

print(car.get_info())    # "2023 Honda Civic (2 doors)"
print(bike.get_info())   # "2023 Yamaha R1 (998cc)"
print(bike.wheelie())    # "Performing wheelie!"
```

### 9.3 Encapsulation and Properties

```python
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self._balance = initial_balance  # Protected attribute
        self.__pin = None  # Private attribute
        self._transaction_history = []
    
    @property
    def balance(self):
        """Getter for balance"""
        return self._balance
    
    @balance.setter
    def balance(self, value):
        """Setter for balance with validation"""
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    
    @property
    def transaction_history(self):
        """Read-only property for transaction history"""
        return self._transaction_history.copy()
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount
        self._transaction_history.append({
            'type': 'deposit',
            'amount': amount,
            'timestamp': datetime.now(),
            'balance_after': self._balance
        })
        return f"Deposited ${amount}. New balance: ${self._balance}"
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount
        self._transaction_history.append({
            'type': 'withdrawal',
            'amount': amount,
            'timestamp': datetime.now(),
            'balance_after': self._balance
        })
        return f"Withdrew ${amount}. New balance: ${self._balance}"
    
    def set_pin(self, pin):
        """Set private PIN"""
        if len(str(pin)) != 4:
            raise ValueError("PIN must be 4 digits")
        self.__pin = pin
    
    def verify_pin(self, pin):
        """Verify private PIN"""
        return self.__pin == pin
    
    def __str__(self):
        return f"Account {self.account_number}: ${self._balance}"

# Using the class
account = BankAccount("12345", 1000)
print(account.balance)  # Uses property getter

account.deposit(500)
account.withdraw(200)

print(f"Transaction history: {len(account.transaction_history)} transactions")
```

### 9.4 Polymorphism and Abstract Classes

```python
from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        return f"This is a {self.__class__.__name__} with area {self.area()}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Polymorphism in action
def print_shape_info(shape):
    """This function works with any Shape subclass"""
    print(f"Shape: {shape.__class__.__name__}")
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print(f"Description: {shape.describe()}")
    print("-" * 30)

# Using polymorphism
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Rectangle(2, 8)
]

for shape in shapes:
    print_shape_info(shape)
```

**Automation Example:**
```python
# Advanced automation system using OOP principles
from abc import ABC, abstractmethod
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

class AutomationTask(ABC):
    """Abstract base class for all automation tasks"""
    
    def __init__(self, task_id: str, name: str):
        self.task_id = task_id
        self.name = name
        self.created_at = datetime.now()
        self.status = "pending"
        self.results = {}
        self.errors = []
    
    @abstractmethod
    def execute(self) -> bool:
        """Execute the task. Return True if successful."""
        pass
    
    @abstractmethod
    def validate_inputs(self) -> bool:
        """Validate task inputs. Return True if valid."""
        pass
    
    def get_summary(self) -> Dict[str, Any]:
        """Get task summary"""
        return {
            'task_id': self.task_id,
            'name': self.name,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'error_count': len(self.errors),
            'results': self.results
        }

class FileProcessingTask(AutomationTask):
    """Task for processing files"""
    
    def __init__(self, task_id: str, source_dir: str, pattern: str = "*.*"):
        super().__init__(task_id, f"File Processing: {source_dir}")
        self.source_dir = Path(source_dir)
        self.pattern = pattern
        self.processed_files = []
    
    def validate_inputs(self) -> bool:
        """Validate that source directory exists"""
        if not self.source_dir.exists():
            self.errors.append(f"Source directory does not exist: {self.source_dir}")
            return False
        return True
    
    def execute(self) -> bool:
        """Execute file processing"""
        try:
            if not self.validate_inputs():
                self.status = "failed"
                return False
            
            self.status = "running"
            
            for file_path in self.source_dir.glob(self.pattern):
                if file_path.is_file():
                    try:
                        self._process_single_file(file_path)
                        self.processed_files.append(str(file_path))
                    except Exception as e:
                        self.errors.append(f"Error processing {file_path}: {str(e)}")
            
            self.results = {
                'files_processed': len(self.processed_files),
                'files_list': self.processed_files
            }
            
            self.status = "completed" if not self.errors else "completed_with_errors"
            return len(self.errors) == 0
            
        except Exception as e:
            self.errors.append(f"Task execution failed: {str(e)}")
        