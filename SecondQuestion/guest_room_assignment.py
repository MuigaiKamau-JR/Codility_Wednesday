def solution(A):
    # Sort the array to handle guests with smaller constraints first
    A.sort()
    
    num_rooms = 0
    i = 0
    
    while i < len(A):
        # Find the number of guests that can be accommodated in this room
        num_rooms += 1
        room_capacity = A[i]
        
        # Move i to the first guest that does not fit in the current room
        while i < len(A) and A[i] <= room_capacity:
            i += 1
    
    return num_rooms
