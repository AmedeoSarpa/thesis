from cmath import cos, pi
from math import sqrt


def correlationComputation(matrix,name) :
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        den = sqrt((((a*d)/b)/c))
        val = pi/(1+den)
        coeff = cos(val)
        print(f"{name} correlation coefficient : {coeff:.3f}")

if __name__ == "__main__" :
        
        try:
            fp = open('story-list.csv','r')
        except :
            print("Error opening file")
            
        lines = fp.readlines()[1:]
        matrix_spike = [[0,0],[0,0]]
        matrix_new_func = [[0,0],[0,0]]
        matrix_new_tech = [[0,0],[0,0]]
        for line in lines :
            numbers = line.split(',')
            bad_estimation = int(numbers[6])
            spike = int(numbers[3])
            new_tech = int(numbers[4])
            new_func = int(numbers[5])
            matrix_spike[bad_estimation][spike] = matrix_spike[bad_estimation][spike] + 1
            matrix_new_tech[bad_estimation][new_tech]=matrix_new_tech[bad_estimation][new_tech]+1
            matrix_new_func[bad_estimation][new_func]=matrix_new_func[bad_estimation][new_func]+1
        
        i = 0
        while i < 3 :
            if i == 0:
                correlationComputation(matrix_new_func,'New functionalities')
            elif i == 1:
                correlationComputation(matrix_new_tech,'New technology')
            else :
                correlationComputation(matrix_spike,'Spike')
            i = i+1