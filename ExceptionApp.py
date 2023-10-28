# Exception class in case Ward number mismatched

class WardError (Exception):
     def __init__(self, message):
        self.message = message
   
     def __str__(self):
        return(self.message)

# Exception class in case Patient number  mismatched

class PatientError (Exception):
     def __init__(self, message):
        self.message = message
   
     def __str__(self):
        return(self.message)

# Exception class in case Date format is  mismatched

class DateFormatError (Exception):
     def __init__(self, message):
        self.message = message
   
     def __str__(self):
        return(self.message)

