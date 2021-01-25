from cumulative_timer import CumulativeTimer
import math

def timed_function():
    sum = 0.0
    x = 2.0
    for cnter in range(0,202000):
        sum += math.sqrt(sum) + x
        sum = math.sqrt(sum)


overall_timer = CumulativeTimer()
overall_timer.start()

timer = CumulativeTimer()
for index in range(0,100):
    timer.start()

    timed_function()
    
    timer.stop(f"Index {index}")
    
timer.finish()

overall_timer.stop()

