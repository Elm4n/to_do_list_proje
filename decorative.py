import time
def run_time(f):
    def wrapper(n):
        start_time = time.time()
        result = f(n)
        end_time = time.time()
        execution_time = end_time - start_time
        print(execution_time)
        return result
    return wrapper
@run_time
def create_list(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers

if __name__ == "__main__":
    n = int(input("Enter n : "))
    result = create_list(n)
    print(result)


