# JLog
A Python logical notation interpreter for JSON 

<h2>Overview</h2>

<p>This Python program is designed to interpret JSON files and allow logical representation within them. It provides a flexible way to structure objects within the JSON files and perform operations on them. The program leverages the "name", "args", "body", and "pass" attributes of each object to define their behavior and relationships.</p>

<p>Each object within a JSON file is read by the interpreter and converted to an instance of the Node class. These classes are then further parsed and executed by the nodehandler module.</p>

<h2>Features</h2>
    <p><b>JSON Interpretation:</b> The program reads and interprets JSON files, extracting the necessary information to create logical representations of objects.</p>
    <p><b>Object Structure:</b> Each object within the JSON file follows a specific structure, including "name", "args", "body", and "pass". This structure allows for clear definition and composition of objects.</p>
    <p><b>Arguments and Operations:</b> The "args" attribute specifies the arguments required by an object, while the "body" attribute contains the operations to be performed on those arguments. This allows for flexible and customizable logic.</p>
    <p><b>Passing Objects:</b> The "pass" attribute indicates the final product after the body, and specifies the object to which it should be passed. This enables the chaining of objects to create complex logical representations.</p>
    <p><b>Python Code Execution:</b> The "body" attribute is interpreted as Python code, allowing for the execution of a wide range of operations on the arguments and variables defined in the body.</p>
    <p><b>Flexibility and Customization:</b> The program provides a flexible framework for creating logical representations, enabling users to define their own objects and behaviors based on their specific requirements.</p>
