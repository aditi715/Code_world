def highest_tem(temps):
    if not temps:
        return 0
    
    max_temp = temps[0]

    for t in temps:
        if t > max_temp:
            max_temp = t

    return max_temp

if __name__ == "__main__":
    hourly_log = [20,23,21,22,25,26,29,23]
print(highest_tem(hourly_log)) 


  
