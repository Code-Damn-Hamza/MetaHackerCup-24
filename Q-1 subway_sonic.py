def solve():
    T = int(input()) 
    for t in range(1, T + 1):
        N = int(input())  
        min_speed = 0  
        max_speed = float('inf')  
        
        for i in range(1, N + 1):
            A, B = map(int, input().split())
            
            if B == 0:
                print(f"Case #{t}: -1") 
                return

            min_speed = max(min_speed, i / B)
            
            if A > 0: 
                max_speed = min(max_speed, i / A)

        if min_speed > max_speed:
            print(f"Case #{t}: -1")
        else:
            print(f"Case #{t}: {min_speed:.6f}") 

solve()
