import os
import re

REPORTS_DIR = "reports"

# Keywords for severity detection
SERIOUS = ["stroke", "heart attack", "severe", "icu", "unconscious", "critical", "broken"]
MODERATE = ["fever", "cough", "pain", "infection", "shortness of breath"]
MINOR = ["mild", "stable", "normal", "headache", "cold"]

def sanitize_filename(name):
    """Make a safe filename from patient name."""
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9 _-]", "", s)        # keep only safe chars
    s = re.sub(r"\s+", "_", s)                # spaces -> underscores
    return s or "patient"

def list_reports():
    """Show all reports in folder"""
    files = [f for f in os.listdir(REPORTS_DIR) if f.endswith(".txt")]
    if not files:
        print("No reports found.")
    else:
        for i, f in enumerate(files, 1):
            print(f"{i}. {f}")
    return files

def read_report(filename):
    """Read the content of a report file"""
    with open(os.path.join(REPORTS_DIR, filename), "r") as file:
        return file.read()

def analyze_report(text):
    """Check severity based on keywords"""
    text_lower = text.lower()
    if any(word in text_lower for word in SERIOUS):
        return "Serious"
    elif any(word in text_lower for word in MODERATE):
        return "Moderate"
    else:
        return "Minor"

def add_new_report():
    """Create a new patient report in the format:
       Patient: <name>
       Age: <age>
       Symptoms: <text>
    """
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    name = input("Patient name (e.g. Sneha Pillai): ").strip()
    if not name:
        print("Patient name is required.")
        return

    # Age input
    age = input("Age (enter number or leave blank): ").strip()
    if age:
        try:
            int(age)  # check if number
        except ValueError:
            print("Age should be a number. Saving as entered.")

    # Symptoms (multi-line until END)
    print("Enter Symptoms (type END on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    symptoms = " ".join([ln.strip() for ln in lines]).strip()
    if not symptoms:
        symptoms = "Not specified."

    # Prepare filename
    base = sanitize_filename(name)
    filename = f"{base}.txt"
    path = os.path.join(REPORTS_DIR, filename)
    counter = 1
    while os.path.exists(path):
        filename = f"{base}_{counter}.txt"
        path = os.path.join(REPORTS_DIR, filename)
        counter += 1

    # Save file
    content = f"Patient: {name}\nAge: {age}\nSymptoms: {symptoms}\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Report saved as: {filename}")
    print("Preview:\n" + content)

def single_report_analysis():
    """Analyze one chosen report"""
    files = list_reports()
    if not files:
        return
    filename = input("Enter exact report filename: ").strip()
    if filename not in files:
        print("File not found.")
        return
    text = read_report(filename)
    result = analyze_report(text)
    print(f"\nReport: {filename} → Condition is **{result}**\n")

def all_reports_analysis():
    """Analyze all reports in folder"""
    files = list_reports()
    if not files:
        return
    print("\n--- All Reports Analysis ---")
    for f in files:
        text = read_report(f)
        result = analyze_report(text)
        print(f"{f}: {result}")
    print("-----------------------------\n")

def analyze_menu():
    """Submenu for analysis"""
    while True:
        print("\n--- Analyze Reports ---")
        print("1. Single Report Analysis")
        print("2. All Reports Analysis")
        print("3. Back to Main Menu")
        choice = input("Choose option: ")

        if choice == "1":
            single_report_analysis()
        elif choice == "2":
            all_reports_analysis()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

def main():
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    while True:
        print("\n=== Medical Report Manager ===")
        print("1. List reports")
        print("2. Read a report")
        print("3. Add new report")
        print("4. Analyze reports")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            list_reports()

        elif choice == "2":
            files = list_reports()
            if files:
                num = int(input("Enter report number: ")) - 1
                if 0 <= num < len(files):
                    print("\n" + read_report(files[num]) + "\n")
                else:
                    print("Invalid selection.")

        elif choice == "3":
            add_new_report()

        elif choice == "4":
            analyze_menu()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
