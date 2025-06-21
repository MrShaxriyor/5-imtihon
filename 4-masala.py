import threading
import random
import time

def rson_chiqarish(nomi):
    time.sleep(random.uniform(0.1, 1.0))
    son = random.randint(1, 100)
    print(f"{nomi} {son}")

threadlar = []


for i in range(1, 11):
    t = threading.Thread(target=rson_chiqarish, args=(f"Thread-{i}",))
    threadlar.append(t)
    t.start()

for t in threadlar:
    t.join()

print("son chiqarish tugadi")
