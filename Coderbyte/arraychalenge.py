arr  = [5,2,4,6]
i =0
moving_avg =[]
window_size =arr[0]
while i < len(arr) - window_size  + 1:
    this_window =arr[i : i + windpw_size]
    window_avg = sum(this_window)/ window_size
    moving_avg.append(window_avg)
    i= i+ 1
print(moving_avg)
    

