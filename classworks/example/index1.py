# # # import index2
# # # index1 = 1

# # # print(globals())


# # def run():
# #   print("runs the whole project")

# # if __name__ == '__main__':
# #   run()

# import sys
# print(sys)

# import fractions


# import sys



# import os

# # os.path.join(sys.modules)

# # print(__file__)

# sys.path.append('/Users/jon/Workspace/ai-group/classworks/')
# # print(sys.path)


import os

import sys




filename = 'new_index.py'
file_path = '../modules'


# new_path = os.path.join(file_path, filename)

# print(new_path)



real_path = os.path.abspath(file_path)

import sys

print(real_path)
sys.path.append(real_path)


import new_index





