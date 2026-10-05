import os
import time
import logging
import subprocess

# 1. Configure Logging for the Automation Tool itself
logging.basicConfig(
    filename='infra_automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 2. Define target files and keywords (Simulating an Engineering App log)
TARGET_LOG_FILE = "engineering_app.log"
CRITICAL_KEYWORD = "CRITICAL_ERROR_SERVICE_HANG"

# Simulate creating a dummy log file if it doesn't exist
if not os.path.exists(TARGET_LOG_FILE):
    with open(TARGET_LOG_FILE, 'w') as f:
        f.write("System initialized.\n")

def trigger_self_healing():
    """
    Simulates a self-healing action by executing an OS-level restart command.
    In production, this would be a systemctl command or a secure remote script.
    """
    logging.warning("Initiating automated self-healing protocol...")
    print("[!] Critical error detected! Attempting recovery...")
    
    try:
        # Simulating restarting a service safely. 
        # Replace 'echo' command with actual administrative commands like 'systemctl restart service_name'
        result = subprocess.run(
            ["echo", "Restarting Engineering Application Service..."], 
            check=True, 
            stdout=subprocess.PIPE, 
            text=True
        )
        logging.info(f"Self-healing output: {result.stdout.strip()}")
        logging.info("Service successfully recovered.")
        print("[+] Recovery action completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Self-healing failed: {e}")
        print("[-] Automated recovery failed. Manual intervention required.")

def monitor_log():
    """
    Monitors the end of a log file dynamically (similar to 'tail -f' in Linux).
    """
    print(f"[*] Starting infrastructure monitor on {TARGET_LOG_FILE}...")
    logging.info("Log monitoring service started.")
    
    with open(TARGET_LOG_FILE, 'r') as file:
        # Move the file pointer to the end of the file so we only read new lines
        file.seek(0, os.SEEK_END)
        
        while True:
            line = file.readline()
            if not line:
                # Wait briefly for new log inputs to prevent high CPU utilization
                time.sleep(1)
                continue
            
            # Process the log line
            line = line.strip()
            if CRITICAL_KEYWORD in line:
                logging.error(f"Alert triggered by log line: {line}")
                trigger_self_healing()

if __name__ == "__main__":
    try:
        monitor_log()
    except KeyboardInterrupt:
        print("\n[*] Monitoring service stopped by administrator.")
        logging.info("Log monitoring service stopped by administrator.")

