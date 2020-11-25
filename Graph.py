class Graph:
    """se esperan 3 argumentos:
    vertex: entero; numero de vetices
    directed: si el grafo es dirigido o no
    weighted: si el grafo tiene peso o no
    primero fila y despues columna
    """

    def __init__(self, vertex, directed, weighted):
        self.vertex = vertex
        self.directed = directed
        self.weighted= weighted
        self.matrix=[]
        for a in range (self.vertex+1):
            (self.matrix).append([])
            for b in range(self.vertex+1):
                (self.matrix[a]).append(0)

        for i in range (len(self.matrix)):
            if i==0: pass
            else :
                self.matrix[i][0]=i
            for j in range (len(self.matrix[i])):
                if j==0: pass
                else:
                    self.matrix[0][j]=j
        self.matrix[0][0]=""

    #imprime la matriz de adyacencia en consola
    def print_matrix(self):
        """for i in self.matrix:
            for j in i:
                print("{:<3} {:<6}".format(i,j))"""

        for i in range (len (self.matrix)):
            for j in range (len(self.matrix[i])):
                print("%5s " % (self.matrix[i][j]), end="")
                if j==0: print("|", end="")
            print("\n")
            if i==0:
                for j in range (len(self.matrix[i])):
                    print("%5s " % ("-----"), end="")
                    if j==0: print("|", end="")
                print("\n")

    #avisa si el vertice buscado esta establecido en el grafo
    def vertex_in_graph(self, searched_v):
        searched_v= str(searched_v)
        in_row=False
        in_col=False
        for i in range (len(self.matrix)):
            if searched_v==str(self.matrix[i][0]):
                in_row=True
                pos_row=i
            for j in range (len(self.matrix[i])):
                if searched_v==str(self.matrix[0][j]):
                    in_col=True
                    pos_col=j
        if (in_row==True) and (in_col==True) and (pos_col==pos_row):
            return True
        else: return False

    #estblece en que posicion de la matriz esta el vertice, para propositos del programador
    def pos_in_graph(self, vertex):
        if self.vertex_in_graph(vertex)==True:
            for i in range (len(self.matrix)):
                if str(vertex)==str(self.matrix[i][0]):
                    pos_row=i
            return pos_row
        else: return None

    #rebautiza un vertice
    def rename_vertex(self, renamed_v, new_name):
        if self.vertex_in_graph(new_name)==True:
            return None

        elif self.vertex_in_graph(renamed_v)==True:
            position=self.pos_in_graph(renamed_v)
            self.matrix[position][0]=new_name
            self.matrix[0][position]=new_name


        else: return None

    #establece una conexion, si el grafo está dirigido lo hará desde ese vertice y hasa el otro vertice
    #si no está dirigido, lo creará en ambas direcciones de la matriz
    #si el grafo tiene peso puede ser cualquier valor positivo o negativo
    #si el grafo no tiene peso, sin importar el valor que se ponga se establecerá un 1
    #si el valor quda como 0 es como no haber estabecido ninguna conexion
    def establish_connection(self, fro, to, value):
        if (self.vertex_in_graph(fro)==True) and (self.vertex_in_graph(to)==True):
            pos_from=self.pos_in_graph(fro)
            pos_to=self.pos_in_graph(to)
            if self.directed==True:
                if self.weighted==False:
                    if value==0: self.matrix[pos_from][pos_to]=0
                    else: self.matrix[pos_from][pos_to]=1
                elif self.weighted==True:
                    self.matrix[pos_from][pos_to]=value
            elif self.directed==False:
                if self.weighted==False:
                    if value==0:
                        self.matrix[pos_from][pos_to]=0
                        self.matrix[pos_to][pos_from]=0
                    else:
                        self.matrix[pos_from][pos_to]=1
                        self.matrix[pos_to][pos_from]=1
                elif self.weighted==True:
                    self.matrix[pos_from][pos_to]=value
                    self.matrix[pos_to][pos_from]=value

        else: return None
    #metodo de alan
    def connections_to_it(self, vertex):
        if self.vertex_in_graph(vertex)==True:
            pos_vertex=self.pos_in_graph(vertex)
            contador=0
            for j in range (len(self.matrix)):
                if j==0: pass
                elif self.matrix[j][pos_vertex]!=0:
                    contador+=1
            return contador
        else: return None

    #conexion que sale de un nodo, es igual que las que entran si el grafo no está dirigido
    def connections_outof_it(self, vertex):
        if self.vertex_in_graph(vertex)==True:
            pos_vertex=self.pos_in_graph(vertex)
            contador=0
            for j in range (len(self.matrix)):
                if j==0: pass
                elif self.matrix[pos_vertex][j]!=0:
                    contador+=1
            return contador
        else: return None

    #añadir un vertice
    def add_vertex(self, vertex_name):
        if self.vertex_in_graph(vertex_name)==True:
            return None
        else:
            (self.matrix).append([])
            for i in range (len(self.matrix)):
                for j in range (len(self.matrix)):
                    if (i==0) and (j==(len(self.matrix))-1):
                        (self.matrix[i]).append(vertex_name)
                    elif (i>0) and (i<len((self.matrix))-1) and  (j==(len(self.matrix)-1)):
                        (self.matrix[i]).append(0)
                    elif (j==0) and (i==len((self.matrix))-1):
                        (self.matrix[i]).append(vertex_name)
                    elif (j>0) and (i==len((self.matrix))-1):
                        (self.matrix[i]).append(0)

    def are_connected(self,v1,v2):
        if (self.vertex_in_graph(v1)==True) and (self.vertex_in_graph(v2)==True):
            pos_v1=self.pos_in_graph(v1)
            pos_v2=self.pos_in_graph(v2)
            if (self.directed==True):
                if (self.matrix[pos_v1][pos_v2]!=0):
                    return True
                else: return False
            elif (self.directed==False):
                if (self.matrix[pos_v1][pos_v2]!=0) and (self.matrix[pos_v2][pos_v1]!=0):
                    return True
                else: return False
            else: return False
        else: return None

    def connection_value(self, v1, v2):
        if (self.vertex_in_graph(v1)==True) and (self.vertex_in_graph(v2)==True):
            pos_v1=self.pos_in_graph(v1)
            pos_v2=self.pos_in_graph(v2)
            return self.matrix[pos_v1][pos_v2]
        else:return None

    def delete_vertex(self, dv):
        if (self.vertex_in_graph(dv)==True):
            #dv-> deleted vertex
            pos_dv=self.pos_in_graph(dv)
            (self.matrix).pop(pos_dv)
            for i in range (len(self.matrix)):
                for j in range (len(self.matrix)):
                    if j==pos_dv:
                        (self.matrix[i]).pop(j)

    def delete_connection(self, v1, v2):
        if (self.vertex_in_graph(v1)==True) and (self.vertex_in_graph(v2)==True):
            pos_v1=self.pos_in_graph(v1)
            pos_v2=self.pos_in_graph(v2)
            value=self.matrix[pos_v1][pos_v2]
            self.establish_connection(v1,v2,0)
            return value
        else: return None

    #my relation with the other vertex
    def mrwov(self, vertex):
        if (self.vertex_in_graph(vertex)==True):
            relation={}
            pos_v=self.pos_in_graph(vertex)
            for i in range (len(self.matrix)):
                for j in range (len(self.matrix)):
                    if j==0: pass
                    elif i==pos_v:
                        relation[(self.matrix[0][j])]=(self.matrix[i][j])
            return relation
        else: return None

    #other vertex related to me
    #same as mrwov when the graph is not directed
    def ovrwm (self, vertex):
        if (self.vertex_in_graph(vertex)==True):
            relation={}
            pos_v=self.pos_in_graph(vertex)
            for i in range (len(self.matrix)):
                for j in range (len(self.matrix)):
                    if i==0:pass
                    elif j==pos_v:
                        relation[(self.matrix[i][0])]=(self.matrix[i][j])
            return relation
        else: return None

    def all_my_connections(self, v):
        if (self.vertex_in_graph(v)==True):
            todo=self.mrwov(v)
            solo_conexiones={}
            for i in todo:
                if todo[i]!=0:
                    solo_conexiones[i]=todo[i]
            return solo_conexiones
        else: return None

    def im_connected_to(self, v):
        if (self.vertex_in_graph(v)==True):
            todo=self.ovrwm(v)
            solo_conexiones={}
            for i in todo:
                if todo[i]!=0:
                    solo_conexiones[i]=todo[i]
            return solo_conexiones
        else: return None

    #are not connected to me
    def anctm(self, v):
        if (self.vertex_in_graph(v)==True):
            todo=self.mrwov(v)
            solo_conexiones=[]
            for i in todo:
                if todo[i]==0:
                    solo_conexiones.append(i)
            return solo_conexiones
        else: return None

    #i'm not connected to
    def inct(self, v):
        if (self.vertex_in_graph(v)==True):
            todo=self.ovrwm(v)
            solo_conexiones=[]
            for i in todo:
                if todo[i]==0:
                    solo_conexiones.append(i)
            return solo_conexiones
        else: return None

