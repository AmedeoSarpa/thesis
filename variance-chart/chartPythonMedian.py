"""
Graph to print the variance chart and compute standard deviation and median for each sp category
"""
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import re 
class UserStory :
       def __init__(self,title,sp,effort,sprint) :
              self.bad_estimated  = False
              self.title = title
              self.sp = sp
              self.effort = effort
              self.sprint = sprint

       def checkEstimation(self,std,median) :
              if self.effort > median+std :
                     self.bad_estimated = True
                     print("User story - ",self.title,' - of sprint',self.sprint,'was overestimated, estimation was:',self.sp)
                     return True
              if self.effort < median-std :
                     self.bad_estimated = True
                     print("User story - ",self.title,'of sprint',self.sprint,'was underestimated, estimation was:',self.sp)
                     return True
              return False              

if __name__ == '__main__' :
       #NUMBER OF THE CURRENT SPRINT
       analyzed_sprint = 8
       #MODIFY THE VALUE ABOVE 

       number_of_bad_estimations = 0
       total_number_of_stories = 0
       sp_list = [] #x-axis of the diagram
       effort_list = [] #y-axis of the diagram
       category = {} #dictionary that keep track of the efforts for each category
       story_list = [] #list of user stories
       category_scale = [1,2,3,5,8,13] #range of possible sp
       # Inizialize the category
       for i in category_scale :
              category[i] = []

       
       fp = open('data.txt','r')
       current_sprint = 1
       sprint_pattern = re.compile('#SPRINT [1-9][0-9]*')

       for line in fp.readlines()[1:] :
              if bool(sprint_pattern.match(line)) :
                     current_sprint = int(line.split('#SPRINT ')[1])
              else :
                     vec = line.split(',')
                     category[int(vec[1])].append(int(vec[2]))
                     sp_list.append(int(vec[1]))
                     effort_list.append(int(vec[2]))
                     story_list.append(UserStory(vec[0],int(vec[1]),int(vec[2]),current_sprint))
                     total_number_of_stories = total_number_of_stories + 1
      

       fig, ax = plt.subplots()
       ax.set_xticks(category_scale)
       ax.set_yticks([0,5,10,15,20,25,30,40,50])
       median_list = [] #median values for each category
       category_list = []
       for sp in category.keys() :
              if len(category[sp]) != 0 : 
                     print('STORY POINTS CATEGORY:',sp) 
                     current_median = np.median(category[sp])
                     current_std_dev = np.std(category[sp])
                     print('std deviation:',current_std_dev)
                     print('median:',current_median)
                     print()
                     ax.vlines(x=sp,ymin=current_median-current_std_dev, ymax=current_median+current_std_dev,colors='green')
                     category_list.append(sp)
                     median_list.append(current_median)


       print()
       print("BAD ESTIMATED STORIES UNTIL SPRINT",analyzed_sprint)
       print()
       for story in story_list :
              median = np.median(category[story.sp])
              std = np.std(category[story.sp])
              if story.checkEstimation(std,median) == True :
                     number_of_bad_estimations = number_of_bad_estimations + 1

       print('Total bad estimated stories',number_of_bad_estimations,'over a total number of stories of:',total_number_of_stories)
       
       ax.plot(category_list,median_list,'ro',label="category's median")
       ax.plot(sp_list, effort_list,'x',label="user story")
       
       ax.legend()
       ax.set(xlabel='User Story', ylabel='Hours effort',
              title='Variance in estimates')
       ax.grid()

       fig.savefig("variance_chart_median.png")
       plt.show()
       
