Disclaimer: I think I'm doing way too much here because is a test for a job. Software engineering as literally everything on computer science and technology is a tradeoff.
This piece of software was very complex to design because it's functionality is rather simplistic. I could solve it all with 5 lines of code or maybe less (of course without considering any wild edge case). Usually design patterns and code design abstract operations decreasing complexity but here I felt like I was increasing complexity for no reason. There is no way someone will change half of the interfaces here.

I mean, the code is extremly modular right now and change a small part of it is pretty easy, but <b>I think it would be better if this software simply had less parts</b>.
I actually had one experience like that where someone did a MVC application to do some data extraction and I went for a script mapping extraction fields to the database. The script was very robust and simple as it was just a couple lines of code. When the extraction format changed it completly broke at least half of the MVC application. The models simply didn't work anymore but my script could have survived the process.

I am just saying sometimes less is more and this code is just me showing off. I wouldn't go with it for production.

# Folder structure

- DesignPatterns -> This folder contains reusable implementations of mine of some deisgn pattern I decided to use on the application. I made it all from scratch. I went for some very popular patterns among web developers (DependencyInjection and Facades) because people just love web development so much!

- Datastructures -> This folder contains enums and simple structures to hold data. Those structures are responsible to validate the data inside them or execute structure specific logic.

- Validation -> This one includes my special custom made testing library just for you guys as I know you love tests! It's simple but it was from the heart. The library just contains one *pseudo decorator* and one enum to control it's configuration.

- TestCases -> This folder contains all tests wrote using my *pseudo decorator*. Those tests are runned automatically if you pass the --test flag to the program and completly ignored if you don't.

\* I'm saying pseudo decorator here because it's not really a 
decorator. <b>It does not returns a function, it actually execute the tests</b>. I just fooled the python interpreter into letting me using the cool @ syntax. Pretty cool, right? I mean, I thought it was cool at least.