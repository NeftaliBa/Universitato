# Ejemplo de scaterplot
from matplotlib import pyplot as plt
# The relationship between the number of frinds your users have and the number of minutes they spend on the site every day

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f ', 'g', 'h', 'i']
plt.scatter(friends, minutes)
for label, friends_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label, xy= (friends_count, minute_count), xytext=(5, -5), textcoords='offset points')
plt.title("Daily minute vs Number of friends")
plt.xlabel("Num. of friends")
plt.ylabel("Daily Minutes")
plt.show()