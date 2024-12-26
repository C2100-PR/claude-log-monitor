import os
import time
import glob
from pathlib import Path

def follow_logs(log_path_pattern, num_lines=20):
    """
    Follow logs in real-time, similar to 'tail -f' command
    
    Args:
        log_path_pattern (str): Pattern to match log files
        num_lines (int): Number of historical lines to show initially
    """
    # Expand user path and glob pattern
    expanded_path = os.path.expanduser(log_path_pattern)
    
    # Get list of matching log files
    log_files = glob.glob(expanded_path)
    if not log_files:
        print(f"No log files found matching pattern: {log_path_pattern}")
        return

    # Dictionary to store file positions
    file_positions = {}
    
    # Show last n lines of each file initially
    for log_file in log_files:
        with open(log_file, 'r') as f:
            # Get last n lines
            lines = f.readlines()
            start = max(0, len(lines) - num_lines)
            if start < len(lines):
                print(f"\n=== Initial {num_lines} lines from {log_file} ===\n")
                for line in lines[start:]:
                    print(line.rstrip())
            
            # Store current position
            file_positions[log_file] = f.tell()

    print("\nMonitoring for new log entries (Press Ctrl+C to stop)...")
    
    try:
        while True:
            updated = False
            
            # Check each file for new content
            for log_file in log_files:
                with open(log_file, 'r') as f:
                    # Seek to last position
                    f.seek(file_positions[log_file])
                    
                    # Read any new lines
                    for line in f:
                        print(f"{Path(log_file).name}: {line.rstrip()}")
                        updated = True
                    
                    # Update position
                    file_positions[log_file] = f.tell()
            
            # Only sleep if no updates
            if not updated:
                time.sleep(0.1)
                
    except KeyboardInterrupt:
        print("\nStopping log monitor...")

if __name__ == "__main__":
    # Log pattern for Claude logs
    log_pattern = "~/Library/Logs/Claude/mcp*.log"
    follow_logs(log_pattern)