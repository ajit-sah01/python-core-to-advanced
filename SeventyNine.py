import multiprocessing

def worker():
    print("Process running")

p = multiprocessing.Process(target=worker)
p.start()
p.join()
