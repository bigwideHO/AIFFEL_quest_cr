class Kiosk:
    def __init__(self):
        self.menu_list = ['americano', 'latte', 'mocha', 'yuza_tea', 'green_tea', 'choco_latte']
        self.price_list = [2000, 3000, 3000, 2500, 2500, 3000]

    def menu_print(self):
        for i in range(len(self.menu_list)):
            print(i+1, '.', self.menu_list[i], self.price_list[i],'원')

    def menu_select(self):
        self.num = int(input("주문하실 음료의 번호를 입력해주세요: "))
        self.order_menu = []
        self.order_price = []
        t = 0

        while t != 1 and t != 2:
            if self.num >= 1 and self.num <= 6:
                t = int(input("HOT을 원하시면 1, ICE를 원하시면 2를 입력해주세요: "))
                if t == 1:
                    temp = 'HOT'
                elif t == 2:
                    temp = 'ICE'
                else: 
                    print("잘못된 숫자를 입력하였습니다. 다시 입력해주세요.")
                    continue
            else:
                print("잘못된 숫자를 입력하였습니다. 다시 입력해주세요.")
                continue

            self.order_menu.append(self.menu_list[self.num-1])
            self.order_price.append(self.price_list[self.num-1])
            self.total = 0
            self.total += sum(self.order_price)

            print('주문하신 음료 ▶ ', temp, self.menu_list[self.num-1], self.price_list[self.num-1], '원')

            self.gopay = int(input("계속 주문을 원하시면 주문하실 음료 번호를, 결제를 원하시면 0을 눌러주세요: "))
            if self.gopay >= 1 and self.gopay <= 6:
                self.num = self.gopay
                t = 0
                continue
            elif self.gopay == 0:
                print(self.order_menu, self.order_price, self.total, '원')
                print("결제 화면으로 이동합니다.")
            else:
                print("잘못된 숫자를 입력하였습니다. 다시 입력해주세요.")
                t = 0

    def pay(self):
        while True:
            self.mean = input("현금일 경우 \'cash\' 또는 1을, 카드일 경우 \'card\' 또는 2를 입력하세요.")
            if self.mean == 'cash' or self.mean == '1':
                print('직원을 호출하겠습니다. 잠시만 기다려주세요.')
                break
            elif self.mean == 'card' or self.mean == '2':
                print('IC칩의 방향을 올바르게 하여 카드를 넣어주세요.')
                break
            else:
                print("잘못된 결제수단 입니다. 다시 입력해주세요.")
                continue
        print("결제가 완료되었습니다. 이용해 주셔서 감사합니다.")

    def table(self):
        print('⟝' + '-' * 30 + '⟝')
        for i in range(5):
            print('|' + ' ' * 31 + '|')
        for i in range(len(self.order_menu)):
            print((' ' * 2) + self.order_menu[i] + str(self.order_price[i]) + (' ' * 2))
        print(' ' * 12 + str(self.total) + ' ' * 12)
        for i in range(5):
            print('|' + ' ' * 31 + '|')
        print('⟝' + '-' * 30 + '⟝')


a = Kiosk()
a.menu_print()
a.menu_select()
a.pay()
a.table()