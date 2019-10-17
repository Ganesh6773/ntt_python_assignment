class FileParser(object):
    '''
        util class, process structured text file, 
        convert it into dict
    '''

    def __init__(self, fileName):
        self.fileName = fileName
        self.dataList = []
        self.parseData()

    def parseData(self):
        '''
            creates list of dict having the data from input txt file
            as key-value pair
        '''
        self.fileContent = ''
        with open(self.fileName, 'r') as fp:
            for line in fp.readlines():
                if(not line):
                    continue
                if(line.startswith('interface')):
                    d = {}
                    ln = line.split()
                    d.update({ln[0]: ln[1]})
                elif('!' in line):
                    self.dataList.append(d)
                elif("ip address" in line):
                    ln = line.split()
                    ipKey = f'{ln[0]}_{ln[1]}'
                    ipVal = ln[2]

                    d.update({ipKey: ipVal})
                    d.update({'subnet': ln[3]})
                elif(len(line) == 1 and not line.isalnum()):
                    continue
                else:
                    ln = line.split()
                    if(len(ln) < 2):
                        raise RuntimeError(
                            f'Error while parsing file. cant determine key-value pair for : {line}')
                    else:
                        d.update({ln[0]: '_'.join(ln[1:])})

    def getInterface(self, val):
        ''' returns dictinary whose interface is val '''

        for item in self.dataList:
            if(item['interface'] == val):
                return item
        return {}

    def getAllInterfaces(self):
        if(not self.dataList):
            return {}
        return self.dataList
