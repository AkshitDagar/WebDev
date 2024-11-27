import matplotlib.pyplot as plt
a=[12,23,34,45,54,36,23,55]
b=[21,16,22,45,2,34,58,47]
plt.title("INDIA PAKISTAN MATCH ANALYSIS")
plt.xlabel("OVERS") 
plt.ylabel("RUNS")
plt.plot(a,color="blue", marker="*")
plt.plot(b,color="green",marker="*")
plt.show()