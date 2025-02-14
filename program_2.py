# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many
# tickets are desired for each movie.
# At the end of the program it prints out the total number of tickets desired by the user.
# Use either a "for loop" or "while loop" to accomplish this.
def main():
    movie = True
    ticket = 0
    while movie == True:
        movie_names = str(input("What movie would you like too see?: "))
        ticket_cost = int(input("How many tickets would you like to but?: "))
        ticket_total= ticket + ticket_cost
        another_movie = input("Would you like to see another movie (Y/N): ")
        if another_movie == "Y":
            movie = True
        else:
            movie = False
        return ticket_total

if __name__ == '__main__':
        ticket_price = main()
        print(f"Number of Tickets: {ticket_price}")
