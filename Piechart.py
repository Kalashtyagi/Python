#A program to show careful girls with percentage
import matplotlib.pyplot as plt
Partition = 'Kalash','kanika','Neha', 'Komal'
sizes = [200,150,250,200]
figl,axl = plt.subplots()
axl.pie(sizes,labels = Partition, autopct = '%1.1f%%',shadow = True,
startangle=90)
axl.axis('equal')
plt.show()