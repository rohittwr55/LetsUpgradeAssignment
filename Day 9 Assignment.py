#!/usr/bin/env python
# coding: utf-8

# # PyLint for a number is prime or not

# In[ ]:


get_ipython().run_cell_magic('writefile', 'number_prime_or_not.py', '\'\'\'This is a Prime Number\'\'\'\nN = int(input("Enter a number"))\nfor Y in range(2, N):\n    if N%Y == 0:\n        print("Not prime ")\n        break\nelse:\n    print("Is prime ")')


# In[7]:


get_ipython().system(' pylint "number_prime_or_not.py"')


# # Unit Test for a number is prime or not

# In[1]:


get_ipython().run_cell_magic('writefile', 'unit_Test_prime_or_not.py', '\'\'\'This is a Prime Number\'\'\'\ndef unitprime(N):\n    for Y in range(2, N):\n        if N%Y == 0:\n            return "Is Not Prime"\n            break\n    else:\n        return "Prime"')


# In[2]:


import unit_Test_prime_or_not
unit_Test_prime_or_not.unitprime(5)


# In[5]:


get_ipython().run_cell_magic('writefile', 'TestPrime.py', 'import unittest\nimport unit_Test_prime_or_not\n\nclass testPrime(unittest.TestCase):\n    def testNumber(self):\n        abc = 5\n        result = unit_Test_prime_or_not.unitprime(abc)\n        self.assertEqual(result,"Prime")\n    def testingAnother(self):\n        xyz = 10\n        result = unit_Test_prime_or_not.unitprime(xyz)\n        self.assertEqual(result,"Is Not Prime")\nif __name__ == "__main__":\n    unittest.main()')


# In[8]:


get_ipython().system(' python TestPrime.py')


# # Armstrong using Generator

# In[63]:


def arm(lst):
    
    for arms in lst:
        y=0
        temp=arms
        while temp>0:
            x=temp%10
            y=y+x**3
            temp=temp//10
        
        if y == arms:
            yield "Number",arms,"Is Armstrong"


# In[64]:


lst = list(range(1,1000))


# In[65]:


print(list(arm(lst)))


# In[ ]:




