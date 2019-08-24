'''
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
* record(order_id): adds the order_id to the log
* get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N. You should be as efficient with time and space as possible.
'''

orderLog = []
N = 5


def record(order_id):
    if len(orderLog) == N:
        orderLog.pop(0)
    orderLog.append(order_id)
    

def get_last(i):
    if i<=N and i<=len(orderLog):
        print(orderLog[i-1])
    elif i>len(orderLog):
        print("Position exceeds the number of orders recorded ({})!".format(len(orderLog)))
    elif i>N:
        print("Position exceeds the maximum number of orders ({})!".format(N))


def showLog():
    print("{}/{} last orders: ".format(len(orderLog), N))
    for i,ID in enumerate(orderLog):
        print("ID #{}: {}".format(i+1, ID))




if __name__ == "__main__":
    while True:
        print("\n----------------\n1: Record\n2: Get last\n3: Show log\n4: Exit")
        choice = input("Enter your choice... ")        

        if choice == 1:
            order_id = input("Enter the order ID: ")
            record(order_id)        

        elif choice == 2:
            i = input("Enter the position: ")
            get_last(i)        

        elif choice == 3:
            showLog()
        
        elif choice == 4:
            break