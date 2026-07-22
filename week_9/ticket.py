def create_ticket():
    print("=== IT Helpdesk Ticket ===")

    student_name = input("Student Name: ")
    student_id = input("Student ID: ")
    issue = input("Issue: ")
    location = input("Location: ")
    priority = input("Priority (High/Medium/Low): ").strip().capitalize()

    if priority not in ("High", "Medium", "Low"):
        print("Invalid priority level. Please enter High, Medium, or Low.")
        return None

    # Assign technician based on priority level
    if priority == "High":
        technician = "Ahmad"
    elif priority == "Medium":
        technician = "Siti"
    else:
        technician = "Ali"

    return (
        student_name,
        student_id,
        issue,
        location,
        priority,
        technician,
        "Pending"
    )