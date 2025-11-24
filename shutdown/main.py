import os

print("A.shutdown\n B.restart\n C.cancel")
choice=input("what is your choice?")
if choice=='A':
    print("shutting down...")
    os.system("shutdown /s /t 5")
elif choice=='B':
    print("restarting...")
    os.system("shutdown /r /t 5")
elif choice=='C':
    print("canceled...")
    exit()
else:
    print("wrong choice!")