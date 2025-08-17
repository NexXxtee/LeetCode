# def solve(misspelled_names: list) -> list:
#     if len(misspelled_names) == 1:
#         return misspelled_names

#     result = []
#     temp = {}

#     for i in range(len(misspelled_names)):
#         s = "".join(sorted(misspelled_names[i]))
#         if s not in temp:
#             temp[s] = 1
#             result.append(misspelled_names[i])
#         else:
#             continue 



#     return result



# print(solve(["vlad", "avld", "almas", "aslam", "aya", "ayan"]))
# print(solve(["vlad", "avld","dwasdw" "almas", "aslam", "aya", "ayan"]))
# print(solve(["vlad", "avld","adlv", "dwasdw" "almas", "aslam", "aya", "ayan"]))


for i in range(6):
    print(i)