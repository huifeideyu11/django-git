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


def jin(x):
        '''
        目的：对于整型列表元素按照由小到大的顺序进行排序
        参数：
             x:是列表，元素必须是整型
        返回值：返回排序后的列表

        '''
        
        for i in range(0, len(x)):
                
                for k in range(1, len(x)-i):
                        
                        if x[k] <= x[k-1]:
                                mx = x[k-1]
                                mi = x[k]
                                x[k] = mx
                                x[k-1] = mi

        return x
                                
                                
                

if __name__ == '__main__':
            
        #hb = shuffleHongbao(5, 1000)
        #random.shuffle(hb)
        
        print('加入分支')        

        x = [1,8,9,5,4,3,99,11,53]
        print(range(0, len(x)))
        print(jin(x))

                        
            
