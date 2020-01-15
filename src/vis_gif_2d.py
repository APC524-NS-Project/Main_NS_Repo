## \file vis_gif_2d.py
#file containing the VisGif2d class
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

import src.visualizer as visualizer

## Class for creating a gif movie of simulation results for 2d scalar variables
class VisGif2d(visualizer.Visualizer):
    ## The constructor. VisGif2d objects are instantiated with an output directory.
    # \param direc The directory in which to save the output
    def __init__(self,direc):
        self.direc = direc
        
    ## Generates a 2d movie of the output from logger and saves it as a GIF to the given output directory  
    # \param log The Logger object containing the data to be animated.
    def make_2d_movie(self,log, **kwargs):
        fext="2d_movie"
        suffix=".gif"
        framenums=log.get_nframes()
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_zlim(*log.get_data_limits())
        x,y=log.get_frame(0)[1].spec.coords #sets up coordinates for plot using GridSpec coordinate tuple
        xmesh,ymesh=np.meshgrid(x,y,indexing='ij')
        first_grid = log.get_frame(0)[1] 
        surf = [ax.plot_surface(xmesh,ymesh,first_grid.grid,**kwargs)]
        
        ani = animation.FuncAnimation(fig, self._animate,frames = framenums,fargs=(xmesh,ymesh,ax,surf,log))
    
        ani.save(self.direc+fext+suffix , writer='pillow')
        plt.close(fig='all')
        
    ## Method used to step forward a frame for the make_2d_movie method
    # \param i The frame to step to
    # \param X The dim number 0 meshgrid
    # \param Y The dim number 1 meshgrid
    # \param ax The matplotlib Axes object used to make the ovie
    # \param surf The matplotlib ax.plot_surface() instance to update       
    # \param log The Logger object containing the data to be plotted
    def _animate(self,i,X,Y,ax,surf,log):
        next_grid = log.get_frame(i)[1]
        surf[0].remove()
        surf[0] = ax.plot_surface(X, Y, next_grid.grid)
        return surf
