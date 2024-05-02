# ================= Question 1 ===================
import random
mood = ["happy", "sad", "energetic", "calm"]
days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

for i in range(len(days)):
    print("on",  days[i], "you were feeling", random.choice(mood))


# ================ Question 2 =================

import random
mood = ["happy", "sad", "energetic", "calm"]
days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
tod = ["morning", "afternoon", "evening"]

for i in range(len(days)):
    print("on",  days[i], random.choice(tod), "you were feeling", random.choice(mood))
