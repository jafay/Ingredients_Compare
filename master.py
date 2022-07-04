import os, time
start_time = time.time()
os.system("python recipes_sort.py")
print("1/5 done")
minutes = (time.time() - start_time) / 60
print("Program took", minutes, "minutes to run")

os.system("python recipes_count.py")
print("2/5 done")
minutes = (time.time() - start_time) / 60
print("Program took", minutes, "minutes to run")

os.system("python branded_food_sort.py")
print("3/5 done")
minutes = (time.time() - start_time) / 60
print("Program took", minutes, "minutes to run")

os.system("python branded_food_count.py")
print("4/5 done")
minutes = (time.time() - start_time) / 60
print("Program took", minutes, "minutes to run")

os.system("python compare.py")
print("Program took", time.time() - start_time, "to run")
minutes = (time.time() - start_time) / 60
print("Program took", minutes, "minutes to run")