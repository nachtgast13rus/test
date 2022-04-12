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
# my_list = [["Albert", "Collins", 3.02], ["Albert", "Nelson", 3.02], ["Cole", "Allen", 3.03]]
# my_list.sort(key=lambda x:(-x[2], x[0]))
# print(my_list)
# walks = [
#     {"day": "Monday", "distance": 2000},
#     {"day": "Tuesday", "distance": 3000},
#     {"day": "Wednesday", "distance": 3500},
#     {"day": "Thursday", "distance": 2500},
#     {"day": "Friday", "distance": 2500},
#     {"day": "Saturday", "distance": 1000},
#     {"day": "Sunday", "distance": 5600}]
# print(sum(walk.get('distance') for walk in walks) // len(walks))
result = 0
cards = {"Ace": 14, "King": 13, "Queen": 12, "Jack": 11}
hand = [input() for _ in range(6)]
for i in hand:
    if i in cards:
        result += cards[i]
    else:
        result += int(i)
print(result / 6)