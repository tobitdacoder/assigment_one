'''The final grades for Programming Methods course unit are recorded in a file final.txt. Write a Python program that reads the grades from the file final.txt and analyzes grades by determining the average grade, the number of grades above the average and the modal grade.'''

finalG=open("gradesList.txt","r")

content=finalG.read()
print(content)

finalG.close()

