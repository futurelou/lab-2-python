# Author: Louis Constable lzc5535@psu.edu
# Collaborator:Christian Torres ckt5298@psu.edu
# Collaborator:Sydney Wetzel skw5571@psu.edu
# Section: 7
# Breakout: 8

def getlettergrade(grade): 
  if grade >= 93.0 :
   return "A"
  elif grade >= 90.0 :
   return "A-"
  elif grade >= 87.0 :
   return "B+"
  elif grade >= 83.0 :
   return "B"
  elif grade >= 80.0 :
   return "B-"
  elif grade >= 77.0 :
   return "C+"
  elif grade >= 70.0 :
   return "C"
  elif grade >= 60.0 :
   return "D"
  elif grade > 60.0 :
   return "F"
   


def run():
  grade = input ("Enter your CMPSC 131 grade: ")
  
  print (f"Your letter grade for CMPSC 131 is {getlettergrade(float(grade))}.")

if __name__ == "__main__":
   run()
