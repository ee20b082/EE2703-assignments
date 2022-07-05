import sys
begining = ".circuit"
ending = ".end"


#below function to identify each lines and classify them into Independent and dependendent sources
def parse_each_line(eachline):
    words=eachline.split()
    elementname=words[0]#to know the element in circuit
    node1=words[1]
    node2=words[2]
    
    #for identifying Independent Sources
    if(len(words) == 4):
        value=words[3]
        return [ elementname, node1, node2, value]

    #for identifying Current controlled sources
    elif(len(words)==5):
        new_voltageSource = words[3]
        value = words[4]
        return [elementname, node1, node2, new_voltageSource, value]

    #for identifying Current controlled sources
    elif(len(words)==6):
        new_voltageSource1 = words[3]
        new_voltageSource2 = words[4]
        value = words[5]
        return [elementname, node1, node2, new_voltageSource1, new_voltageSource2, value]
    else:
        return []

#if len(sys.argv)<2 then entire information(either .netlist or file name) is not provided.
if(len(sys.argv)==2):

    #try-except is used to verify given file exists or not and if given circuit is according to required format.
    try:
        #opening file with "with open()" and analyzing the circuit details.
        with open(sys.argv[1]) as f:
            lines = f.readlines()
            start = 0 ; end = 0
            count=0
            for line in lines:
                if (begining == line[:len(begining)]):
                    start = lines.index(line)
                    count+=1
                elif(ending == line[:len(ending)]):
                    end = lines.index(line)
                    count+=1
                    break
            #'count' is to check if both 'begining' and 'ending' are present.

            #if index of 'begining' greater than index of 'ending' or if either one of 'ending' ,'begining' is absent 
            # then we need to print error
            if(start>=end or count!=2):
                print("INVALID CIRCUIT DEFINITION")
                sys.exit()
            lines_of_circuit_details = lines[start+1:end]
            circuit_details=[]
            for line in lines_of_circuit_details:
                circuit_details.append(parse_each_line(line))
            #circuit_details contain details about dependent and independent sources. And index '0' of each individual list give type of
            #element(eg: R L C ...)

            #below line is to print in reverse
            for line in reversed([' '.join(reversed(line.split('#')[0].split())) for line in lines[start+1:end]]):
                print(line) 
    except IOError:
        print("Given file does not exist. ERROR in file name")
else:
    #printing error if input is not sufficient.
    sys.exit("Invalid number of arguments! Pass the netlist file as the second argument.")