from ticket import create_ticket
from display import display_ticket

def main():
    ticket = create_ticket()
    if ticket is not None:
        display_ticket(ticket)
    else:
        print("Ticket creation cancelled or failed.")

if __name__ == "__main__":
    main()