def print_pyramid(n):
    if n == 0:
        return
    print_pyramid(n - 1)  
    for i in range(n):
        print("!", end= "")
    print("")
    
if __name__ == "__main__":
    print_pyramid(4)
