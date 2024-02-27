n = int(input()) 
array = list(map(int, input().split())) 
q = int(input()) 

# Предварительно вычисляем префиксные суммы
curr_sum_to_prefix = [0] * (n + 1) 
for i in range(1, n + 1): 
    curr_sum_to_prefix[i] = curr_sum_to_prefix[i - 1] + array[i - 1] 

for z in range(q): 
    left, right = map(int, input().split()) 
    
    # Вычисляем сумму элементов от left до right включительно
    sum_left_right = curr_sum_to_prefix[right] - curr_sum_to_prefix[left - 1] if left > 0 else curr_sum_to_prefix[right]
    
    print(sum_left_right)