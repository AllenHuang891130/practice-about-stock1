#!/usr/bin/env python
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt
import requests
import pandas as pd
import numpy as np
import csv
from io import StringIO
#先處理指數
bigdata = []
index = []
final = []
#日期一天一天跳 
datestr = '2021-01-04'
# 載股價
r = requests.post('https://www.twse.com.tw/exchangeReport/MI_5MINS_INDEX?response=csv&date=' + datestr.replace('-','') + '&type=ALL')
df = csv.reader(StringIO(r.text.replace("=", "")))
bigdata += df
# 顯示出來
#for i in range(1,3243):
    #print(bigdata[i][0],bigdata[i][1])   
for i in range(0,5):
    index.append(float(bigdata[720*i+2][1].replace(',','')))
print(index)
#index.append(bigdata[3242][0])


#再處理DI
di = []
url='https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466920&stname=%25E8%2587%25BA%25E5%258C%2597&datepicker='+datestr+'&altitude=5.3m#'
table=pd.read_html(url,encoding = 'utf-8')
we = pd.DataFrame(table[1][7:14])
for i in range(0,5):
    k = int(we.iloc[i]['temperature'])-0.55*(1-0.01*int(we.iloc[i]['RH']))*(int(we.iloc[i]['temperature'])-58)
    di.append(k)

#時間軸
time = []
time1 = []
for i in range(9,14):
    time.append(i)
for i in range(8,13):
    time1.append(i)
#畫圖
plt.subplot(2, 1, 1)
plt.plot(time1 ,di ,'g')
plt.subplot(2, 1, 2)
plt.plot(time ,index ,  "b")


# In[ ]:





# In[ ]:





# In[ ]:


#linear Regression
import numpy as np
from sklearn.linear_model import LinearRegression

temperatures = np.array([29, 28, 34, 31, 25, 29, 32, 31, 24, 33, 25, 31, 26, 30])
iced_tea_sales = np.array([77, 62, 93, 84, 59, 64, 80, 75, 58, 91, 51, 73, 65, 84])

# 轉換維度
temperatures = np.reshape(temperatures, (len(temperatures), 1))
iced_tea_sales = np.reshape(iced_tea_sales, (len(iced_tea_sales), 1))

lm = LinearRegression()
lm.fit(temperatures, iced_tea_sales)

# 模型績效
mse = np.mean((lm.predict(temperatures) - iced_tea_sales) ** 2)
r_squared = lm.score(temperatures, iced_tea_sales)

# 印出模型績效
print(mse)
print(r_squared)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import requests
res = requests.get('https://free-proxy-list.net/')
#res.text
import re
m = re.findall('\d+\.\d+\.\d+\.\d+:\d+', res.text)
validips = []
for ip in m:
    try:
        res = requests.get('https://api.ipify.org?format=json',proxies = {'http':ip, 'https':ip}, timeout = 5)
        validips.append({'ip':ip})
        
        print(res.json())
    except:
        print('FAIL', ip )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[6]:


import matplotlib.pyplot as plt
import requests
import pandas as pd
import numpy as np
import csv
from io import StringIO


#處理時間
import datetime
today=datetime.date.today()
today=today-datetime.timedelta(days=449)
for i in range(0,10):
    today=today+datetime.timedelta(days=1)
    datestr=str(today)
    #先處理指數
    bigdata = []
    index = []
    final = []
    # 載股價
    r = requests.post('https://www.twse.com.tw/exchangeReport/MI_5MINS_INDEX?response=csv&date=' + datestr.replace('-','') + '&type=ALL')
    #讀取資料
    df = csv.reader(StringIO(r.text.replace("=", "")))
    bigdata += df
    for i in range(0,5):    
        index.append(float(bigdata[720*i+2][1].replace(',','')))

    #再處理DI
    di = []
    url='https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466920&stname=%25E8%2587%25BA%25E5%258C%2597&datepicker='+datestr+'&altitude=5.3m#'
    table=pd.read_html(url,encoding = 'utf-8')
    we = pd.DataFrame(table[1][7:14])
    for i in range(0,5):
        k = int(we.iloc[i]['temperature'])-0.55*(1-0.01*int(we.iloc[i]['RH']))*(int(we.iloc[i]['temperature'])-58)
        di.append(k)

    #時間軸
    time = []
    time1 = []
    for i in range(9,14):
        time.append(i)
    for i in range(8,13):
        time1.append(i)

    #畫圖
    plt.subplot(2, 1, 1)
    plt.plot(time1 ,di ,'g')
    plt.subplot(2, 1, 2)
    plt.plot(time ,index ,  "b")

    bigdata.clear()
    index.clear()
    final.clear()
    di.clear()
    time.clear()
    time1.clear()


# In[ ]:





# In[ ]:





# In[ ]:




