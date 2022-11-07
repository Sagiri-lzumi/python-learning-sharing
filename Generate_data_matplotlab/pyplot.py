import matplotlib.pyplot as plt
fig , ax = plt.subplots()
array = []
for i in range(50):
    num = i*i
    array.append(num)
    i = i+1


ax.plot(array)
plt.show()