#import libraries
import sys, numpy

#get file name from user
fasta_file = sys.argv[1]  #add your file name here or use the next code line
#fasta_file = input("Name of your fasta file: ")

#define a function that creates dna matrix
def read_fasta(fasta_file):
    main_list = []
    with open(fasta_file,"r") as fp:
        lines = fp.readlines()
        for line in lines:  
            if line.startswith('>'):
                pass
            else:
                temp = []
                line = line.rstrip()
                for letter in line:
                    temp.append(letter)
                main_list.append(temp)
        return numpy.array(main_list)


#define a function that creates profile matrix
def profile_matrix(matrix):
    #create dictionary with keys and empty lists
    main_dict= {"A": [], "C": [], "G": [], "T": []}
    print_dict = {"A": "", "C": "", "G": "", "T": ""}
    total_gen = ""
    for x in range(len(matrix)+1):
        temp_dict = {"A":0, "C":0, "G":0, "T":0}

        #find number of letters in each column and create a consensus string and profile matrix
        for y in matrix[:,x]:
            temp_dict[y] += 1
        max_key = max(temp_dict, key=lambda key: temp_dict[key])
        total_gen += max_key
        for key in temp_dict:
            main_dict[key].append(temp_dict[key])
    for key in main_dict:
        for x in main_dict[key]:
            print_dict[key] += str(x) + " "
    #print results
    with open("result.txt", "w") as fp2:

        print(total_gen)
        fp2.write(total_gen + "\n")
        for key in print_dict:
            fp2.write(key + " " + print_dict[key] + "\n")
            print("{}: {}".format(key, print_dict[key]))
    

profile_matrix(read_fasta(fasta_file))



