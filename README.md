# Ingredients_Compare
Ingredients_Compare runs a comparison on the ingredients between two separate files. This was written to compare ingredients between Branded Food Ingredients and recipe ingredients.


#Installation instructions:
Python 3.10 is required to run this program.


#Requirements
1. In order to run this program, you must first download the necessary python files. These include branded_food_count.py, branded_food_sort.py, ingredientCompare.py, recipes_count.py, recipes_sort.py, and master.py. The master.py file is the only file that needs to be run.

2. In order to run this program, you must have two csv files you need to compare the ingredients in: 1 file labeled branded_food.csv and 1 file labeled recipes.csv. In the recipes.csv, ingredients must be listed in the 2nd column. In the branded_food.csv, ingredients must be listed in the sixth column. 
#Note: Next step in the program is to specify a file name and column number to enter; however, they must currently have the names listed above, or can be changed in the files. These filenames are listed in branded_food_sort.py line 16 and recipes_sort.py line 16. The column numbers are listed in the same files, line 20.

3. In the command prompt, run the command 'python master.py', making sure all other python files and csv files are in the same directory


#Output
There are several files returned from this. They are listed below:
branded_foodparsed.txt - this file contains partially sorted branded food ingredients used for further in the program

recipes_parsed.txt - same as file above but for recipes

branded_food-full.txt - this file contains the fully sorted branded food ingredients

recipes_full.txt - same as file above but for recipes

branded_foodcounts.csv - this file contains how frequently every ingredient occurs

recipecounts.csv - same as file above but for recipes

branded_food-mostfrequent.txt - contains the most frequently occurring values in branded_foods (values that occur more than 25000 times. Can be changed in branded_food_count.py line 36)

recipes-mostfrequent.txt - contains the most frequently occurring values in recipes (values that occur more than 1000 times. Can be changed in recipes_count.py line 36)

commonlist.txt - A list of all ingredients in common between the initial recipes.csv file and branded_food.csv file.

commonlist-mostfrequent.txt - Same as above, but only for the most frequently occurring ingredients.

diffbrandlist.txt - A list of all ingredients unique to the branded_food.csv file.

diffbrandlist-mostfrequent.txt - Same as above, but only for the most frequently occurring ingredients. 

diffrecipelist.txt - A list of all ingredients unique to the recipes.csv file. 

diffrecipelist-mostfrequent.txt - Same as above, but only for the most frequently occurring ingredient. 


#Disclaimer
All files are currently working as expected. However, it is not very user-friendly and more work is being done to correct that problem. Future updates should expect to include a filename to specify, include column numbers to specify, and run the calculation on how to do the most frequently occurring ingredients in the program (which would include specifying how frequently is wanted). In the current state of the program, all of this is hard-coded, but see above where to change each metric. 
