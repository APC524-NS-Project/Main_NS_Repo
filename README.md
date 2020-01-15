# Main_PDE_Repo

[![Build Status](https://travis-ci.com/APC524-PDE-Project/Main_PDE_Repo.svg?branch=master)](https://travis-ci.com/APC524-PDE-Project/Main_PDE_Repo)

An Object-Oriented Framework for Solving Parabolic PDEs via Finite Difference Methods

The manual can be built simply using the command: ```doxygen Doxyfile``` from the project root directory. This generates html and latex output. The html can be viewed by opening the file html/index.html in a web browser. To run the example script, simply run the main.py file in the project root directory. This will create a gif of the time evolution of the system in the outputs folder.

This software uses Finite Difference methods to solve PDEs which may be solved by the method of lines. Particular finite difference schemes can be implemented modularly to solve the PDE with no user manipulation of the governing equations. The code can allow for user implementation of a particular finite difference scheme to solve a given PDE but which still requires proper interface construction for the user to access these methods. Currently the parameters can be changed within initializer.py, and the boundary conditions can be changed in main.py. Future work will implement a more user-friendly interface which allows specification of parameters at runtime. Currently the only implemented PDE problem is the 2D heat equation in conduct_heat_eqn.py, but the code could easily be extended by creating additional linear operators and problem types.
