class Employee:
    def __init__(self, name, division, jopgrade, years, basic):
        self.name = name
        self.division = division
        self.jopgrade = float(jopgrade)
        self.years = float(years)
        self.basic = float(basic)

    def getName(self):
        return self.name
    def getdivision(self):
        return self.division
    def getJopGrade(self):
        return self.jopgrade
    def getyear(self):
        return self.years
    def getbasic(self):
        return self.basic
    def salary(self):
        self.salary = self.basic + (self.basic * self.years * 0.1)
        return self.salary

def makeEmployee(inputdata):
    name, division, jopgrade, year, basic = inputdata.split(',')
    basic = basic[:-2]
    return Employee(name, division, jopgrade, year, basic)

def main():
    filename = 'employeefile.txt'
    inputfile = open(filename, 'r')
    highest = makeEmployee(inputfile.readline())
    for line in inputfile:
        e = makeEmployee(line)
        if e.years() > highest.years():
            highest = e
    inputfile.close()
    
    print("The Name of highest salary employee is", highest.getName())
    print("years of services", highest.getyear())
    print("division", highest.getdivision())
    print("salay", highest.salary())

if __name__ == '__main__':
    main()