# I LOVE YOU MONTSE <3

"""
def main():
    grafo=Graph(4, True, True)
    grafo.print_matrix()
    #si existe
    print(grafo.vertex_in_graph(2))
    #no existe
    print(grafo.vertex_in_graph(6))
    #si existe
    print(grafo.pos_in_graph(2))
    #no existe
    print(grafo.pos_in_graph(6))
    grafo.rename_vertex(2,"A")
    grafo.print_matrix()
    grafo.establish_connection(1,"A",11)
    grafo.print_matrix()
    print(grafo.connections_to_it("A"))
    grafo.add_vertex("W")
    grafo.print_matrix()
    grafo.add_vertex("H")
    grafo.print_matrix()
    grafo.establish_connection(1,"W",6)
    grafo.print_matrix()
    print(grafo.connections_outof_it(1))
    print(grafo.connections_to_it("W"))
    print(grafo.connections_outof_it("W"))
    print(grafo.are_connected("W",1))
    print(grafo.are_connected(1,"W"))
    print(grafo.connection_value(1, "W"))
    grafo.delete_vertex("A")
    grafo.print_matrix()
    print(grafo.mrwov("W"))
    print(grafo.ovrwm("W"))
    print(grafo.all_my_connections(1))
    print(grafo.im_connected_to("W"))
    print(grafo.anctm(1))
    print(grafo.inct("W"))
main()
"""
