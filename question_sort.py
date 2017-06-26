class Unit:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def addQuestion(self, question):
        self.questions.append(question)

    def sort(self):
        self.questions = sorted(self.questions, reverse = True, key= lambda q: q.occurance)


class Question:
    def __init__(self, question, occurance):
        self.question = question
        self.occurance = occurance

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        qStr = self.question

        if self.occurance > 1:
            qStr += '  x' + str(self.occurance)
        return qStr

def parseQuestion(line):
    line = line.strip()
    occurance = 1

    if(line[-2:-1].lower() == 'x' and line[-1:].isdigit() ):
        occurance = int(line[-1:])

    if occurance > 1:
        question = line[:-2].strip()
    else:
        question = line.strip()
    return Question(question, occurance)

def parseUnit(unit):
    unitName = unit[0]
    unit = unit[1:]

    u = Unit(unitName)

    for line in unit:
        u.addQuestion(parseQuestion(line))

    return u

def fileToUnits(filename):
    fContents = None
    nums = list(range(10))
    nums = [str(num) for num in nums]

    with open(filename) as f:
        fContents = f.read()

    lines = fContents.split('\n')
    lines = [line for line in lines if line.strip() != '']
    units = []
    for i in range(len(lines)):
        line = lines[i]
        unitFound = True
        for num in nums:
            if line.startswith(num):
                unitFound = False
                break

        if unitFound and line.strip() != '':
            units.append(i)

    unitQuestions =[]
    for i in range(len(units)):
        if i == len(units) - 1:
            unitQuestions.append(lines[units[i]:])
        else:
            unitQuestions.append(lines[units[i]:units[i + 1]] )

    unitObjs = [parseUnit(uq) for uq in unitQuestions]

    return unitObjs

def unitsToFile(units, filename):
    with open(filename, 'w') as f:
        for u in units:
            f.write(u.name + '\n')
            for q in u.questions:
                f.write(str(q) + '\n')
            f.write('\n\n')


if __name__ == '__main__':
    units = fileToUnits('ME.txt')

    for u in units:
        u.sort()

    unitsToFile(units, 'MEsorted.txt')
