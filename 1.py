#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A travel company wants to fly a plane to the Bahamas. Flying the plane costs 5000 dollars. So far, 29 people have signed up for the trip .if the company charges 200 dollars per ticket, what is the profit made by the company? Create variables for each numeric quantity and use appropriate arithmetic operations.


# In[1]:


cost_of_flying_plane=5000
print("Total amount required to fly a plan in air is",cost_of_flying_plane)
number_of_passengers=29
print("{} numbers of passengers signed".format(number_of_passengers))
price_of_ticket=200
print("cost of a ticket is ",price_of_ticket)
total_amount_of_passengers=number_of_passengers*price_of_ticket
print("total amount given by passengers is",total_amount_of_passengers)
profit=total_amount_of_passengers-cost_of_flying_plane
print("The company makes of a profit of {} dollars".format(profit))

