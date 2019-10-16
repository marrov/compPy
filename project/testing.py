import pandas as pd

s = pd.Series(range(4), index=['a', 'b', 'c', 'd'])


def read_log(dir):
    idx = 0
    with open(dir, 'r') as reader:
        for line in reader:
            # Discard first line
            if idx != 0:
                # Define strings which signal the function and the time
                str_func = '...'
                str_time = 'Done in '

                # Extract the function and time based on the strings above
                lin_func = line[0:line.find(str_func)]
                lin_time = line[line.find(str_time)+len(str_time):-3]

                # If strings are not empty write function and time in data
                if not lin_func and not lin_time:
                    pass
                else:
                    data = [lin_func, lin_time]
            idx += 1
    return data

# YOU ARE OVERRRIDING DATA!!!

# Define directory for log files
dir = 'project/logs/log.run_np_1'

data = read_log(dir)

print(data)
