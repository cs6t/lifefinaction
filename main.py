import random
import time

content = [
    "You’ve been meaning to stop buying lottery tickets, but on the way back from the gas station you picked one up "
    "and won $5! Seems like the habit pays for itself, and then some. You’re tempted to stop by and grab some "
    "more next time you swing by – after all, there’s always the chance you get lucky and make it big.",

    "Vegas is a haze of neon lights and smoke, of cheap alcohol and cheaper cigarettes, and everywhere the whir and "
    "buzz of gambling. You’re at a roulette wheel, stewing in your own anxiety. You’d managed to win $1500 on a lucky "
    "hand in blackjack, but you’ve already lost 600 at the wheel. You’ve bet on black three times, and it’s come up "
    "red three times. You run the math in your head: there’s a 1/2 chance of red each time, right? To come up red four "
    "times in a row, that’d be a 1/16 chance, right? As long as you bet on black next round, you’ve got a 15/16 "
    "chance of winning!.",

    "You noticed that $700 was deducted from your bank account – you had expected a $200 hit, for a plane ticket to "
    "visit your friends in Colorado. You called the airline’s helpdesk, and after a long and therapeutic bout of "
    "swearing quietly at their hold music, you found that you were accidentally scheduled for a $500 trip to "
    "California as well, on the same weekend. You’d really wanted to visit your friends – plus, Colorado is nicer "
    "this time of year anyway – but it would be irresponsible to waste $500 by not taking the more "
    "expensive trip, right?"
]


income = 5000
net_worth = 50000
flags = []


class RandomEvent:
    def __init__(self, income_effect, nw_effect1, nw_effect2, content1, content2, add_flag, check_flag):
        self.income_effect = income_effect
        self.nw_effect1 = nw_effect1
        self.nw_effect2 = nw_effect2
        self.content1 = content1
        self.content2 = content2
        self.add_flag = add_flag
        self.check_flag = check_flag


a = RandomEvent(-200, -50, -50, "you adopted a cat!", "even though you already have a dog, you got a cat", "cat", "dog")
b = RandomEvent(200, 0, 0, "you got a promotion!", "", "promotion", "")
c = RandomEvent(0, -800, -200, "you had to fix your car.", "your car broke, but you had insurance", "carfix", "carins")
d = RandomEvent(-200, -50, -50, "you adopted a dog!", "even though you already have a cat, you got a dog", "dog", "cat")
e = RandomEvent(-500, -200, -200, "you started taking music lessons", "", "music", "")
f = RandomEvent(-30, 4, 4, content[0], "", "smallcosts", "")
g = RandomEvent(0, -500, -500, content[1], "", "gambling", "")
h = RandomEvent(0, -700, -700, content[2], "", "sunkcost", "")

event_list = [a, b, c, d, e, f, g, h]

while True:
    event = event_list[random.randint(0, len(event_list)-1)]
    if event.check_flag != "" and event.check_flag in flags:
        print(event.content2)
        net_worth = net_worth + event.nw_effect2
    else:
        print(event.content1)
        net_worth = net_worth + event.nw_effect1
    if event.add_flag not in flags:
        flags.append(event.add_flag)

    income = income + event.income_effect
    print(income)
    print(net_worth)
    net_worth = net_worth + income
    input()
