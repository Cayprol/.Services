# .Services

macOS services to create shortcuts and sned command to Terminal.

Must have a .Service folder in home directory containing all the .py files directly without any sub directories.
The .workflow will be able to find at such location for the services to work.

.worksflow files need to be placed at ~/Library/Services
It can be installed by double clicking it, system will move it to the above directory.

________________________________________________________________

Python3 is recommended to avoid bugs.
Default python came with macOS is 2.7 which should work, but all .py files are written with python3 grammar.  
There might be incompatible grammar, if encountered,
1. Try to copy the file to the directory at which the service to perform.

2. Run the .py file by issuing command in terminal at such directory with "python3 example.py", without the quotes, change example to the name of the service.  Verify python3 runs without problem.

3. Change corresponded .workflow file to run python3 not python by open .workflow file in automator.