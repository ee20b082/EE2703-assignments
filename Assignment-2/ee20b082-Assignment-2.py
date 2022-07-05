import sys
import numpy as np
from numpy import sin,cos
begining = ".circuit"
ending = ".end"
ac=".ac"

#to count number of voltage sources and number of inductors.
number_of_voltage_sources=0
number_of_inductors=0
freq=0
nodes=[]
nodes_index={}
voltage_sources=[]
voltage_sources_index={}
inductors=[]
inductors_index={}

#below function to identify each lines and to identify elements.
def parse_each_line(eachline):
    words=eachline.split()
    elementname=words[0]
    from_node=words[1]
    to_node=words[2]
    global nodes
    nodes.append(from_node)
    nodes.append(to_node)
    nodes=list(set(nodes))
    if(words[3]=="dc"):
        words[3]=words[4]
    if(words[3]=="ac"):
        Vmax = float(words[4])/2
        phase = float(words[5])
        real = Vmax*cos(phase)
        imag = Vmax*sin(phase)
        words[3] = complex(real,imag)
    if(words[0][0]=="R" or words[0][0]=="C" or words[0][0]=="I"):
        value=words[3]
        return [ elementname, from_node, to_node, value]
    elif(words[0][0]=="V" ):
        value=words[3]
        global voltage_sources
        voltage_sources.append(words[0])
        global number_of_voltage_sources
        number_of_voltage_sources+=1
        return [ elementname, from_node, to_node, value]
    elif(words[0][0]=="L" ):
        value=words[3]
        global inductors
        inductors.append(words[0])
        global number_of_inductors
        number_of_inductors+=1
        return [ elementname, from_node, to_node, value]

#below function to update matrix M,b.
def update_matrix(circuit_details,M,b):  
    for j in range(len(circuit_details)):
        if(circuit_details[j][0][0]=="R"):
            if(circuit_details[j][1]=="GND"):
                M[nodes_index[circuit_details[j][2]]][nodes_index[circuit_details[j][2]]]+=(1/float(circuit_details[j][3]))
            elif(circuit_details[j][2]=="GND"):
                M[nodes_index[circuit_details[j][1]]][nodes_index[circuit_details[j][1]]]+=(1/float(circuit_details[j][3]))
            else:
                M[nodes_index[circuit_details[j][1]]][nodes_index[circuit_details[j][1]]]+=(1/float(circuit_details[j][3]))
                M[nodes_index[circuit_details[j][2]]][nodes_index[circuit_details[j][2]]]+=(1/float(circuit_details[j][3]))
                M[nodes_index[circuit_details[j][1]]][nodes_index[circuit_details[j][2]]]-=(1/float(circuit_details[j][3]))
                M[nodes_index[circuit_details[j][2]]][nodes_index[circuit_details[j][1]]]-=(1/float(circuit_details[j][3]))
        if(circuit_details[j][0][0]=="V"):
            if(circuit_details[j][1]=="GND"):
                M[nodes_index[circuit_details[j][2]]][len(nodes)+voltage_sources_index[circuit_details[j][0]]]-=1
                M[len(nodes)+voltage_sources_index[circuit_details[j][0]]][nodes_index[circuit_details[j][2]]]+=1
                b[len(nodes)+voltage_sources_index[circuit_details[j][0]]]=(circuit_details[j][3])
            elif(circuit_details[j][2]=="GND"):
                M[nodes_index[circuit_details[j][1]]][len(nodes)+voltage_sources_index[circuit_details[j][0]]]+=1
                M[len(nodes)+voltage_sources_index[circuit_details[j][0]]][nodes_index[circuit_details[j][1]]]-=1
                b[len(nodes)+voltage_sources_index[circuit_details[j][0]]]=(circuit_details[j][3])
            else:
                M[nodes_index[circuit_details[j][2]]][len(nodes)+voltage_sources_index[circuit_details[j][0]]]-=1
                M[len(nodes)+voltage_sources_index[circuit_details[j][0]]][nodes_index[circuit_details[j][2]]]+=1
                M[nodes_index[circuit_details[j][1]]][len(nodes)+voltage_sources_index[circuit_details[j][0]]]+=1
                M[len(nodes)+voltage_sources_index[circuit_details[j][0]]][nodes_index[circuit_details[j][1]]]-=1
                b[len(nodes)+voltage_sources_index[circuit_details[j][0]]]=(circuit_details[j][3])
        if(circuit_details[j][0][0]=="I"):
            if(circuit_details[j][1]=="GND"):
                b[nodes_index[circuit_details[j][2]]]+=(circuit_details[j][3])
            elif(circuit_details[j][2]=="GND"):
                b[nodes_index[circuit_details[j][1]]]-=(circuit_details[j][3])
            else:
                b[nodes_index[circuit_details[j][2]]]+=(circuit_details[j][3])
                b[nodes_index[circuit_details[j][1]]]-=(circuit_details[j][3])
        if(circuit_details[j][0][0]=="L"):
            if(freq==0):
                if(circuit_details[j][1]=="GND"):
                    M[nodes_index[circuit_details[j][2]]][len(nodes)+len(voltage_sources)+voltage_sources_index[circuit_details[j][0]]]-=1
                    M[len(nodes)+len(voltage_sources)+voltage_sources_index[circuit_details[j][0]]][nodes_index[circuit_details[j][2]]]+=1
                elif(circuit_details[j][2]=="GND"):
                    M[nodes_index[circuit_details[j][1]]][len(nodes)+len(voltage_sources)+voltage_sources_index[circuit_details[j][0]]]+=1
                    M[len(nodes)+len(voltage_sources)+voltage_sources_index[circuit_details[j][0]]][nodes_index[circuit_details[j][1]]]-=1
                else:
                    M[nodes_index[circuit_details[j][2]]][len(nodes)+len(voltage_sources)+voltage_sources_index[circuit_details[j][0]]]-=1
                    M[len(nodes)+len(voltage_sources)+voltage_sources_index[circuit_details[j][0]]][nodes_index[circuit_details[j][2]]]+=1
                    M[nodes_index[circuit_details[j][1]]][len(nodes)+len(voltage_sources)+voltage_sources_index[circuit_details[j][0]]]+=1
                    M[len(nodes)+len(voltage_sources)+voltage_sources_index[circuit_details[j][0]]][nodes_index[circuit_details[j][1]]]-=1
            else:
                if(circuit_details[j][1]=="GND"):
                    M[nodes_index[circuit_details[j][2]]][nodes_index[circuit_details[j][2]]]-=complex(0, 1/(2*np.pi*freq*(float(circuit_details[j][3]))))
                elif(circuit_details[j][2]=="GND"):
                    M[nodes_index[circuit_details[j][1]]][nodes_index[circuit_details[j][1]]]-=complex(0, 1/(2*np.pi*freq*(float(circuit_details[j][3]))))
                else:
                    M[nodes_index[circuit_details[j][1]]][nodes_index[circuit_details[j][1]]]-=complex(0, 1/(2*np.pi*freq*(float(circuit_details[j][3]))))
                    M[nodes_index[circuit_details[j][2]]][nodes_index[circuit_details[j][2]]]-=complex(0, 1/(2*np.pi*freq*(float(circuit_details[j][3]))))
                    M[nodes_index[circuit_details[j][1]]][nodes_index[circuit_details[j][2]]]+=complex(0, 1/(2*np.pi*freq*(float(circuit_details[j][3]))))
                    M[nodes_index[circuit_details[j][2]]][nodes_index[circuit_details[j][1]]]+=complex(0, 1/(2*np.pi*freq*(float(circuit_details[j][3]))))
        if(circuit_details[j][0][0]=="C"):
            if(circuit_details[j][1]=="GND"):
                M[nodes_index[circuit_details[j][2]]][nodes_index[circuit_details[j][2]]]+=complex(0, 2*np.pi*freq*(float(circuit_details[j][3])))
            elif(circuit_details[j][2]=="GND"):
                M[nodes_index[circuit_details[j][1]]][nodes_index[circuit_details[j][1]]]+=complex(0, 2*np.pi*freq*(float(circuit_details[j][3])))
            else:
                M[nodes_index[circuit_details[j][1]]][nodes_index[circuit_details[j][1]]]+=complex(0, 2*np.pi*freq*(float(circuit_details[j][3])))
                M[nodes_index[circuit_details[j][2]]][nodes_index[circuit_details[j][2]]]+=complex(0, 2*np.pi*freq*(float(circuit_details[j][3])))
                M[nodes_index[circuit_details[j][1]]][nodes_index[circuit_details[j][2]]]-=complex(0, 2*np.pi*freq*(float(circuit_details[j][3])))
                M[nodes_index[circuit_details[j][2]]][nodes_index[circuit_details[j][1]]]-=complex(0, 2*np.pi*freq*(float(circuit_details[j][3])))

