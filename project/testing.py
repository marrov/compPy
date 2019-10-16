import pandas as pd

def read_log_list(dir):
    """
    Reads log files at given directory and returns relevant time data in list
    """
    data=[]
    with open(dir, 'r') as reader:
        for line in reader:
            # Define strings which signal the function and the time
            str_func = '...'
            str_time = 'Done in '
            # If line includes the strings write function and time in data
            if str_func in line and str_time in line:
                # Extract function and time based on the strings above
                lin_func = line[0:line.find(str_func)]
                lin_time = line[line.find(str_time)+len(str_time):-3]
                # Append to list
                data.append([lin_func, lin_time])
    return data


def read_log_dict(dir):
    """
    Reads log files at given directory and returns relevant time data in dictionary
    """
    data = {'function':[],'time':[]}
    func = []
    time = []
    with open(dir, 'r') as reader:
        for line in reader:
            # Define strings which signal the function and the time
            str_func = '...'
            str_time = 'Done in '
            # If line includes the strings write function and time in data
            if str_func in line and str_time in line:
                # Extract function and time based on the strings above
                func.append(line[0:line.find(str_func)])
                time.append(float(line[line.find(str_time)+len(str_time):-3]))
    data = dict(zip(func, time))
    return data

# OK I GOT IT!!! MAKE TO FUNCS
# 1) READ_LOG_KEYS which reads the funcs
# 2) READ_LOG_VALS which reads the times, which get concatenated

# Define directory for log files
dir1 = 'project/logs/log.run_np_1'
dir2 = 'project/logs/log.run_np_2'

d1 = read_log_dict(dir1)
d2 = read_log_dict(dir2)

z = {**d1, **d2}

#df = pd.DataFrame(data=d1)
#df = pd.DataFrame(data=d['time'],index=d['function'])

print(z)
