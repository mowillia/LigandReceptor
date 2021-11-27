import numpy as np
import matplotlib.pyplot as plt

# color to rgb map
rgb_map = {'salmon':[255,126,121],
           'cantaloupe':[255,212,121],
           'aqua':[0,150,255],
           'magnesium':[192,192,192],
           'banana':[255,252,121],
           'moss':[0,144,81],
           'mocha':[148,82,0],
           'light-blue':[216,243,255],
          'white':[255,255,255]}

# coordinates of colors for the image
color_coods = {'salmon':[[4,3],
               [5,2],[5,3],[5,4],
               [6,1],[6,2],[6,3],[6,4],[6,5]],
              'cantaloupe':[[7,1],[7,2],[7,3],[7,4],[7,5],
               [8,1],[8,2],[8,4],[8,5]],
              'aqua':[[9,0],[9,1],[9,2],[9,3],[9,4],[9,5],[9,6],[9,7],[9,8],[9,9]],
               'magnesium': [[0,0],[0,1],[0,2],[1,0],[1,1]],
              'banana':[[0,7],[0,8],[0,9],[1,8],[1,9],[2,7],[2,9]],
              'moss':[[4,7],[4,8],[4,9],[5,7],[5,8],[5,9]],
              'mocha':[[6,8],[7,8],[8,8]]}

# conversion functions
def matrix_to_list(matrix):
    
    """
    Converts matrix to a list
    """
    
    return list(matrix.flatten())

def list_to_matrix(list_,shape_x = 10,shape_y=10):
    
    """
    Converts list to a matrix
    """    
    
    return np.array(list_, dtype = object).reshape(shape_x, shape_y)

def color_to_rgb(matrix):
    
    """
    Converts the informal name of a color to its rgb representation
    """    
    
    shape_x,shape_y = matrix.shape
    
    new_matrix = np.zeros(shape = (10,10,3), dtype = np.int)
    for k in range(shape_x):
        for j in range(shape_y):
            new_matrix[k,j] = rgb_map[matrix[k,j]]
            
    return new_matrix

def compute_master_list():
    
    """
    Creates a list representing the objective
    image for the grid
    """       
    
    # defining matrix with elements as color strings
    data_color_matrix = np.empty(shape = (10,10), dtype = object)

    # background
    for k in range(10):
        for j in range(10):
            data_color_matrix[k,j] = 'light-blue'

    # image of house trees and cloud
    for k in range(10):
        for j in range(10):
            for key, value in color_coods.items():
                if [k,j] in value:
                    data_color_matrix[k,j] = key 

    # matrix to list                
    list_ = matrix_to_list(data_color_matrix)       

    return list_

def imshow_list(list_, title = None):
    
    """
    Displays the grid display given a list
    representing the microstate
    """        
    
    # showing image data
    plt.imshow(color_to_rgb(list_to_matrix(list_)))

    ax = plt.gca();
    ax.set_xticks([])
    ax.set_yticks([])

    # Minor ticks
    ax.set_xticks(np.arange(0.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(0.5, 10, 1), minor=True)

    # Gridlines based on minor ticks
    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
    
    if title:
        ax.set_title(title, fontsize = 18, y = -.15)

    # plt.axis('off')
    plt.box(on=None)
    plt.show()
