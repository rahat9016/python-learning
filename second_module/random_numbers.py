import random

for i in range(10, 20):
    print(random.random())

for i in range(1, 10):
    print(random.randint(10, 80))

# random name select for leader
    
list_of_leader_name = ['Rahat', 'Minhajur', 'Rohoman', 'Python', 'JavaScript', 'TypeScript']

find_leader = random.choice(list_of_leader_name)
print(find_leader)
