filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
for i in range(len(filenames)):
    if filenames[i][-3:] == "hpp":
        filenames[i] = filenames[i].replace("hpp", "h") 


print(filenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]