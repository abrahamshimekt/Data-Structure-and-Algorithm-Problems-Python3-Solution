"""
The problem is to find the total number of seats for ith booking
steps to solve the problem
1.first create booking array to keep track the total number of seats for the ith booking which has
a length of n
2. for each reservation take
bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
[10,45,-10,-20,0,25]
[10,55,45,25,25,50]
for j in range(bookings[i][0],bookings[j][1]+1):
  answer[j] += bookings[i][2]
"""
def corpFlightBookings( bookings, n) :
    seats = [0]*n
    i = 0
    while i < len(bookings):
        for j in range(bookings[i][0]-1,bookings[i][1]):
            seats[j] += bookings[i][2]
            print(seats)
        i +=1
    return seats
print(corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]],5))