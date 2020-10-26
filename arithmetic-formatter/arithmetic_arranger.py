def arithmetic_arranger(problems, *args):
    k = 4
    if(len(args)==1):
      k = 5
    
    #too many problems verify    
    if(len(problems)>5):
      return "Error: Too many problems."
    pad = [0] * 5
    # Assertion
    for i in range(len(problems)):
        temp = problems[i].split(" ")
        if(temp[0].isdigit()==False or temp[2].isdigit()==False):
          #sys.exit("Error: Numbers must only contain digits.")
          return "Error: Numbers must only contain digits."
        if(temp[1]!="+" and temp[1]!="-"):
          return "Error: Operator must be '+' or '-'."
        if(len(temp[0]) > 4 or len(temp[2]) > 4 ):
          return "Error: Numbers cannot be more than four digits."
        if(len(temp[0])>=len(temp[2])):
          pad[i] = len(temp[0]) + 2 
        else:
          pad[i] = len(temp[2]) + 2
    c1=""
    c2=""
    c3=""
    c4=""
    for i in range(k):
      if (i==1):
        continue
      for j in range(len(problems)):
        temp = problems[j].split(" ")
        if(i==0):
         padstr1 = temp[i].rjust(pad[j], ' ')
         if(j==len(problems)-1):
           c1 = c1 + padstr1
         else:
           c1 = c1 + padstr1 + "    "
        elif(i==3):
         padstr3 = "".rjust(pad[j],'-') 
         if (j == len(problems)-1):
             c3 = c3 + padstr3
         else:
             c3 = c3 + padstr3 + "    "
        elif(i==2):
         padstr2 = temp[2].rjust(pad[j]-2, ' ') 
         if (j == len(problems)-1):
             c2 = c2 + temp[1] + " " + padstr2
         else:
             c2 = c2 + temp[1] + " " + padstr2 + "    "
        elif(i==4):
         if(temp[1]=="-"):
          padstr4 = str(int(temp[0])-int(temp[2])).rjust(pad[j], ' ')
         else:
          padstr4 = str(int(temp[0])+int(temp[2])).rjust(pad[j], ' ')
         if(j==len(problems)-1):
            c4 = c4 + padstr4
         else:
            c4 = c4 + padstr4 + "    "
          

      print("")
    if(k==5):
     arranged_problems = c1 + "\n" + c2 + "\n" + c3 + "\n" + c4
     print(arranged_problems, end="")
    else: 
     arranged_problems = c1 + "\n" + c2 + "\n" + c3
     print(arranged_problems, end="")
      
    return arranged_problems
