from collections import Counter
def find_duplicate_employees(emps_id):
    counts = Counter(emps_id)
    duplicates = []

    for emp_id, frequency in counts.items():
        if frequency > 1:
            duplicates.append(emp_id)
            return duplicates
        
if __name__ == "__main__":
    roster = [2,3,5,2,3,6,4,9,8]
    print(find_duplicate_employees(roster))
   