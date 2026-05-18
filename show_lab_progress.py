import time
import sys
import os

# ANSI Color codes for a pretty terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(f"{Colors.HEADER}{Colors.BOLD}==================================================")
    print("      ROSETTA STONE AI - DEVOPS LAB PROJECT      ")
    print(f"=================================================={Colors.ENDC}\n")

def simulate_pipeline(include_push=True):
    stages = [
        ("1. Source Code Checkout", "Fetching from GitHub (main branch)..."),
        ("2. Code Quality Analysis", "Running SonarCloud Scanner (Project: Plutoaintaplanet_hocr)..."),
        ("3. Vulnerability Scanning", "Running Trivy Docker (Image: ghcr.io/aquasecurity/trivy:canary)..."),
        ("4. Docker Image Build", "Executing: docker build -t hocr-app:latest ."),
    ]
    
    if include_push:
        stages.append(("5. Docker Hub Push", "Pushing to: hub.docker.com/r/plutoaintaplanet/hocr-app..."))
    else:
        stages.append(("5. Docker Hub Push", "SKIPPED - As per Second Pipeline requirements."))
        
    stages.extend([
        ("6. Public Cloud Deployment", "Triggering Render Webhook... SUCCESS"),
        ("7. GitHub Push Trigger", "Webhook received! Pipeline automation complete.")
    ])

    print(f"{Colors.CYAN}{Colors.BOLD}Starting Pipeline: {'FULL (With Push)' if include_push else 'NO-PUSH VERSION'}{Colors.ENDC}\n")
    
    for i, (name, detail) in enumerate(stages, 1):
        timestamp = time.strftime("%H:%M:%S")
        
        # Skip simulation if it's the "skipped" step
        is_skipped = not include_push and "SKIPPED" in detail
        
        if is_skipped:
            print(f"[{timestamp}] {Colors.WARNING}[SKIP]{Colors.ENDC} {name}")
            print(f"    -> {detail}\n")
            time.sleep(0.5)
            continue

        print(f"[{timestamp}] {Colors.BLUE}[RUNNING]{Colors.ENDC} {name}...", end="\r")
        time.sleep(1.5) # Simulate work
        
        print(f"[{timestamp}] {Colors.GREEN}[SUCCESS]{Colors.ENDC} {name}")
        print(f"    -> {detail}\n")
        time.sleep(0.5)

    print(f"{Colors.GREEN}{Colors.BOLD}Pipeline execution finished successfully!{Colors.ENDC}")
    input("\nPress Enter to return to menu...")

def main_menu():
    while True:
        clear_screen()
        print_header()
        print(f"{Colors.BOLD}Select Pipeline Timeline to Demonstrate:{Colors.ENDC}")
        print(f"{Colors.GREEN}1. First Pipeline (Complete 7 Steps - With Docker Push){Colors.ENDC}")
        print(f"{Colors.BLUE}2. Second Pipeline (6 Steps - WITHOUT Docker Push){Colors.ENDC}")
        print(f"{Colors.CYAN}3. View Project Deliverables Summary{Colors.ENDC}")
        print(f"{Colors.FAIL}4. Exit Presentation{Colors.ENDC}")
        
        choice = input(f"\n{Colors.BOLD}Enter choice (1-4): {Colors.ENDC}")
        
        if choice == '1':
            clear_screen()
            print_header()
            simulate_pipeline(include_push=True)
        elif choice == '2':
            clear_screen()
            print_header()
            simulate_pipeline(include_push=False)
        elif choice == '3':
            clear_screen()
            print_header()
            with open('README_SUBMISSION.md', 'r') as f:
                print(f.read())
            input("\nPress Enter to return to menu...")
        elif choice == '4':
            print(f"\n{Colors.CYAN}Exiting Lab Presentation. Good luck!{Colors.ENDC}")
            break
        else:
            print(f"{Colors.FAIL}Invalid choice. Try again.{Colors.ENDC}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
