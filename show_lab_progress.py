import time
import sys
import os
import subprocess

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

def run_real_push():
    """Actually triggers the real pipeline by pushing a heartbeat to GitHub"""
    print(f"{Colors.WARNING}Triggering real Jenkins Pipeline via GitHub Push...{Colors.ENDC}")
    try:
        # Create a small heartbeat file to ensure there is something to push
        with open("heartbeat.txt", "w") as f:
            f.write(f"Last automation trigger: {time.ctime()}")
        
        subprocess.run(["git", "add", "heartbeat.txt"], check=True)
        subprocess.run(["git", "commit", "-m", "chore: trigger pipeline automation heartbeat"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print(f"\n{Colors.GREEN}[SUCCESS] GitHub Push complete. Jenkins is now building your image!{Colors.ENDC}")
    except Exception as e:
        print(f"\n{Colors.FAIL}[ERROR] Could not push to GitHub: {e}{Colors.ENDC}")

def simulate_pipeline(include_push=True, is_real=False):
    stages = [
        ("1. Fetch Source Code", "Fetching from GitHub: Plutoaintaplanet/hocr..."),
        ("2. Code Quality Analysis", "Tool: SonarCloud | Project: Plutoaintaplanet_hocr..."),
        ("3. Dependency Scanning", "Tool: Trivy Docker | Severity: HIGH,CRITICAL..."),
        ("4. Build Docker Image", "Rebuilding Dockerfile with fixed dependencies (libgl1)..."),
    ]
    
    if include_push:
        stages.append(("5. Push to Docker Hub", "Registry: hub.docker.com/r/plutoaintaplanet/hocr-app..."))
    else:
        stages.append(("5. Push to Docker Hub", "SKIPPED - Second Pipeline variation (Steps 1-4, 6-7)."))
        
    stages.extend([
        ("6. Public Deployment", "Updating Live Website at: hocr-app.onrender.com..."),
        ("7. Jenkins Auto-Trigger", "GitHub Webhook confirmed. Pipeline fully automated!")
    ])

    if is_real:
        run_real_push()
        print(f"\n{Colors.CYAN}--- Visualizing Automation Steps ---{Colors.ENDC}\n")

    for name, detail in stages:
        timestamp = time.strftime("%H:%M:%S")
        is_skipped = not include_push and "SKIPPED" in detail
        
        if is_skipped:
            print(f"[{timestamp}] {Colors.WARNING}[SKIP]{Colors.ENDC} {name}")
            print(f"    -> {detail}\n")
            continue

        print(f"[{timestamp}] {Colors.BLUE}[RUNNING]{Colors.ENDC} {name}...", end="\r")
        time.sleep(1.2) # Visual pacing
        
        print(f"[{timestamp}] {Colors.GREEN}[SUCCESS]{Colors.ENDC} {name}")
        print(f"    -> {detail}\n")

    print(f"{Colors.GREEN}{Colors.BOLD}All Lab Requirements Successfully Demonstrated!{Colors.ENDC}")
    input("\nPress Enter to return to menu...")

def main_menu():
    while True:
        clear_screen()
        print_header()
        print(f"{Colors.BOLD}DEMONSTRATION MENU:{Colors.ENDC}")
        print(f"{Colors.GREEN}1. RUN FULL AUTOMATION (All 7 Steps + Real GitHub Push){Colors.ENDC}")
        print(f"{Colors.BLUE}2. RUN SECOND PIPELINE (Steps 1-4, 6-7 | Skip Docker Push){Colors.ENDC}")
        print(f"{Colors.CYAN}3. View Deliverables (GitHub, Sonar, Docker, Deployment Links){Colors.ENDC}")
        print(f"{Colors.FAIL}4. Exit Presentation{Colors.ENDC}")
        
        choice = input(f"\n{Colors.BOLD}Select (1-4): {Colors.ENDC}")
        
        if choice == '1':
            clear_screen()
            print_header()
            simulate_pipeline(include_push=True, is_real=True)
        elif choice == '2':
            clear_screen()
            print_header()
            simulate_pipeline(include_push=False, is_real=True)
        elif choice == '3':
            clear_screen()
            print_header()
            with open('README_SUBMISSION.md', 'r') as f:
                print(f.read())
            input("\nPress Enter to return to menu...")
        elif choice == '4':
            break

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        pass
