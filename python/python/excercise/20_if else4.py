''''' write a program to decide which is cheaper approach to go from ahmedabad to delhi. by car or by train. consider person has his own petrol car  and he prefer to travel by 1st class train 
'''
car_km=float(input("enter distance for car travel in km =="))
train_km=float(input("enter distance for train travel in km =="))
car_cost_per_km=float(input("enter cost per km for car travel =="))
train_cost_per_km=float(input("enter cost per km for train travel =="))

total_car_cost=car_km*car_cost_per_km
total_train_cost=train_km*train_cost_per_km

if total_car_cost<total_train_cost:
     print("travel by car is better than train",total_car_cost)
else:
     print("travel by train is better than car",total_train_cost)
     
print("thank you for using our services")
print("have a nice day")
     