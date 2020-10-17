class PreProcess:

    def __init__(self):
        self.relation = ""
        self.inputs = {}
        self.output = {}
        self.data = []

    def parser(self, arq):
        file = open(arq, "r")
        for line in file:
            if line.__contains__("relation"):
                self.relation = line.split(" ")[1]
            elif line.__contains__("["):
                universe = line.split("[")
                interval = universe[1].split("]")[0].replace(" ", "").split(",")
                self.inputs[universe[0].split(" ")[1]] = interval
            elif line.__contains__("{"):
                label = line.split("{")[1].split("}")[0].replace(" ", "").split(",")
                for index in range(len(label)):
                    self.output[label[index]] = index;
            elif line.__contains__("data"):
                self.getDatas(file)

    def getDatas(self, file):
        for line in file:
            sample = line.replace(" ", "").split("\n")[0].split(",")
            rotulo = sample.__getitem__(len(sample)-1)
            idRotulo = self.output[rotulo]
            sample[len(sample)-1] = idRotulo
            self.data.append(sample)






