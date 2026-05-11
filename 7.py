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

    
    
    def display_patients(self):
        for i in self.patients:
            print(f'the patient is {i.name}')

class Patient:

    def __init__(self,name,phone):
        self.phone=phone
        self.name=name
        self.appointments=[]

    def book_appointments(self,doctor):
        self.appointments.append(doctor)
        doctor.patients.append(self)
    
    def show_appointments(self):

        if len(self.appointments)==0:
            print(f"there are no appointments for {self.name}")

        for i in self.appointments:
            print(f"patient {self.name} have appoiment with doctor {i.name}")
    def cancel_appointments(self,doctor):

        if doctor in self.appointments:
            self.appointments.remove(doctor)
            doctor.patients.remove(self)
    
  




    
p1=Patient("felix",234)
p2=Patient("jobi",678)

d1=Doctor("ethan","neuro")
d2=Doctor("melvin","cardio")


p1.book_appointments(d1)
p2.book_appointments(d2)
d1.display_patients()
p1.show_appointments()

p1.cancel_appointments(d1)
p1.show_appointments()



    

        