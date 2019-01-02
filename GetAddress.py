#!/usr/bin/python3
# coding=utf-8
__author__ = 'zhongyujian'

import json


def get_address():
    """
    给出一个身份证，或者前几位号码，给出所在地的省市县
    :return:
    """
    input_number = input("请输入身份证号码前六位号码查询所在地(输入数字大于两位):")

    def print_error_msg():
        print("请检查输入号码是否正确！")

    def check_input_length(number):
        """
        检查识别号码的长度
        :param number:
        :return:
        """
        number = str(number)
        if len(number) < 2:
            print("输入身份证号码不足两位！请重新输入！")
        elif 2 <= len(number) < 4:
            return 2
        elif 4 <= len(number) < 6:
            return 4
        elif len(number) >= 6:
            return 6

    def print_card_adrress(input_number):
        length = check_input_length(input_number)
        tp = load_cardArr()
        if length == 2:
           num = str(input_number)[0:2]
           dt = tp['two_digit_number']
           if num in dt:
               print(dt[num])
           else:
               print_error_msg()
        elif length == 4:
            num = str(input_number)[0:4]
            dt = tp['four_digit_number']
            if num in dt:
                print(dt[num])
            else:
                print_error_msg()
        else:
            num = str(input_number)[0:6]
            dt = tp['six_digit_number']
            if num in dt:
                print(dt[num])
            else:
                print_error_msg()

    def load_cardArr():
        with open("content.json", 'rb') as f:
            temp = json.loads(f.read())
            return temp

    try:
        print_card_adrress(input_number)
    except KeyError:
        print_error_msg()


if __name__ == '__main__':
    get_address()

    # fp = open('content.json', encoding='gb18030', errors='ignore')
    # data = json.load(fp)

    # print(data['two_digit_number'])
    with open("content.json", 'rb') as f:
        temp = json.loads(f.read())
        # print(temp)
        # print(temp['two_digit_number'])
        # print(temp['two_digit_number'])
        # print(temp['four_digit_number'])
        # print(temp['six_digit_number'])
        # print(temp['two_digit_number']['11'])
        # print(type(temp['two_digit_number']))

