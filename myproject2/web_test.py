import random


def shuffleHongbao(people, money):
        '''
                people:表示人数；
                money: 为红包的总金额，单位为分
        '''

        hongbao = []

        if people == 1:
                m = money/100.0     # 将分转换成元
                hongbao.append(m)
                
        else:
                for i in range(1, people):
                      m = random.randint(1, money-1)
                      money -= m
                      hongbao.append(m/100.0)

                
                hongbao.append(money/100.0)
                                     
                
        return hongbao

def ji(ll):
        num = 0
        for i in ll:
                num += i

        return num
                

if __name__ == '__main__':
        hb = shuffleHongbao(5, 1000)
        random.shuffle(hb)
        print('红包随机分配为：' , hb)

        print('红包总金额为：', ji(hb))
        



                        
            
