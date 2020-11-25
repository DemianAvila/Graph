# Graph

## Constructor
Data structure "Graph" representes as a Adjacency matrix in python
Each instance of the class expects 3 parameters, first, the number of nodes (a positive integer), which in this case are called "vertex"

2nd expect a boolean, which indicates if the graph is directed or not (if indeed, it is directed, each time a edge is created, it only creates that connection from a vertex (row) to another (column) "A to B is not the same as B to A"); if is not directed, it creates a edge in both directions row/column and column/row "A to B is the same as B to A", and that creats a symetric matrix

3rd expects also a boolean that indicates if the graph is weighted or not, if it is weighted any value can be inserted, anything else than 0 indicates connection; if is not weighted only a 1 or a 0 might be inserted, 1 indicates connection, 0 does not

## Explaining methods
### print_matrix:
Does not require or return any value, it just outputs the matrix in a visual way in the console

### vertex_in_graph
Expects as input a vertex name, and it returns True/false depending if a vertex with such name exist in the graph

### pos_in_graph
This also expects a name of a vertex, and it returns the index of the array 2D in which is founded; mainly for development reasons

### rename_vertex
Expects the name of a current vertex and a new one of the developer's choice; if the vertex exist, the method rename it; otherwise return a None value

### establish_connection
Expects the name of 2 vertex and a value, if the vertex exists it creates a connection with the inputed value; else, returns a None value
#### if is a directed graph:
It only creates a connection from vertex 1 to vertex 2
#### otherwise:
Creates a connection from vertex 1 to vertex 2, and the other way arround
#### if is a weighted graph:
you can insert any value, insert a 0 is the same than delete the connection
#### otherwise
You can insert only 0 and 1 (the value of the method's input is ignored), insert a 0 is the same than delete the connection


### connections_to_it
Expects a vertex name and returns how many other vertex are conected to it, same value as the connections out of it, for non directed graphs

### connections_outof_it
Expects a vertex name and returns how many other vertex are conected from it, same value as the connections to it, for non directed graphs

### add_vertex
Expects a vertex name that is not in the graph, and adds it to it; in the vertex exist in the graph, the method returns a None value

### are_connected
Expects two vertex names that are in the graph, it tells True/false depending if they are connected to each other or not; the method returns a None value if a vertex is not in the graph

### connection_value
Expects two vertex names that are in the graph, it returns the value of the connection between vertex; the method returns a None value if a vertex is not in the graph

### delete_vertex
Expects a vertex name that is in the graph, and deletes it from it; if the vertex doesn't exist in the graph, the method does nothing

### delete_connection
It does what "establish_connection" do, but with the value of 0

### mrwov
#### short for "my relation with the other vertex"
Expects a vertex name that is in the graph, and returns a dictionary with the pairs of vertex-edge's values of all the other vertex in the graph related to it; if the vertex doesn't exist in the graph, the method does nothing. This dictionary is the same as the one returned by "ovrwm" when the graph is not directed

### ovrwm
#### short for "other vertex related to me"
Expects a vertex name that is in the graph, and returns a dictionary with the pairs of vertex-edge's values of all the other vertex in the graph on which the original vertex has connection to; if the vertex doesn't exist in the graph, the method does nothing. This dictionary is the same as the one returned by "mrwov" when the graph is not directed

### all_my_connections
Does the same as mrwov, but this does not return the pairs "key-value" in whose value equals 0

### im_connected_to
Does the same as ovrwm, but this does not return the pairs "key-value" in whose value equals 0

### anctm
#### short for "are not connected to me"
Does the same as mrwov, but this only return the pairs "key-value" in whose value equals 0

### inct
#### short for "I'm not connected to"
Does the same as ovrwn, but this only return the pairs "key-value" in whose value equals 0

# Things to do for the next version
1.- Obtain the graph from a csv file, validate it, work on it and write the new graph in other file or overwrite it
2.- Obtain the graph from an 2D Array, validate it, work on it and write the new graph in other array 2D or overwrite it
3.- Find a way to generate an image with the graph represented in the traditional way, and not as a matrix
