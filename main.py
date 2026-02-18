import os
import sys
import subprocess

def main():
    print("=======================================================")
    print("   E-commerce Intelligent Systems Analysis Project")
    print("=======================================================")
    print("Select an action:")
    print("1. Check Project Status")
    print("2. Run Real-time Stream Simulation (Kafka)")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == '1':
        print("\n--- Checking Files ---")
        # Check for data
        if os.path.exists('ecommerce_data.csv'):
            print("✅ Data file 'ecommerce_data.csv' found.")
        else:
            print("❌ Data file missing. Please open 'analysis.ipynb' and run the Data Generation cells.")
            
        # Check for Docker config
        if os.path.exists('docker-compose.yml'):
            print("✅ Docker configuration found.")
        else:
            print("❌ 'docker-compose.yml' missing.")
            
        print("\nTo see the analysis and model, open 'analysis.ipynb' in Jupyter.")

    elif choice == '2':
        print("\n--- Starting Stream Simulation ---")
        if not os.path.exists('ecommerce_data.csv'):
            print("Error: Data file missing. Cannot stream.")
            return

        print("Note: Ensure Docker is running (docker-compose up -d) before proceeding.")
        try:
            # Runs the stream_simulation.py script using the current Python interpreter
            subprocess.run([sys.executable, 'stream_simulation.py'])
        except KeyboardInterrupt:
            print("\nSimulation stopped by user.")
        except Exception as e:
            print(f"Error running simulation: {e}")

    elif choice == '3':
        print("Goodbye!")
        
    else:
        print("Invalid choice. Please run the script again.")

if __name__ == "__main__":
    main()
