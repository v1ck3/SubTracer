import subprocess
import os
import sys
import time
import pyfiglet
import json

# Print tool header
def print_banner():
    result = pyfiglet.figlet_format("SubTracer", font="standard")
    print(result)
    print("Subdomain Enumeration started")
    print("Copyright - MR SUDO (since 2022)\n")
    print("<====== ONGOING ======>")
    time.sleep(2)

def run_sublist3r_script(domain):
    """Runs Sublist3r from the cloned GitHub repository to enumerate subdomains."""
    sublist3r_dir = './Sublist3r'  # Ensure Sublist3r repo is in the same directory as this script
    sublist3r_script = 'sublist3r.py'
    
    if not os.path.exists(os.path.join(sublist3r_dir, sublist3r_script)):
        print(f"Sublist3r repository not found in {sublist3r_dir}. Please clone it first.")
        sys.exit(1)
    
    # Run Sublist3r using subprocess, passing the domain and output file location
    print(f"Running SubTracer for {domain}...")
    try:
        # Execute Sublist3r's script using subprocess
        result = subprocess.run(
            ['python', os.path.join(sublist3r_dir, sublist3r_script), '-d', domain, '-o', 'subdomains.txt'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        
        if result.returncode != 0:
            print(f"Error during subdomain enumeration: {result.stderr.decode('utf-8')}")
            return None
        
        # Parse and return the subdomains
        with open('subdomains.txt', 'r') as file:
            subdomains = file.readlines()
            subdomains = [sub.strip() for sub in subdomains]
            return subdomains
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python SubTracer.py <domain>")
        sys.exit(1)
    
    domain = sys.argv[1]
    
    # Print banner and start the enumeration
    print_banner()
    start_time = time.time()
    
    subdomains = run_sublist3r_script(domain)
    
    if subdomains:
        print(f"\nFound {len(subdomains)} subdomains for {domain}:")
        for sub in subdomains:
            print(sub)
    else:
        print(f"\nNo subdomains found for {domain}.")
    
    print(f"\nEnumeration completed in {time.time() - start_time:.2f} seconds.")
    print (f"\nSaved subdomains to subdomains.txt !!!")

if __name__ == "__main__":
    main()
