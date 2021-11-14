#A python program to shut down your computer.
#For this program OS library, which can be installed using pip install os. You can shut down, restart,
# and even set a timer for shutdown or restart with this package.

import os
print(" Alert:- Save your  work before shutdown...")
shutdown = input("Do you want to shutdown your computer(Yes / No ): ")
if shutdown == "Yes":
    os.system("shutdown /s /t 1")
else:
     print("Shutdown is not requested...Thankyou")