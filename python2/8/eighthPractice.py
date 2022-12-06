'''
author:leon
project:programmerUpgrade
date:2022/12/6
email:13368447@qq.com
'''


# 8-12
# def sandwich(*topping):
#     print(*topping)
#
#
# sandwich('1')
# sandwich('1', '2')
# sandwich('1', '2', '3')


# 8-13
# def buildProfile(first, last, **user_info):
#     profile = {}
#     profile['firstName'] = first
#     profile['lastName'] = last
#     for k, v in user_info.items():
#         profile[k] = v
#     return profile
#
#
# print(buildProfile('Li', 'Tao', age=26, sex='male'))

# 8-14
def makeCar(brand, model, **carInfo):
    car = {'brand': brand, 'model': model}
    for k, v in carInfo.items():
        car[k] = v
    return car


print(makeCar('subaru', 'outback', color='blue', towPackage=True))
