import matplotlib.pyplot as plt

#########################################################

def MPL_Prefs(fig,ax,title_obj,grid):
    """
    matplotlib prefences for 2d and 3d guis
    """  
    
    if "3D" in str(type(ax)):
        #if 3d do this stuff also (zaxis operations)
        ax.grid(color='green',linewdith=1, alpha=0.5)

        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

        ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))

        ax.xaxis.label.set_color(       'lime')
        ax.yaxis.label.set_color(       'lime')
        ax.zaxis.label.set_color(       'lime')

        ax.tick_params(axis='z', colors='lime')

        leg = ax.legend(loc='upper left', facecolor='none')
        ax.spines['bottom'].set_color(  'lime')
        ax.spines['top'].set_color(     'lime')

        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        ax.set_zlabel('$z$')

        ax.zaxis._axinfo["grid"]['color'] = "green" 
        ax.zaxis._axinfo["grid"]["linewidth"] = 0.5
        ax.yaxis._axinfo["grid"]['color'] = "green" 
        ax.yaxis._axinfo["grid"]["linewidth"] = 0.5
        ax.xaxis._axinfo["grid"]['color'] = "green"
        ax.xaxis._axinfo["grid"]["linewidth"] = 0.5

    if "3D" not in str(type(ax)):
        # if 2d do this stuff
        leg = ax.legend(loc=(0,1.04), facecolor='none')
        plt.grid(color='green', alpha=0.5)
        plt.xlabel('$x$',c='lime')
        plt.ylabel('$y$',c='lime')

    # if 2d or 3d do this stuff

    fig.set_facecolor('black')
    ax.set_facecolor('black')
    plt.setp(title_obj, color='white')
   # plt.rcParams['grid.color'] = "green"

    ax.tick_params(axis='x', colors='lime')
    ax.tick_params(axis='y', colors='lime') 

    for text in leg.get_texts():
        text.set_color('w')