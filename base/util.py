from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np

def euler(f, x0, t):
    X = [x0]
    for k in range(1, len(t)):
        nX = X[k-1] + (t[k] - t[k-1]) * f(X[k-1], t[k-1])
        X.append(nX)
    return np.array(X)


def plot(x, y, xlabel=None, ylabel=None, title=None, figsize=None):
    plt.figure(figsize=figsize)
    plt.plot(x, y)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.title(title, fontsize=14)
    plt.grid(':')
    plt.show()


def plot_state_evolution(X, t, ylabels=None, xlabel=None, title=None, figsize=None, same_scale=False):
    # NOTA questa è una funzione di disegno più complessa!
    # Il codice è basato su quello di: https://matplotlib.org/3.5.0/gallery/spines/multiple_yaxis_with_spines.html
    fig = plt.figure(figsize=figsize)
    
    # Definisco le etichette per gli assi y
    if ylabels is None:
        ylabels = [None for i in range(X.shape[1])]
        
    # Preparo la mappa dei colori
    cmap = cm.get_cmap('Set2')
    
    # Preparo l'offset per gli assi addizionali
    offset = 1
    
    # Build the host axis
    host = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
    
    # Disegno le altre componenti
    for i in range(1, X.shape[1]):
        if not same_scale:
            # pass
            # ax = ParasiteAxes(host, sharex=host)
            # host.parasites.append(ax)
            ax = host.get_aux_axes(viewlim_mode=None, sharex=host)

            h = ax.plot(t, X[:, i], color=cmap(i))

            ax.axis[f'right{i}'] = ax.new_fixed_axis(loc="right", offset=(60 * (i-1), 0))
            ax.axis[f'right{i}'].set_visible(True)
            ax.axis[f'right{i}'].major_ticklabels.set_visible(True)
            ax.axis[f'right{i}'].label.set_visible(True)

            #ax.spines.right.set_position(("axes", 1 + offset * (i-1)))
            ax.set_ylabel(ylabels[i], fontsize=14)
            ax.yaxis.label.set_color(cmap(i))
        else:
            host.plot(t, X[:, i], color=cmap(i), label=ylabels[i])

    # Disegno la componente principale
    host.plot(t, X[:, 0], color=cmap(0), label=ylabels[0])
    host.set_xlabel(xlabel, fontsize=14)

    if not same_scale:
        host.set_ylabel(ylabels[0], fontsize=14)
        host.yaxis.label.set_color(cmap(0))

    if same_scale:
        plt.legend()
        
    plt.title(title, fontsize=14)
    plt.grid(':')
    plt.show()
