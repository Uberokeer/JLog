import json
import os
import node
import nodehandler
class logicalnotation:
    def get_program(file_path):
        try:
            with open(file_path) as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("(mod)Logicalnotation.py - (def)get_program - Error: (Object manifest not found at: '"+file_path+"')")
            return None
        except json.JSONDecodeError:
            print("(mod)Logicalnotation.py - (def)get_program - Error: (Invalid JSON format in file at: '"+file_path+"')")
            return None
    def interpret_json_objects(JSON_file):
        if (JSON_file == None):
            print("(mod)Logicalnotation.py - (def)interpret_json_objects - Error: (JSON_file is null)")
        else:
            try:
                for index, item in enumerate(JSON_file):
                    name = item['name']
                    arguments = item['args']
                    body = item['body']
                    passvar = item['pass']
                    object_data = [name,arguments,body,passvar]
                    logicalnotation.object_to_node(object_data)
            except (KeyError, TypeError): 
                print(f"(mod)Logicalnotation.py - (def)interpret_json_objects - Error: (The program found at: ({load_url}) does not contain the proper headers: 'name', 'args', 'body', or 'pass')")
                print(f"Exception occured on object: {index+1}")
    def object_to_node(object_data):
        n = node.node(object_data)
        logicalnotation.add_to_environment(n)
    def add_to_environment(node_to_add):
        ne.add_node(node_to_add)

#class tests (MAIN)
print("Please enter path of JSON file to interpret")
load_url = input()
if (os.path.exists(load_url)):
    ne = nodehandler.node_handler
    print("Reading JSON file")
    json_file = logicalnotation.get_program(load_url)
    print("File read successfully")
    print("Interpreting file objects")
    logicalnotation.interpret_json_objects(json_file)
    print("Objects successfully interpreted")
    #ne.print_nodes()
    print("Executing objects")
    ne.execute_environment()
else:
    print("Please enter a valid path")