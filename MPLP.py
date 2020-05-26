import matplotlib.pyplot as plt

#########################################################

def MPL_Prefs(fig,ax,title_obj,grid):
    """
    matplotlib prefences for 2d and 3d guis
    """  
    
    if "3D" in str(type(ax)):
        #if 3d do this stuff also (zaxis operations)
        leg = ax.legend(loc=(1.05,0.25), facecolor='none', prop={'size': 10}, handlelength=0.5)
        fig.subplots_adjust(left=0, right=0.5, bottom=0, top=1)

        ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))

        ax.xaxis.label.set_color(       'lime')
        ax.yaxis.label.set_color(       'lime')
        ax.zaxis.label.set_color(       'lime')

        ax.tick_params(axis='z', colors='lime')

        
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
        leg = ax.legend(loc=(1.05,0.5), facecolor='none', prop={'size': 10}, handlelength=0.5)
        fig.subplots_adjust(left=0.1, right=0.75, bottom=0.1, top=0.95)
        
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

def legend_labeller(func_string_raw):
    to_be_split = ''+func_string_raw+''
    to_be_split = to_be_split.replace(' ','')
    long_legend_label = to_be_split.split('#')[0]
    try:
        lims_legend_label = '\nLimits:\n'+to_be_split.split('#')[1]
    except:
        pass
   # for i in range(0,int(len(long_legend_label.split('#'))/2)):
   #     split_legend_label0.append(long_legend_label.split('#')[i+1])

   # long_legend_label = ''.join(split_legend_label0)
    splitter_char = 14
    split_legend_label = []
    [split_legend_label.append(long_legend_label[i:i+splitter_char]) for i in range(0,len(long_legend_label),splitter_char)]
    
    try:
        legend_label = '$'+"$...\n   $".join(split_legend_label)+'$'+lims_legend_label
    except:
        legend_label = '$'+"$...\n   $".join(split_legend_label)+'$'
    return legend_label