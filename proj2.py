'''this project sorts numbers in file.'''
file = open('rand_num', 'r')
file = file.read()
num_count = file.split(': ')
numbers = []
for num in num_count:
    ind1 = num.find('`')
    ind2 = num.find(' ')
    numbers.append(num[ind1 + 1:ind2])
for i in range(len(numbers)):
      for j in range(len(numbers) - 1 - i):
            if int(numbers[j]) > int(numbers[j + 1]):
                  numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                  num_count[j], num_count[j + 1] = num_count[j + 1], num_count[j]
new = open('sorted_rand_nums', 'w')
for num in num_count:
      w = new.write(num)
      w = new.write(': ')
