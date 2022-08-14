'''this fuction generates 4 * 10**9 random numbers in a new file using less than 4GB memory space.'''
import random
lst = []
for i in range(1, 201):
      lst.append(i)
count = 0
my_dict = {'1': count}
for ind in range(4 * 10**6):
      num = random.choice(lst)
      for n in my_dict:
              if n == f'{num}':
                  my_dict[f'{num}'] += 1
                  break
      else:
              count = 1
              my_dict[f'{num}'] = count
new_file = open('rand_num', 'w')
for key, number in my_dict.items():
     key1 = new_file.write(f"number`{key} ")
     key1 = new_file.write(f"count`{number}: ")
