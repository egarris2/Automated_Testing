class initialSetup (object):
    def __init__(self):
        self.parameter = []
        self.state = []

    def addCondition(self, varParameter, varState):
        self.parameter.append(varParameter)
        self.state.append(varState)

    def printParam(self, param):

        dictmap = {0 : 'L Check', 1 : 'CC Check', 2 : 'A Check', 3 : 'O1 Check', 4 : 'W2 Check', 5 : 'HWG Check'}
        parameter = dictmap.get(param, 'Not Found')
        print parameter
        

    
TableInfo = initialSetup()
