from graph_traversal import VisualizeGraphTraversal
from packages import *


def main():

    root = Tk()
    root.title("Graph Traversal Visualizer")
    root.geometry("400x600")
    root.maxsize(500, 600)
    root.minsize(500, 600)
    root.config(bg="orange")
    VisualizeGraphTraversal(root)
    root.mainloop()



if __name__ == "__main__":
    main()