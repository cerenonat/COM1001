# 3.6 Turing Test Medical Diagnosis
problem = input("What is your problem? ")
past = input("Have you had this problem before (yes or no)? ")

if past.lower() == 'yes':
    print("Well, you have it again.")
else:
    print("Well, you have it now.")
