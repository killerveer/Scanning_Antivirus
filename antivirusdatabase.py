dbse=list(open('virus hash.txt','r').readlines())

for i in dbse:
    abc = open('hashvirusnames.txt','a').writelines(i[0:64]+'\n')
    xyz = open('virusinfo.txt','a').writelines(i[65:len(i)])
 