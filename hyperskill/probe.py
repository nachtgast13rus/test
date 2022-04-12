# class Robot:
#     def __init__(self, name, variety):
#         self.name = name
#         self.variety = variety
#         print("Robot")
#
#     def get_info(self):
#         return "{} is a {} robot".format(self.name, self.variety)
#
#
# class ServiceRobot(Robot):
#     def __init__(self, name):
#         super().__init__(name, 'service')
#
#
# chappi = ServiceRobot("Chappi")
# print(chappi.get_info())
# class NegativeSumError(Exception):
#     def __init__(self):
#         super().__init__()
#
#
# def sum_with_exceptions(a, b):
#     if (a + b) < 0:
#         raise NegativeSumError
#     else:
#         print(a + b)
my_list = [["Albert", "Collins", 3.02], ["Albert", "Nelson", 3.02], ["Cole", "Allen", 3.03]]
my_list.sort(key=lambda x:(-x[2], x[0]))
print(my_list)