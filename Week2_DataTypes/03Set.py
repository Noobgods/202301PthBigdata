s1 = {1, 2, 3}
s2 = set([1,2,3])

# 집합자료형의 특징
# - 중복을 허용하지 않는다.
# - 집합 자료형은 순서가 없다.

set1 = set([2, 3, 5, 7])
set2 = set([0, 2, 4, 6, 8])

# 교집합
set1 & set2     # == set1.intersection(set2)

# 합집합
set1 | set2     # == set1.union(s2) 

# 차집합
set2 - set1     # == set2.difference(set1)


# 관련 함수