
# coding: utf-8

# # Background
# Sample code and markdown file
# - Simple Hello World program
# - Simple Fibonacci sequence program
# 

# In[1]:

#Hello world
print 'Hello world!'


# In[4]:

#Fibonacci
y = input("Enter end number for Fibonacci sequence: ")

fibonacci = 0
trail = 1

while fibonacci < y:
    print(fibonacci)
    fibonacci = fibonacci + trail
    trail = fibonacci - trail

