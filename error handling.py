# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as ex:
#         return ex
#     except:
#         print('unknow error occured')


# print(divide(4, 2))
# # print(divide(4, 0))
# print(divide(int(input()), input()))


# file = None
# try:
#     file = open(r'C:\tmp\fdgfdg.txt')
#     data = file.read()
# except FileNotFoundError as ex:
#     print(ex.strerror)
# else:
#     print('maybe else')
# finally:
#     print('finally')
#     if file:
#         file.close()

def get_int():
    while True:
        try:
            reply = int(input('Enter a number'))
            return reply
        except:
            print('Repeat, please')
            continue
print(get_int())