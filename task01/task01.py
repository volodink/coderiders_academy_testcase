import random
import sort

random_list = [random.randint(-10, 10) for _ in range(25)]

print(f'Random list =>               {random_list}')
print(f'Sorted random list =>        {sorted(random_list)}')
print(f'Quick sort implementation => {sort.qsort(random_list)}')
