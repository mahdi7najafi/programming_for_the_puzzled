sched = [
    (6, 8), (6, 12), (6, 7), (7, 8),
    (7, 10), (8, 9), (8, 10), (9, 12),
    (9, 10), (10, 11), (10, 12), (11, 12)
]
#print("Start, ", sched[0][0])
#print("Start, ", sched[0][1])



# Each corresponds to a celebrity that comes at a time and then leave at another time.

def celebrityDensity(schedule, start, end):
    count = [0] * (end + 1)
    print(count)
    for i in range(start, end + 1):
        count[i] = 0
        for c in schedule:
            if c[0] <= i < c[1]:
                count[i] += 1
    print(count)
    return count


def bestTimeToAttendParty(schedule):
    start = schedule[0][0]
    end = schedule[0][0]
    for c in schedule:
        start = min(c[0], start)
        end = max(c[1], end)
    count = celebrityDensity(schedule, start, end)
    print("second",count)
    maxCount = 0

    for i in range(start, end + 1):
        if count[i] > maxCount:
            maxCount = count[i]
            time = i

    print("Best time to attend the party is at : ",
          time, 'o\'clock', ':', maxCount,
          'celebrities will be attending!')


bestTimeToAttendParty(sched)


#################################################   Smarter way of doing the above

sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0),
          (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0),
          (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]


def best_time_to_party(sched):
    time = []
    for c in sched:
        time.append((c[0], 'start'))
        time.append((c[1], 'end'))
    sortlist(time)
    maxcount, t = chooseTime(time)
    print('Best time to attend the party is at',
          t, 'o\'clock', ':', maxcount,
          'celebrities will be attending!')


def sortlist(time):
    # This is a Selection Sort Algorithm.
    for i in range(len(time) - 1):
        min_idx = i
        for j in range(i, len(time)):
            if time[min_idx][0] > time[j][0]:
                min_idx = j
        time[min_idx], time[i] = time[i], time[min_idx]
def chooseTime(times):
    rcount = 0
    maxcount = time = 0
    for t in times:
        if t[1] == 'start':
            rcount = rcount + 1
        elif t[1] == 'end':
            rcount = rcount - 1
        if rcount > maxcount:
            maxcount = rcount
            time = t[0]
    return maxcount, time



best_time_to_party(sched2)







########################################################Selection Sort Algorithm
# A = [2, 4, 1, 3, 5, 6, 7, 19, 12, 8, 9, 10, 20]
#
# def selection_sort(arr):
#     for i in range(len(arr) - 1):
#         min_idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#
# selection_sort(A)
# print(A)


