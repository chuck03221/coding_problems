#!/usr/bin/python3


class gstring:
    def decomp(self,comp_str):
        pos_rear    = comp_str.find("]")
        if pos_rear == -1:
            return comp_str
        pos_front   = comp_str.rfind("[",0,pos_rear)
        pos_digit   = pos_front-1
        n_times_str = ""
        while comp_str[pos_digit].isdigit():
            n_times_str = comp_str[pos_digit]+n_times_str
            pos_digit-=1
        n_times = int(n_times_str)
        return self.decomp(comp_str[0:pos_digit+1]+n_times*comp_str[pos_front+1:pos_rear]+comp_str[pos_rear+1:])


solution = gstring()


test_case1 = ["4[5[2[a]b]c]3[ab]","3[a]4[b]5[c]","4[3[a]3[b]4[c]]","4[a3[z]b2[c]]"]
for test in test_case1:
    print(test)
    print(solution.decomp(test))
