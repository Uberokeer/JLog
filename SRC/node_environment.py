import node
node_list = []
class node_handler:
    
    def add_node(node_to_add):
        node_list.append(node_to_add)
    def print_nodes():
        print("Printing from node_list: ")
        for n in node_list:
            print(getattr(n, "nvals"))