import json
import node

class logicalnotation:
    def interpret_nodes(data):
        node_map = {}
        try: #try for type error
            for index, item in enumerate(data): # for nodes in laoded json file
                name = item['name']
                arguments = item['args']
                body = item['body']
                passvar = item['pass']
                node_map[name] = (arguments, body, passvar) #sets corresponding node_map value to tuple with args, body, and pass
                logicalnotation.build_from_node(name, node_map[name]) #invokes node builder
        except (KeyError, TypeError): 
            print(f"The program found at: ({load_url}) does not contain the proper headers: 'name', 'args', 'body', or 'pass'")
            print(f"Exception occured on object: {index+1}")
        
        print(*node_list)
        logicalnotation.execute_node_list(node_list)
    def build_from_node(node_name, nvals): #Evaluates single node from json file and builds new node class
        node_ref = node.node()
        new_node = type(node_ref)
        setattr(new_node, "name",node_name)
        setattr(new_node, "args",nvals[0])
        setattr(new_node, "body",nvals[1])
        setattr(new_node, "passvar",nvals[2])
        
        node_list.append(new_node)
    
    def execute_node_list(nlist):
        for c in nlist:
            c.print_node(c)
                        

def get_program(file_path):
        try:
            with open(file_path) as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("ClassBuilder.py - Error: (Object manifest not found at: '"+file_path+"')")
            return None
        except json.JSONDecodeError:
            print("ClassBuilder.py - Error: (Invalid JSON format in file at: '"+file_path+"')")
            return None
        
node_list = []
load_url = 'Data/programtest.json'
data = get_program(load_url)
logicalnotation.interpret_nodes(data)