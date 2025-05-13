import random
import string
import sys

def generate_ec2_names():
    # Step 1 – Get user input
    num_instances = int(input("How many EC2 instance names do you need? "))
    department = input("Enter your department name: ")

    # Step 2 – Normalize and validate department
    allowed_departments = ["marketing", "accounting", "finops"]
    normalized_dept = department.strip().lower()

    if normalized_dept not in allowed_departments:
        print(f"\n🚫 '{department}' is not authorized to use this EC2 name generator.")
        print("✅ Allowed departments: Marketing, Accounting, or FinOps")
        sys.exit(1)

    # Step 3 – Generate EC2 names
    print("\n✅ Generated EC2 Names:\n")
    for _ in range(num_instances):
        rand_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        ec2_name = f"{normalized_dept}-{rand_suffix}"
        print(ec2_name)

# Call the function
generate_ec2_names()





