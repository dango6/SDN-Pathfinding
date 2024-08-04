# SDN-Pathfinding


# PROJECT DESCRIPTION #

In this project, I am going to explore how object oriented programming and graph theory algorithms 
can be applied to accomplish network pathfinding goals such as routing and loop prevention in a 
software defined network

This project will allow me to combine my CCNA and computer science knowledge. This intersection is
an area of significant interest for me, especially considering the ubiquity of software defined networks
as well as their importance in ever-increasing network complexity.

Not only will this project allow me to apply my existing knowledge of networking and programming,
but I will also research and learn about SDN-specific technologies and paradigms as I go.
It will also provide a foundation for Cisco DevNet, a certification that I plan on pursuing in the future




----------------------------------------------------------------------------------------------------------


## First Steps ##

1. Set Up Git Repository:

Created and accessed a new Git repository for the project via WSL
Added POX controller (an open source simulated SDN controller) as a submodule to the repository

2. Configured Environment:

Verified that the Git repository and POX submodule are accessible in WSL
Ensured Python and Mininet, open vSwitch, and various other network simulation tools
are installed and accessible in the WSL environment

3. Incompatibility issues:

After installing all required software, I ran into an issue where the open vSwitch module was not able to run. 
After doing some troubleshooting I determined that the best course of action would
be to start over and use a virtual machine so I can have a native linux environment, 
which will likely be much more compatible with the linux based software than WSL.
Even if I could resolve the specific issue with open vSwitch, I assumed this 
incompatibility would most likely bring more headache in the future
