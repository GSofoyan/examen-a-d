
def analyze_numbers(numbers: list):
    som=0
    for n in range(0,len(numbers)):
        som+=numbers[n]
    gem= som/len(numbers)
    count = 0
    for i in range(len(numbers)):
        if numbers[i] > gem:
            count += 1
    print(f"Average is {gem}")
    print(f"Number of elements above the average is {count}")

analyze_numbers([1,2,3,4,5,6,7,8,9,10])
