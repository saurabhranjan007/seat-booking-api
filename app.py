from flask import Flask, jsonify
from icecream import ic 


app = Flask(__name__)
app.debug = True

@app.route("/", methods=['GET'])
def home():
    return jsonify(message="App is running"), 200 

seats = [[0]*7 for i in range(10)]
@app.route("/booking/<num_seats>", methods=['POST'])
def book_seats(num_seats):
    ic(f'Inside <book_seats>. Seats to be booked: {num_seats}')
    ic(f'Total seats: {seats}')
    
    try:
        num_seats = int(num_seats)
        booked_seats = []
        for i in range(len(seats)):
            j = 0
            while j < 7:
                if seats[i][j] == 0:
                    consecutive_seats = 1
                    for k in range(1, num_seats):
                        if j+k < 7 and seats[i][j+k] == 0:
                            consecutive_seats += 1
                        else:
                            break
                    if consecutive_seats == num_seats:
                        for k in range(num_seats):
                            seats[i][j+k] = 1
                            booked_seats.append((i*7)+j+k+1)
                        return booked_seats
                    else:
                        j += consecutive_seats
                else:
                    j += 1
                    
        for i in range(len(seats)):
            j = 0
            while j < 7:
                if seats[i][j] == 0:
                    nearby_seats = 1
                    for k in range(1, num_seats):
                        if j+k < 7 and seats[i][j+k] == 0:
                            nearby_seats += 1
                        else:
                            break
                    if nearby_seats == num_seats:
                        for k in range(num_seats):
                            seats[i][j+k] = 1
                            booked_seats.append((i*7)+j+k+1)
                        return booked_seats
                    else:
                        j += nearby_seats
                else:
                    j += 1
        return jsonify(message="Sorry, the coach is full."), 200 
    
    except Exception as err:
      print('An exception occurred', str(err))
      return jsonify(error=f'{err}'), 400 
