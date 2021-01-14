#!/usr/bin/env python
# coding: utf-8

# # Analyzing CIA Factbook Data Using SQL

# ### Install/Import the necessary programs/packages 

# In[3]:


pip install ipython-sql


# In[ ]:


import sqlalchemy
sqlalchemy.create_engine('sqlite:///factbook.db')
get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite:///factbook.db')


# For help with installing sql for use in Jupyter: https://towardsdatascience.com/heres-how-to-run-sql-in-jupyter-notebooks-f26eb90f3259

# **Import the table from the sql database.**

# In[5]:


get_ipython().run_cell_magic('sql', '', "SELECT * \nFROM sqlite_master\nWHERE type='table'")


# In[6]:


get_ipython().run_cell_magic('sql', '', 'SELECT * \nFROM facts\nLIMIT 5')


# **Column Descriptions:**
# 
# name — the name of the country.
# 
# area— the country's total area (both land and water).
# 
# area_land — the country's land area in square kilometers.
# 
# area_water — the country's waterarea in square kilometers.
# 
# population — the country's population.
# 
# population_growth— the country's population growth as a percentage.
# 
# birth_rate — the country's birth rate, or the number of births per 
# 
# year per 1,000 people.
# 
# death_rate — the country's death rate, or the number of death per 
# year per 1,000 people.

# In[7]:


get_ipython().run_cell_magic('sql', '', 'SELECT MIN(population), MAX(population), \n        MIN(population_growth), MAX(population_growth)\nFROM facts')


# In[8]:


get_ipython().run_cell_magic('sql', '', 'SELECT Name, MIN(population)\nFROM facts')


# In[9]:


get_ipython().run_cell_magic('sql', '', 'SELECT Name, MAX(population)\nFROM facts')


# In[10]:


get_ipython().run_cell_magic('sql', '', "SELECT MIN(population), MAX(population),\n        MIN(population_growth), MAX(population_growth)\nFROM facts\nWHERE name != 'World'")


# In[11]:


get_ipython().run_cell_magic('sql', '', 'SELECT AVG(population), AVG(Area)\nFROM facts')


# In[12]:


get_ipython().run_cell_magic('sql', '', "SELECT name, population\nFROM facts\nWHERE population > (SELECT AVG(population)\n                   FROM facts)\nAND name != 'World'")


# In[13]:


get_ipython().run_cell_magic('sql', '', 'SELECT name, area\nFROM facts\nWHERE area < (SELECT AVG(area)\n             FROM facts)')


# Country with the most people

# In[14]:


get_ipython().run_cell_magic('sql', '', "SELECT name, MAX(population)\nFROM facts\nWHERE name != 'World'")


# Country with the highest growth rate

# In[ ]:


get_ipython().run_cell_magic('sql', '', "SELECT name, MAX(population_growth)\nFROM facts\nWHERE name != 'World'")


# Countries with the highest ratios of water to land

# In[16]:


get_ipython().run_cell_magic('sql', '', 'SELECT name, CAST(area_land AS FLOAT)/area_water AS water_land_ratio\nFROM facts\nORDER BY water_land_ratio DESC\nLIMIT 5')


# Countries with more water than land

# In[17]:


get_ipython().run_cell_magic('sql', '', 'SELECT name, area_land, area_water\nFROM facts\nWHERE area_water > area_land')


# Countries that will add more people to their populations next year

# In[18]:


get_ipython().run_cell_magic('sql', '', 'SELECT name, population_growth\nFROM facts\nWHERE population_growth > 1')


# Countries with a higher death rate than birth rate

# In[19]:


get_ipython().run_cell_magic('sql', '', 'SELECT name, death_rate, birth_rate\nFROM facts\nWHERE death_rate > birth_rate')


# Countries with the highest population/area ratio

# In[20]:


get_ipython().run_cell_magic('sql', '', 'SELECT * \nFROM facts')


# In[ ]:




