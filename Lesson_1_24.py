import os 

for i in range(100 + 1):
    if i % 2 == 0:
        if not os.path.exists("Lesson_1_24/juft.txt"):
            z = open("Lesson_1_24/juft.txt", "x")
           
        a = open("Lesson_1_24/juft.txt", "a")
        a.write(f"{i} ")
        a.close()   

    else:
        if not os.path.exists("Lesson_1_24/toq.txt"):
            r = open("Lesson_1_24/toq.txt", "x")
           
        c = open("Lesson_1_24/toq.txt", "a")
        c.write(f"{i} ")
        c.close()