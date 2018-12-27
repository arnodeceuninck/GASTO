class HtmlRapport:
    def __init__(self, filename):
        self.file_structure = []
        self.filename = filename
    def buildfile(self):
        file_string = "<html>\n<head>\n<style>\n" \
                      "table {\nborder-collapse: collapse;\n}\n\n" \
                      "table, td, th {\nborder: 1px solid black;\n}\n" \
                      "</style>\n</head>\n<body>\n"
        for structure in self.file_structure:
            file_string += str(structure)
        file_string += "</body>"

        f = open(self.filename, 'w+')
        f.write(file_string)
        f.close()

    def addStructure(self, structure):
        self.file_structure.append(structure)

class HtmlTitle:
    def __init__(self, text):  # Text must be a string
        self.text = text
    def __str__(self):
        return "<h1>" + self.text + "</h1>\n"


class HtmlTable:
    def __init__(self, matrix):  # matrix [0][1] is op de bovenste rij, het tweede element
        self.matrix = matrix

    def __str__(self):
        tablestring = "<table>"
        firstRow = True
        for row in self.matrix:
            if firstRow:
                tablestring += "<thead>\n"
            else:
                tablestring += "<tr>\n"

            for column in row:
                tablestring += "<td>" + str(column) + "</td>\n"

            if firstRow:
                tablestring += "</thead>\n"
                if len(self.matrix) > 1:
                    tablestring += "<tbody>\n"
                firstRow = False
            else:
                tablestring += "</tr>\n"

        if len(self.matrix) > 1:
            tablestring += "</tbody>\n"
        tablestring += "</table>\n"
        return tablestring


testrapport = HtmlRapport("test.html")

testrapport.addStructure(HtmlTitle("Hello World! :-)"))

tabel = []
tabel.append(["Kolom 1", "Kolom 2", "Kolom 3"])
tabel.append(["Never", "Gonna", "Give"])
tabel.append(["You", "Up", "Never"])
tabel.append(["Gonna", "Let", "You"])
tabel.append(["Down"])
testrapport.addStructure(HtmlTable(tabel))

testrapport.buildfile()