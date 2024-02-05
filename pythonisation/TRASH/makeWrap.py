import sys

lines = open("Capi").readlines()
print("import ctypes\n")
com = '\t"""\n'
for k,l in enumerate(lines):
    if l.find("DWORD _ICNC")==0:
        k1 = l.index("(")
        k2 = l.index(")")
        nom = l[12:k1+1]
        param = l[k1:k2+1]
        param = param.replace("(","")
        param = param.replace(")","")
        ps = param.split(",")
        inp = []
        out = []
        for p in ps:
            if p.find("*")!=-1:
                inp.append(p) 
            else:
                out.append(p)
        newLine = "def "+nom
        if len(out)==0:
            newLine += "("
        for p in out:
            newLine += p+","
        newLine =  newLine[0:-1]+"):"
        if len(inp)!=0:
            newLine += " # output param:"
        for p in inp:
            newLine += p.replace("\n","")+" "
        newLine = newLine.replace("DWORD","")
        newLine = newLine.replace("BOOL","")
        newLine = newLine.replace("INT","")
        newLine += "\n"
        print(newLine,end="")
        continue
    if l[0:2] == "//":
        com += "\t"+l[3:]
        continue
    # ici line vide = fin enregistrement
    if len(l)!=1:
        print("OOPS")
        sys.exit(1)
    com += '\t"""\n'
    com += "\tprint('non implemente')\n"
    com += "\treturn -1\n\n"
    print(com)
    com = '\t"""\n'

com += '\t"""\n'
com += "\tprint('non implemente')\n"
com += "\treturn -1\n\n"
print(com)
