import random as rand
from numpy import random #pip install numpy

# print(random.random()) # 0~1 random float
# uniform distribution 
# random variable

# 사람은 모든 나이때 죽을 확률이 0.01
# 초기 인구: 남자 500명 여자 500명
# 100년 시뮬레이션
SIGMA = 20
female_life = 86.4
male_life = 80.6

year = 2025
male = [] # [[age, death_age], .... ]
for i in range(100):
    person = []
    person.append(i)
    person.append(random.normal(loc=male_life, scale=SIGMA))
    male.append(person)

female = [] # [[age, death_age], .... ]
for i in range(100):
    person = []
    person.append(i)
    person.append(random.normal(loc=female_life, scale=SIGMA))
    female.append(person)



def get_death_age(sex):
    global male_life
    global female_life
    global SIGMA    
    if sex == "m": # or "f"
        return random.normal(loc=male_life, scale=SIGMA)

    else:
        return random.normal(loc=female_life, scale=SIGMA)

## TODO 23.03
# way 1: (easy) 평균 아이 낳는 나이를 가져와서, 적절한 sigma 임의로 부여해서 위에처럼 normal
# way 2: internet에서 real distribution (data가져오기만 하자. 대신, 이거 택하면 위에 death age도 비슷한 데이터 가져와야함)
def probability_to_give_birth(age):
    return 0.0047/2



while year < 2124:
    print(f"Simulating year: {year}")

    male_survivor=[]
    female_survivor=[]
    for x in male:
        if x[1] > x[0]+1:
            x[0]+=1
            male_survivor.append(x)
    
    for x in female:
        if x[1] > x[0]+1:
            x[0]+=1
            female_survivor.append(x)
    
    for p_mom in female_survivor:
        if rand.random() < probability_to_give_birth(p_mom):
            if rand.random() <0.51:
                male_survivor.append([0,get_death_age('m')])
            else:
                female_survivor.append([0,get_death_age('f')])



    print(f"Male Survivors: {len(male)}")
    print(f"Female Survivors: {len(female)}")
    ###
    year += 1
    male = male_survivor
    female = female_survivor
