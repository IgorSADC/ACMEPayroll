<b> Attention: I didn't have much time to do this exercise. The code quality is not what I really planned but I needed to make some compromises </b>

# Central Design

- ConfigManager is the class responsible to hold all configurations. It's completly static as it is supposed to be accessed trough all the program all the time. Any class that implements the get_value_from_config can be a configuration. 

- The parser is responsible for translating the input in what the program expects. Any class that implements parse_input can be a parser.

- Runner is responsible for calling the other classes and is responsable for holding the businness logic that is not configuration. The runner validate if the configuration has intervals that cover the same hour, for example. The configuration just holds the data, the runner validate it with real world knowlege.

- Datastructures are enums and simple structures to hold data. Those structures are responsible to validate the data inside them or execute structure specific logic. I planned more structures but I am out of time here.


I couldn't document or test my code. I was planning a cool testing library using decorators but I couldn't find the time to do it. I'm sorry.