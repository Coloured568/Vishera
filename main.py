import vishera
import coloured

# please do not mess with the order of the program :)

# runs when the program is launched
vishera.header(r"""


 /$$    /$$ /$$           /$$                                   
| $$   | $$|__/          | $$                                   
| $$   | $$ /$$  /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$ 
|  $$ / $$/| $$ /$$_____/| $$__  $$ /$$__  $$ /$$__  $$|____  $$
 \  $$ $$/ | $$|  $$$$$$ | $$  \ $$| $$$$$$$$| $$  \__/ /$$$$$$$
  \  $$$/  | $$ \____  $$| $$  | $$| $$_____/| $$      /$$__  $$
   \  $/   | $$ /$$$$$$$/| $$  | $$|  $$$$$$$| $$     |  $$$$$$$
    \_/    |__/|_______/ |__/  |__/ \_______/|__/      \_______/
                                                                
                                                                
Developed by: Coloured                                                
                """)
# runs when the program loads, can handle multiple functions at once.
vishera.vishera_run(
    (
        coloured.cpu, coloured.system, coloured.motd
    )
)

# runs as long as the program is running
vishera.onUpdate(
    coloured.shell
)

'''
Vishera doesn't directly handle lines of code, but rather just executes functions.
In order to keep it clean, it's recommended to make the functions in a seperate file
(as seen in coloured.py)
'''
