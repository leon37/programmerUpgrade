'''
author:leon
project:programmerUpgrade
date:2022/12/6
email:13368447@qq.com
'''
#! python3

# 传递任意数量的实参

# def makePizza(*toppings):
#     print(toppings)

# makePizza('pepperoni')
# makePizza('mushrooms', 'green peppers', 'extra cheese')

# 结合使用位置实参和任意数量实参

# def makePizza(size, *toppings):
#     print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')
#     for topping in toppings:
#         print('- ' + topping)

# makePizza(16, 'pepperoni')
# makePizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用任意数量的关键字实参

# def buildProfile(first, last, **user_info):
#     profile = {}
#     profile['firstName'] = first
#     profile['lastName'] = last
#     for k, v in user_info.items():
#         profile[k] = v
#     return profile


# user_profile = buildProfile(
#     'albert', 'einstein', location='princeton', field='physics')
# print(user_profile)
