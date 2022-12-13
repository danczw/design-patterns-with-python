# decorator method - structural design pattern
#   allows to provide a substitute or placeholder for another object to
#   represent its functionality


# create base class
class PatientFileManager:
    def __init__(self):
        self.__patients = {}
        
    def _add_patient(self, patient_id: str, data: list) -> None:
        self.__patients[patient_id] = data
        
    def _get_patient(self, patient_id) -> list:
        return self.__patients[patient_id]
    

# create proxy class
# - without changing the base code, new proxies can easily be introduced
# - proxy works even when the service object is not ready or is not currently available
# - provides the security to the system
# - increases the performance of the application by avoiding the duplication of
#   the objects which might be huge size and memory intensive
class AccessManager(PatientFileManager):
    def __init__(self, fm: PatientFileManager):
        self.fm = fm
    
    def add_patient(self, patient_id: str, data: list, password: str) -> None:
        if password == 'sudo':
            self.fm._add_patient(patient_id, data)
        else:
            print("Wrong password.")
            
    def get_patient(self, patient_id: str, password: str) -> list:
        if password == 'totallytheirdoctor' or password == 'sudo':
            return self.fm._get_patient(patient_id)
        else:
            print("Only their doctor can access this patients data.")
            return [None]


# run method
if __name__ == '__main__':
    am = AccessManager(PatientFileManager())
    am.add_patient('Jessica', ['pneumonia 2020-23-03', 'shortsighted'], 'sudo')

    print(am.get_patient('Jessica', 'totallytheirdoctor'))