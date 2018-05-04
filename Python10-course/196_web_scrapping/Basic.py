
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[6]:


r=requests.get("https://pythonhow.com/example.html")
c=r.content


# In[25]:


soup=BeautifulSoup(c, "html.parser")
all=soup.find_all("div",{'class':'cities'})


# In[27]:


for item in all:
    print(item.find_all("p")[0].text)

