# cap = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
#
#
# def please_conform(cap):
#     # start is used to determine the start position of the intervals.
#     # forward is to count the number of heads in the interval.
#     # backward is to count the number of tails in the interval.
#
#     start = forward = backward = 0
#     interval = []
#
#     for i in range(1, len(cap)):
#         if cap[start] != cap[i]:
#             interval.append([start, i - 1, cap[start]])
#             if cap[start] == 'F':
#                 forward += 1
#             else:
#                 backward += 1
#             start = i
#     interval.append([start, len(cap) - 1, cap[start]])
#     if cap[start] == 'F':
#         forward += 1
#     else:
#         backward += 1
#
#     ''' Notice that the code below only check the number of intervals, and not the number of F or B.'''
#     if forward < backward:
#         flip = 'F'
#     else:
#         flip = 'B'
#     for t in interval:
#         if t[2] == flip:
#             print('People in positions ', t[0],
#                   'through ', t[1], 'flip your caps!')
#
#
# please_conform(cap)
#
#
# def list_conacetenate(cap):
#     cap = cap + ['END']
#     print(cap)
#
# capA = ['f','f','b']
# list_conacetenate(capA)
# print(capA)
#
# def list_append(cap):
#     cap.append('End')
#     print(cap)
# list_append(capA)
# print(capA)

##########################################################################################
##############################One Pass Algorithm- Code Optimized #########################
my_cap = ['h','h','t','t','t','h','t','t','h']
def pleaseConformOnepass(caps):
    if len(caps) > 0:
        caps = caps + [caps[0]]
        for i in range(1, len(caps)):
            if caps[i] != caps[i-1]:
                if caps[i] != caps[0]:
                    print('People in positions', i, end='')
                else:
                    print(' through', i-1, 'flip your caps!')
    else:
        return print('No Caps!')
pleaseConformOnepass(my_cap)