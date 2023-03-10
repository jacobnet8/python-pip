import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["A", "B", "C"]
    values = [200, 32, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig("pie.png") #Esto es para generar una imagen y que el programa no se detenda
    plt.close()
