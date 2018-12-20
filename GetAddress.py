#!/usr/bin/python3
# coding=utf-8
__author__ = 'zhongyujian'
import cardArr


def get_address():
    """
    给出一个身份证，或者前几位号码，给出所在地的省市县
    :return:
    """
    input_number = input("请输入身份证号码(或前六位号码)查询所在地:")

    def print_error_msg():
        print("请检查输入号码是否正确！")

    def check_length(number):
        number = str(number)
        if len(number) < 6 or len(number) > 18:
            print_error_msg()
        else:
            return number[0:6]

    def print_card_adrress(input_number):
        if input_number.startswith('1'):
            print(cardArr.cardArr_start_by_1[input_number])
        elif input_number.startswith('2'):
            print(cardArr.cardArr_start_by_2[input_number])
        elif input_number.startswith('3'):
            print(cardArr.cardArr_start_by_3[input_number])
        elif input_number.startswith('4'):
            print(cardArr.cardArr_start_by_4[input_number])
        elif input_number.startswith('5'):
            print(cardArr.cardArr_start_by_5[input_number])
        elif input_number.startswith('6'):
            print(cardArr.cardArr_start_by_6[input_number])
        else:
            print(cardArr.qt_cardArr[input_number])

    try:
        number = check_length(input_number)
        if number:
            print_card_adrress(number)
    except KeyError:
        print_error_msg()

if __name__ == '__main__':
    get_address()
