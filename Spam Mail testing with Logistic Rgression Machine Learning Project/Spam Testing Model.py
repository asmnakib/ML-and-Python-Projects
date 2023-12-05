#!/usr/bin/env python
# coding: utf-8

# # Importing Dependecy

# In[38]:


import numpy as np


# In[39]:


import pandas as pd


# In[40]:


from sklearn.model_selection import train_test_split


# In[41]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[42]:


from sklearn.linear_model import LogisticRegression


# In[43]:


from sklearn.metrics import accuracy_score


# # Data Collection & Pre-processing

# In[44]:


#loading data from csv file to a pandas dataframe
raw_mail_data = pd.read_csv("mail_data.csv")
raw_mail_data.head()


# In[45]:


# replce the null values with a null string
mail_data =raw_mail_data.where((pd.notnull(raw_mail_data)),'')


# In[46]:


# printing the firdt 5 rows of the data frame
mail_data.head()


# In[47]:


# checking the number of rows ND COLUMNS IN THE DATAFRAME
mail_data.shape


# # Label Encoding 

# In[48]:


# label spam mail as 0; ham mail as 1;

mail_data.loc[mail_data['Category'] == 'spam','Category',] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category',] = 1


# spam  -  0
# ham   -  1

# In[49]:


mail_data.head()


# In[50]:


# Sepaerating the data as texts and label
  
x = mail_data['Message']        

y= mail_data['Category']      


# In[51]:


x.head()


# In[52]:


print(y)


# In[53]:


x_train, x_test,y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 4)


# In[54]:


print(x.shape)
print(x_train.shape)
print(x_test.shape)


# In[55]:


# transform the text data to feature vectors that can be used as input to the Logistic Regrression

feature_extraction = TfidfVectorizer(min_df=1, stop_words='english',lowercase='True')

x_train_features = feature_extraction.fit_transform(x_train)

# only wiil feed the training data nbut no need to fit in your test

x_test_features = feature_extraction.transform(x_test)

#converting  y_train and y_test values as integers

Y_train = y_train.astype('int')
y_test = y_test.astype('int')


# 
# # Training Model

# Logistic Regression

# In[56]:


model = LogisticRegression()


# In[57]:


# training logistic regression model with training data

model.fit(x_train_features, Y_train)


# Evaluating the trained model

# In[58]:


prediction_on_training_data = model.predict(x_train_features)


# In[59]:


accuracy_on_training_data =accuracy_score(Y_train,prediction_on_training_data)


# In[60]:


print(accuracy_on_training_data)


# In[61]:


prediction_on_testing_data = model.predict(x_test_features)
accuracy_on_testing_data =accuracy_score(y_test,prediction_on_testing_data)
print(accuracy_on_testing_data)


# Building a predictive system 

# input_mail = input("Input mail for prediction:")

# list=[]
# x = int(input("How many mail you need to be checked"))
# for r in range(0,x):
#     mail = input("Enter mail:     ")
#     list.append(mail)

# In[84]:


input_mail = ["Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030"]


# In[85]:


# convert text to feature vectors
input_mail_features =feature_extraction.transform(input_mail)


# In[86]:


# making predictions

prediction = model.predict(input_mail_features)


# In[87]:


if prediction[0] ==1:
    print(" This is a ham mail.")
else:
    print("This is a spam")

