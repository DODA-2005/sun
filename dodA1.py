import pickle

def new_customer():
    while True:
        with open('telephone.dat', 'ab') as file:
            phone = int(input('Enter phone num: '))
            name = input('Enter name: ')
            ctype = input('Enter connection type: ')
            customer_data = [phone, name, ctype]
            pickle.dump(customer_data, file)

            ans = input('Add more? (yes/no): ')
            if ans.lower() != "yes":
                break

def display():
    with open('telephone.dat', 'rb') as f:
        while True:
            try:
                data = pickle.load(f)
                print('Phone:', data[0])
                print('Name:', data[1])
                print('Connection Type:', data[2])
                print('*****')
            except EOFError:
                print('End of file')
                break

new_customer()
display()
