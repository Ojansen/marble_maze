#maze 1 2
#maze 3 4
#maze level 5?

maze1 = [[r,r,r,r,r,r,r,r],
         [r,b,r,b,r,b,b,t1],
         [r,b,r,b,r,b,r,r],
         [r,b,b,b,r,b,r,r],
         [r,r,r,b,r,b,r,r],
         [r,b,b,b,r,b,b,t2],
         [r,b,r,b,b,b,r,r],
         [r,t3,r,r,r,r,r,r]]

maze2 = [[r,r,r,r,r,r,r,r],
         [t4,b,b,b,b,r,b,r],
         [r,r,r,r,r,r,b,r],
         [r,b,b,b,b,b,b,r],
         [r,b,r,r,r,b,r,r],
         [t5,b,r,r,r,b,b,r],
         [r,b,r,b,r,b,b,r],
         [r,r,r,t6,r,r,t7,r]]

maze3 = [[r,t8,r,r,r,r,r,r],
         [r,b,b,b,b,b,b,t9],
         [r,r,r,r,r,r,b,r],
         [r,b,b,b,b,r,b,t10],
         [r,r,r,r,b,r,r,r],
         [r,b,b,b,b,b,b,r],
         [r,g,r,r,b,b,b,t11],
         [r,r,r,r,r,r,r,r]]

maze4 = [[r,r,r,t12,r,r,t13,r],
         [t14,b,r,b,r,r,b,r],
         [r,r,r,b,b,r,r,r],
         [t15,b,b,b,b,b,b,r],
         [r,r,r,r,r,r,b,r],
         [r,b,b,b,b,r,b,r],
         [t16,b,b,r,b,b,b,r],
         [r,r,r,r,r,r,r,r]]

t1 to maze2, (1,1)
t2 to maze2, (1,5)
t3 to maze3, (1,1)
t4 to maze1, (6,1)
t5 to maze1, (6,5)
t6 to maze4, (3,1)
t7 to maze4, (6,1)
t8 to maze1, (1,6)
t9 to maze4, (1,1)
t10 to maze4, (1,3)
t11 to maze4, (1,6)
t12 to maze2, (3,6)
t13 to maze2, (6,6)
t14 to maze3, (6,1)
t15 to maze3, (6,3)
t16 to maze3, (6,6)
