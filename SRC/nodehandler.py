import node
node_list = []
class node_handler:
    
    def add_node(node_to_add):
        node_list.append(node_to_add)
    def print_nodes():
        print("Printing from node_list: ")
        for n in node_list:
            print(getattr(n, "nvals"))
            return None
    def execute_environment():
        index = 0
        for n in node_list:
            index+=1
            body = n.nvals[2]
            print(f"Executing node: {index} SRC =", body)
            for seg in body:
                   #fetch arguments
                   exec(seg)
                   #fetch return statement