#if len(sys.argv)<2 then entire information(either .netlist or file name) is not provided.        
if(len(sys.argv)==2):
    #below try-except to read lines of circuit and identify all elements.
    try:
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
                elif(ac==line[:len(ac)]):
                    freq = float(line.split()[2])
            if(start>=end or count!=2):
                print("INVALID CIRCUIT DEFINITION")
                sys.exit()
            lines_of_circuit_details = lines[start+1:end]
            circuit_details=[parse_each_line(line) for line in lines_of_circuit_details]

            #I want to take matrix for nodes except GND.so i elemenated GND from nodes.
            nodes.remove("GND")
            dimension=0
            dc=False 

            #finding dimensions of matrix
            if(freq==0):
                dc=True
                dimension=number_of_voltage_sources+len(nodes)+number_of_inductors
            else:
                dimension=number_of_voltage_sources+len(nodes)
            
            #Making matrix M,b with all entries as "0+0j"
            M=np.zeros((dimension,dimension),dtype=complex)
            b=np.zeros(dimension,dtype=complex)

            #Making nodes dictionary
            for index,node_name in enumerate(nodes):
                nodes_index[node_name]=index

            #Making voltage dictionary
            for index,voltage_sources_name in enumerate(voltage_sources):
                voltage_sources_index[voltage_sources_name]=index
            
            #Making inductors dictionary
            for index,inductor_name in enumerate(inductors):
                inductors_index[inductor_name]=index
            update_matrix(circuit_details,M,b)
            print("Matrix M is","\n",M)
            print("Matrix b is","\n",b)
            #solving matrix
            try:
                x = np.linalg.solve(M,b)    
            except Exception:
                print('ERROR(cannot calculate inverse of matrix).')
                sys.exit()
            print("The voltage at node GND is 0j")

            #printing final voltages and currents through voltage sources and current through inductors.
            for i in nodes:
                print("The voltage at node {} is {}".format(i,x[nodes_index[i]]))
            for j in voltage_sources:
                print('The current through source {} is {}'.format(j,x[len(nodes)+voltage_sources_index[j]]))
            
            #current through inductors will be taken into account only when voltage is DC
            if (dc):
                for i in inductors:
                    print("The current through inductor {} is {}".format(i,x[len(nodes)+len(voltage_sources)+inductors_index[i]]))
    except IOError:
        print("Given file does not exist. ERROR in file name")
else:
    sys.exit("Invalid number of arguments! Pass the netlist file as the second argument.")