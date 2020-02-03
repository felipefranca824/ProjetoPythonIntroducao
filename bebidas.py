import pandas as pd
import matplotlib.pyplot as plt

arquivo = pd.read_csv('a8_d_Bebida.csv')

eixo_x = arquivo['Time']
eixo_y = arquivo['Bebida']
plt.xticks(rotation=90)
plt.xlabel('Time')
plt.ylabel('Bebida')
plt.grid()
plt.title('Todos os valores')

plt.plot(eixo_x, eixo_y)

plt.show()


plt.xlabel('Time')
plt.ylabel('Bebida')
plt.grid()
plt.title('Boxplot')

plt.boxplot(eixo_y)

plt.show()



eixo_x_primeiros = eixo_x[:10]
eixo_y_primeiros = eixo_y[:10]
plt.xlabel('Time')
plt.ylabel('Bebida')
plt.xticks(rotation=90)
plt.grid()
plt.title('10 primeiros valores')
plt.plot(eixo_x_primeiros, eixo_y_primeiros)

plt.show()

eixo_x_ultimos = eixo_x[177:]
eixo_y_ultimos = eixo_y[177:]
plt.xlabel('Time')
plt.ylabel('Bebida')
plt.xticks(rotation=90)
plt.grid()
plt.title('10 ultimos valores')
plt.plot(eixo_x_ultimos, eixo_y_ultimos)

plt.show()

eixo_x_primeiros_30 = eixo_x[:10]
eixo_y_primeiros_30 = eixo_y[:10]
plt.xlabel('Time')
plt.ylabel('Bebida')
plt.xticks(rotation=90)
plt.grid()
plt.title('30 primeiros valores')
plt.plot(eixo_x_primeiros, eixo_y_primeiros)

plt.show()

