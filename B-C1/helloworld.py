import webapp2
from google.appengine.ext.webapp import template
from google.appengine.ext import db
import os
class Employee(db.Model):
    firstname=db.StringProperty()
    lastname=db.StringProperty()
    department=db.StringProperty()
    salary=db.IntegerProperty()
    date=db.DateTimeProperty(auto_now_add=True)
    
class MainPage(webapp2.RequestHandler):
    def get(self):
        employee_query=Employee.all()
        employees=employee_query.fetch(10)
        template_values={'employees':employees}
        path=os.path.join(os.path.dirname(__file__),'index.html')
        self.response.out.write(template.render(path,template_values))

class AddEmployee(webapp2.RequestHandler):
    def post(self):
        employee=Employee()
        employee.firstname=self.request.get('fname')
        employee.lastname=self.request.get('lname')
        employee.department=self.request.get('dept')
        try:
            employee.salary=int(self.request.get('salary'))
            employee.put()
            self.redirect('/')
        except ValueError:
                st={"error":"Error in values"} 
                path=os.path.join(os.path.dirname(__file__),'index.html')
                self.response.out.write(template.render(path,st))
                #self.redirect('/')
            
            

app=webapp2.WSGIApplication([('/',MainPage),('/add',AddEmployee)],debug=True)
if __name__ == "__main__":
    app.run()
