from library_app.reservation import view_reservations

def reports_menu(report, reservations):
    while True:
        print("1: View Reservations")
        print("2: Overdue Reports")
        print("3: Members With Overdue Books")
        print("4: Exit")

        selection = input("Please select report type: ")
        
        # Pulls report information from Mich'as reservation file
        if selection == "1":
            view_reservations(reservations)

        # Pulls overdue_reports from my book_status file
        elif selection == "2":
            print(f"Overdue books: {report.overdue_count()}")

        elif selection == "3":
            members = report.overdue_members()

            if not members:
                print("No members have overdue books currently.")
            else:
                print("Members with overdue book:")

                for member in members:
                    print(f"- {member}")

        elif selection == "4":
            break

        else:
            print("Invalid selection. Please select 1 thru 4.")