class Student:
    def __init__(self, name, roll_no, department, degree, semester):
        self.name=name
        self.roll_no=roll_no
        self.department=department
        self.degree=degree
        self.semester=semester
    def display_info(self):
        print('-----Student Information-----')  
        print('Name',self.name)  
        print('Roll_no',self.roll_no)
        print('Department',self.department)
        print('Degree',self.degree)
        print('Semester',self.semester)
class DataAnalyticsStudent(Student):
    def __init__(self,name, roll_no, department, degree, semester, python_marks, statistics_marks, excel_marks):
        super().__init__(name, roll_no, department,degree, semester)
        self.python_marks=python_marks
        self.statistics_marks=statistics_marks
        self.excel_marks=excel_marks
    def calculate_average(self):
        average=(self.python_marks+self.statistics_marks+self.excel_marks)/3
        return average
    def display_performance(self):
        average=self.calculate_average()
        print("\n--- Academic Performance ---")
        print("Python:", self.python_marks)
        print("Statistics:", self.statistics_marks)
        print("Excel:", self.excel_marks)
        print("Average Marks:", round(average, 2))

        if average >= 80:
            print("Performance: Excellent")
        elif average >= 60:
            print("Performance: Good")
        elif average >= 50:
            print("Performance: Satisfactory")
        else:
            print("Performance: Needs Improvement")
Student= DataAnalyticsStudent('Muqadas',2097,'Statistics','BS Data Analytics',3,85,78,92)
Student.display_info()
Student.display_performance()        
          

 