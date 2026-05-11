#hospital management system. 
#doctors are added
#patients are added
#patients have appointment with doctors


class Doctor:

    hospital="memorial hospital"
    
    def __init__(self,name,department):
        self.name=name
        self.department=department
        self.patients=[]
    
    def display_doctor_info(self):
        print(f"the doctor is {self.name} and from {self.department}")

    def add_patient(self,patient_name):
        self.patients.append(patient_name)
    
    def display_patients(self):
        for i in self.patients:
            print(f'the patient is {i.name}')

class Patient:

    def __init__(self,name,phone):
        self.phone=phone
        self.name=name

    
p1=Patient("felix",234)
p2=Patient("jobi",678)

d1=Doctor("ethan","neuro")
d2=Doctor("melvin","cardio")

d1.add_patient(p1)
d1.add_patient(p2)
d1.display_patients()

#add appoiment list to patient to show list of appointments the patient has
#add a function in patient to remove his or her appointment. it should also refect to the doctors patients list

    

        