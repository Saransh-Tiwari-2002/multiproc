import multiprocessing
from multiprocessing import Pool, Process
import random
import time


def main_worker(my_list):
    new_list = random.sample(range(10000, 99999), 1000)
    return new_list

def indirect_worker(count, arg):
    t = time.time()
    results = []
    for i in range(count):
        results.append(main_worker(arg[i]))
    print(f"Process completed in : {time.time() - t}")


if __name__ == "__main__":
    num_proc = 8
    length = 80000
    num_args = length//num_proc
    args = [random.sample(range(10000, 99999), length)] * length
    p = Pool(num_proc)

    t = time.time()
    p.map(main_worker, args)
    print(f'Pool completed in : {time.time() - t}')

    processes = []
    for i in range(8):
        # In this, i * num_args is the starting index and i * num_args + num_args is the ending index of arguments for
        # to provide to this process
        processes.append(Process(target=indirect_worker, args=(num_args, args[i * num_args:i * num_args + num_args])))
        processes[-1].start()

    for process in processes:
        process.join()