# 56. Merge Intervals

# 1е рабочее решение
def merge(intervals):
    if intervals and len(intervals) > 1:
            intervals.sort(key=lambda x: x[0])
            result = [intervals[0]]
    else:
        return intervals

    for interval in intervals[1:]:
        if result[-1][1] >= interval[0] and interval[1] >= result[-1][1]:
            result[-1][1] = interval[1]
        elif interval[1] < result[-1][1]:
            continue
        else:
            result.append(interval)
    
    return result 
    





# print(merge([[1,3],[8,10],[2,6],[15,18]]))
# print(merge([[1,4],[0,4]]))