from restapi.models import EmployeeModel


class Employee:

    def findEmployeeById(self, empId):

          return EmployeeModel.objects.get(id=empId)

    def getEmployeeById(self, id):

        return EmployeeModel.objects.get(id=id)

    def setEmployeeModelObjects(self, postData, empModel=None):

            if empModel is None:
                empModel = EmployeeModel()
            empModel.emp_name = postData['emp_name']
            empModel.emp_emil = postData['emp_email']
            empModel.emp_address = postData['emp_address']
            empModel.emp_city = postData['emp_city']
            return empModel

    def findEmployeeByEmail(self, empEmail):

          return EmployeeModel.objects.get(empEmail=empEmail)
    def findAll(self):

          return EmployeeModel.objects.values()



