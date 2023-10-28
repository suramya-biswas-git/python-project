import WardApp
import PatientApp
# https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/

def hospitalMenu():
    ans="y"
    while ans=="y" or ans=="Y" :
        print("1.Ward Addition")
        print("2.Ward Report")
        print("3.Patient Admission")
        print("4.Patient Release")
        print("5.Exit")
        choice=input("Enter your choice(1-5):")
        match choice:
            case "1" :
                WardApp.wardAddition()
            case "2" :
                WardApp.wardReport()
            case "3" :
                PatientApp.patientEntry()
            case "4" :
                PatientApp.patientRelease()
            case "5" :
                ans="N"

hospitalMenu()
                   
        
