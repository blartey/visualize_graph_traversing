from packages import *

class VisualizeGraphTraversal:

    def __init__(self, root) -> None:
        self.window = root
        self.make_canvas = Canvas(self.window, bg="chocolate", relief=RAISED, bd=7, width=WIDTH, height=HEIGHT)
        self.make_canvas.pack()
        self.vertex_store = []
        self.total_circle = []
        self.queue = []
        self.stack = []

        # status label initialization
        self.status = None

        # invoke default functions
        self.basic_set_up()
        self.make_vertex()

       

    def basic_set_up(self):
        # algs = Algorithms(self.window)
        heading = Label(self.make_canvas,text="Graph Traversing Visualization",bg="chocolate",fg="yellow",font=("Arial",20,"bold","italic"))
        heading.place(x=50,y=10)

        bfs_btn = Button(self.window,text="BFS",font=("Arial",15,"bold"),bg="black",fg="green",relief=RAISED,bd=8,command=self.bfs)
        bfs_btn.place(x=20,y=530)

        dfs_btn = Button(self.window, text="DFS", font=("Arial", 15, "bold"), bg="black", fg="green", relief=RAISED, bd=8, command=self.dfs)
        dfs_btn.place(x=400, y=530)

        self.status = Label(self.make_canvas,text="Not Visited",bg="chocolate",fg="brown",font=("Arial",20,"bold","italic"))
        self.status.place(x=50,y=450)

    def make_vertex(self):# Vertex with connection make
        for i in range(15):
            self.total_circle.append(i)

        self.total_circle[0] = self.make_canvas.create_oval(80,250,110,280,width=3)

        self.total_circle[1] = self.make_canvas.create_oval(160, 180, 190, 210, width=3)

        self.total_circle[2] = self.make_canvas.create_oval(160, 320, 190, 350, width=3)

        self.total_circle[3] = self.make_canvas.create_oval(230, 130, 260, 160, width=3)

        self.total_circle[4] = self.make_canvas.create_oval(230, 230, 260, 260, width=3)

        self.total_circle[5] = self.make_canvas.create_oval(230, 270, 260, 300, width=3)

        self.total_circle[6] = self.make_canvas.create_oval(230, 370, 260, 400, width=3)

        self.total_circle[7] = self.make_canvas.create_oval(280, 80, 310, 110, width=3)

        self.total_circle[8] = self.make_canvas.create_oval(280, 180, 310, 210, width=3)

        self.total_circle[9] = self.make_canvas.create_oval(280, 250, 310, 280, width=3)

        self.total_circle[10] = self.make_canvas.create_oval(280, 320, 310, 350, width=3)

        self.total_circle[11] = self.make_canvas.create_oval(280, 420, 310, 450, width=3)

        self.total_circle[12] = self.make_canvas.create_oval(350, 130, 380, 160, width=3)

        self.total_circle[13] = self.make_canvas.create_oval(350, 220, 380, 250, width=3)

        self.total_circle[14] = self.make_canvas.create_oval(350, 360, 380, 390, width=3)

        self.make_connector_up(0, 1)
        self.make_connector_down(0, 2)
        self.collector_connector(0,1,2)

        self.make_connector_up(1, 3)
        self.make_connector_down(1, 4)
        self.collector_connector(1, 3, 4)

        self.make_connector_up(2, 5)
        self.make_connector_down(2, 6)
        self.collector_connector(2, 5, 6)

        self.make_connector_up(3, 7)
        self.make_connector_down(3, 8)
        self.collector_connector(3, 7, 8)

        self.make_connector_down(4, 9)
        self.collector_connector(4, None, 9)

        self.make_connector_down(5, 10)
        self.collector_connector(5, None, 10)

        self.make_connector_down(6, 11)
        self.collector_connector(6, None, 11)

        self.make_connector_up(8, 12)
        self.collector_connector(8, 12, None)

        self.make_connector_up(9, 13)
        self.collector_connector(9, 13, None)

        self.make_connector_down(10, 14)
        self.collector_connector(10, None, 14)

        print(self.vertex_store) 

    def make_connector_up(self,index1,index2):# Up node connection make
        first_coord = self.make_canvas.coords(self.total_circle[index1])# Source node coordinates
        second_coord = self.make_canvas.coords(self.total_circle[index2])# Destination node coordinates
        line_start_x = (first_coord[0]+first_coord[2]) / 2# Connector line start_x
        line_end_x = (second_coord[0]+second_coord[2]) / 2# Connector line end_x
        line_start_y = (first_coord[1]+first_coord[3]) / 2# Connector line start_y
        line_end_y = (second_coord[1]+second_coord[3]) / 2# Connector line end_y
        self.make_canvas.create_line(line_start_x+10,line_start_y-10,line_end_x-10,line_end_y+10,width=3)

    def make_connector_down(self,index1,index2):# Down node connection make
        first_coord = self.make_canvas.coords(self.total_circle[index1])# Source node coordinates
        second_coord = self.make_canvas.coords(self.total_circle[index2])# Destination node coordinates
        line_start_x = (first_coord[0] + first_coord[2]) / 2# Connector line start_x
        line_end_x = (second_coord[0] + second_coord[2]) / 2# Connector line end_x
        line_start_y = (first_coord[1] + first_coord[3]) / 2# Connector line start_y
        line_end_y = (second_coord[1] + second_coord[3]) / 2# Connector line end_y
        self.make_canvas.create_line(line_start_x+12 , line_start_y +5, line_end_x - 12, line_end_y -5, width=3)

    def collector_connector(self,source,connector1,connector2):# All about node data collect and store
        temp = []
        temp.append(self.total_circle[source])

        if connector1:
            temp.append(self.total_circle[connector1])
        else:
            temp.append(None)

        if connector2:
            temp.append(self.total_circle[connector2])
        else:
            temp.append(None)

        self.vertex_store.append(temp)

    def binary_search(self, left, right, source):
        """
        search for source node
        """
        while left <= right:
            mid = (left + right) // 2
            if self.vertex_store[mid][0] == source:
                return self.vertex_store[mid]
            elif self.vertex_store[mid][0] < source:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def bfs(self):
        try:
            self.status["text"] == "blue: visited"
            self.queue.append(self.vertex_store[0][0])
            while self.queue:
                source_node = self.binary_search(0, 9, self.queue[0])
                if source_node != -1:
                    # add neighbors to queue
                    if source_node[1]:
                        self.queue.append(source_node[1]) 
                    if source_node[2]:
                        self.queue.append(source_node[2]) 
                next_node = self.queue.pop(0)
                self.make_canvas.itemconfig(next_node, fill="blue")
                self.window.update()
                time.sleep(0.3)
            self.status["text"] = "All nodes visited."
        except:
            print("Force stop error.")

    def dfs(self):
        try:
            self.status["text"] == "red: visited"
            self.stack.append(self.vertex_store[0][0])
            while self.stack:
                next_node = self.stack.pop()
                self.make_canvas.itemconfig(next_node, fill="red")
                self.window.update()
                time.sleep(0.3)
                source_node = self.binary_search(0, 9, next_node)
                if source_node != -1:
                    # add neighbors to queue
                    if source_node[1]:
                        self.stack.append(source_node[1]) 
                    if source_node[2]:
                        self.stack.append(source_node[2]) 
            self.status["text"] = "All nodes visited."
        except:
            print("Force stop error.")