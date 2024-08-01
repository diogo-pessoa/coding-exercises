import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize global variables
churros = 20
chaves_mangos = [1]  # Use a list for mutability
venda_funds = chaves_mangos

# Figure setup
fig, ax = plt.subplots()
line_churros, = ax.plot([], [], 'b-', label='Churros')
line_chaves, = ax.plot([], [], 'g-', label='Chaves $ Mangos')
line_venda, = ax.plot([], [], 'r-', label='Venda de Churros $ Cashier')

ax.set_xlim(0, churros)
ax.set_ylim(0, churros)
ax.set_xlabel('Churros')
ax.legend()  # Show labels

line_churros.set_data([0, churros], [churros, churros])
line_venda.set_data([0, 0], [0, 0])
line_chaves.set_data([0, 1], [1, 1])


def sell_churros(frame):
    global churros
    churros -= 1
    chaves_mangos[0] -= 1
    venda_funds[0] += 1

    # Update the plot
    line_churros.set_data([0, churros], [churros, churros])
    print(20 -churros, chaves_mangos[0], venda_funds[0])
    # line_chaves.set_data([chaves_mangos[0], 20 - churros], [chaves_mangos[0], chaves_mangos[0]])
    line_venda.set_data([venda_funds[0], 20 - churros], [venda_funds[0], venda_funds[0]])

    return line_churros, line_chaves, line_venda


def buy_churros(frame):
    global churros
    churros -= 1
    chaves_mangos[0] -= 1
    venda_funds[0] += 1

    # Update the plot
    line_churros.set_data([0, churros], [churros, churros])
    print(20 -churros, chaves_mangos[0], venda_funds[0])
    # line_chaves.set_data([chaves_mangos[0], 20 - churros], [chaves_mangos[0], chaves_mangos[0]])
    line_venda.set_data([venda_funds[0], 20 - churros], [venda_funds[0], venda_funds[0]])

    return line_churros, line_chaves, line_venda


ani_churros = FuncAnimation(fig, sell_churros, frames=range(churros), interval=800, blit=True, repeat=True)

plt.show()
