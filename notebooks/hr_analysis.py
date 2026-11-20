#!/usr/bin/env python
# coding: utf-8

# # HR Employee Data Analysis
# 
# ## Introduction
# 
# This notebook contains a basic analysis of employee data.
# 
# The data includes employee names, departments, salaries,
# cities and joining dates.
# 
# The aim is to understand the employee information using Python and Pandas.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Employee data

# In[4]:


employees = pd.read_csv("../data/employees.csv")

employees.head()


# Department data

# In[5]:


departments = pd.read_csv("../data/departments.csv")

departments.head()


# Dataset

# In[6]:


print("Employee data shape:", employees.shape)

print("Column names:")
print(employees.columns)

print("Data information:")
employees.info()


# In[7]:


employees.isnull().sum()


# In[8]:


average_salary = employees["salary"].mean()

print("Average employee salary:", average_salary)


# In[9]:


chennai_employees = employees[employees["city"] == "Chennai"]

print(chennai_employees)


# In[10]:


department_count = employees["department"].value_counts()

print(department_count)


# In[11]:


salary_array = np.array(employees["salary"])

print("Highest salary:", np.max(salary_array))

print("Lowest salary:", np.min(salary_array))

print("Average salary:", np.mean(salary_array))


# In[12]:


get_ipython().run_line_magic('timeit', 'employees["salary"].mean()')


# In[13]:


employees.groupby("department")["salary"].mean().plot(
    kind="bar",
    title="Average Salary by Department"
)

plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()


# ## Findings
# 
# 1. The dataset contains 10 employees.
# 2. There are three departments: IT, HR and Finance.
# 3. Five employees belong to Chennai.
# 4. The average salary is 37600.
# 5. IT has the highest average salary among the three departments.

# 
