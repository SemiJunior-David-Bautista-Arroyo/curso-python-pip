import matplotlib.pyplot as plt

def generate_pie_chart():
    #se asignan los valores 
    labels = ['A','B','C']
    values = [200,34,120]

    fig,ax = plt.subplots() #se obtiene la figura y coordenadas desde matplot
    ax.pie(values, labels = labels)# se envían los valores y luego los labels
    plt.savefig('pie.png') #se guarda la grafica como el archivo pie.png
    plt.close()#se cierra 
