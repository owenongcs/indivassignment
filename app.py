#!/usr/bin/env python
# coding: utf-8

# In[29]:


from flask import Flask


# In[30]:


app = Flask(__name__)


# In[31]:


from flask import request, render_template 
import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        print(income, age, loan)
        
        model = joblib.load("model")
        pred = model.predict([[float(income), float(age), float(loan)]])
        if (pred > 0.5):
            result = "Yes"
        else: 
            result = "No"
        s = "Is Customer Defaulting? " + result
        return (render_template("index.html", result = s))
    else: 
        return (render_template("index.html", result = "2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




