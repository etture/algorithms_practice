# Basic imports --------------------------------------------
from __future__ import annotations                         
import sys                                                 

sys.setrecursionlimit(10**6)
from os.path import dirname, abspath, basename, normpath   
root = abspath(__file__)                                   
while basename(normpath(root)) != 'algo_practice':           
    root = dirname(root)                                   
sys.path.append(root)                                      
from utils.Tester import Tester, Logger                    
logger = Logger(verbose=False)                             
# ----------------------------------------------------------

from collections import Counter

def solution(string):
    def check_scatter_palindrome(substr):
        even = len(substr) % 2 == 0
        cntr = Counter(substr)
        if even:
            if num_odds(cntr.values()) == 0:
                return True
            return False
        else: # odd
            if num_odds(cntr.values()) == 1:
                return True
            return False

    def num_odds(sequence):
        odds = 0
        for num in sequence:
            if num % 2 == 1:
                odds += 1
        return odds
    
    # start_idx, end_idx = 0, 1
    num_scatter_palindromes = 0
    for start in range(len(string)):
        for end in range(start+1, len(string) + 1):
            # print(f'substr: {string[start:end]}, start: {start}, end: {end}')
            if check_scatter_palindrome(string[start:end]):
                # print('         YES!')
                num_scatter_palindromes += 1
    return num_scatter_palindromes


'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output
test_cases = [
    (['aabb'], 9),
    (['bbrrg'], 12),
    (['babaggllrnrvinmvdimduurrtntcbtnttocbbtobckwckwbxbxppuueehhccoowwuuuxeuxnnencncypvygpckvgvckmvmvgavgajjaaiiooururxbullrlrxbvohgapulfwlrlvoahgappffmwrmapfkmgwmkgfwchfchqqzeoozueoonuniiuucrcrcmtcammuhmtarmsmuhhrrmvsxhrjmsyvufxepjsnyzuwfeapnzvqwmavqbjhmbwjyjhpwtjyptwwbwbzwznehsohlnehsbsoihblssfcbgboibseffzixnbgcbpgoefzixxfnbgzphxfzzyhzykekekfkfeaeazfijcvgzofuaxisjufckvvgouavrxecsjvugfytkvvmrecpwjevjsmgyvstobmprzpwedfjszmqpvjusobbprzwlwwdfzqooxpijikuydfbwlwwouwuidonmxiifkypttpmdifoutwwituigidbnmfftpwttpmjiovxtwniltengibwhftewrjmvxnfleswqnwhejrmeftswjqjetjwicgaqwiwxucczjgaoqwbxmekauyczjobibreemeaeqbhkaybftisreoeiaeqbahsftskudowmliasxhkujdwmdlxhjdxxukuykyqbmqdoifhlsibmbvbsxgadoifhldjosypihabsvkblnrzsxgvadsfjpoayfpqvxhayjsklnxrcczvtguseefjpmavhfqovsxyjtxccftgxuejejmpuymcvhostfmxiwjpuymcmfjiwfjrotroihgtcyihgecxfgyefxfgjpggfcgfegjqjhgbmpxxwgjcfeqgwjanjvqhgbmxxwpjqwijanvpitthhrriqxiqwxwddhhbzbzhuehuelulkukmmbcbbzsohicapbksmznsohhkxgiqapkdzisbksmnhhnkklxbtoamgqdhzainbkisshnklwbtloacalrmhanilswloac'], 9820),
    (['qoqcoqscfoqxiacorxkdsrcffyxiuxjarxkidrpnfyrpugmhsxprzjhpliponrppgmhspfrzhfpgslkolqvzthfknpslcffgsklqrkvjzthpifknrseqlcrmksfkotomljpinrteqsymskxeasofmootwjomdlbwzvnltsysyxmeadomoqoclcwjdhbwyqwfbrdyazcenvdtlymdqocwlchyqrkwfvbewwzrdcypadnhzcszendttwyzrkvfdewwzcpdgnboghzzxsztayzfdguyboqfgzxaucpayfqofcpogjabfoskogwqtdjbsmkcwsrqoitdekimccsrzoihekinlcddgkztphncvlddsfmgktpcvsfxzmxzaeaaledoavohalxmedondayuhevfmohxkkmkeendrypufhjvzefdemfkmkaktlberajpfgejikevvzexvdkszefpwmatqlwwbdgsaojjlhgvxeiketveexvlkshzpwwqwwdglbqesojlqqhnvxtelhdxdzfwylbqeqqndbxdbhwdxzzkfyfbbiahgxwdwbiewhcwxxiziybpakbfioaisgxnpwaubkkaieowhnacwxkioiybpabkuijoiyusnpaqubkckaeoonakokiwuijodeyfixsxszuqbpcytehcoirbwodefveixsxvdruxxwszqfpythcrbgwdviexqevdeqruuznlxmwrqzkfkgwdmeiqdeequznqlslmrzkekmedqslgofrnzegopbbqfrvhjnzppbibqvtvhlqjjbpiwdrtgwlvlgzqljabwhqdregwlgzlahqhehhuhuoojjrcrfcpcfecpeagagppfffofowwsbslzjblhznfjnhntfneteasasitilnwvhtlnzjwvhestztyjeoystavtxdnyroplyavxdnrplwgnwowrgnjbworxjbooxouohulhluussddaaaaqaqtajtvjvfznrfzxnrx'], 3048),
]

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(input[0])
    ).run()
