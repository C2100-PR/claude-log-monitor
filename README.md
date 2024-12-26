# Claude Log Monitor

A Python script for real-time monitoring of Claude log files, similar to the `tail -f` command. This script provides a simple way to watch multiple log files simultaneously with pattern matching support.

## Features

- Monitor multiple log files in real-time
- Show initial history (last N lines) when starting
- Support for glob patterns to match multiple files
- Clean display with filename prefixes for each log entry
- Graceful shutdown with Ctrl+C

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/C2100-PR/claude-log-monitor.git
   cd claude-log-monitor
   ```

2. No additional dependencies required - uses Python standard library only

## Usage

Run the script directly:

```bash
python log_monitor.py
```

By default, it monitors Claude log files in `~/Library/Logs/Claude/mcp*.log`

### Customization

To monitor different files, modify the `log_pattern` variable in the script or import the `follow_logs` function to use in your own code:

```python
from log_monitor import follow_logs

# Monitor different files
follow_logs("/path/to/your/logs/*.log")

# Change number of initial history lines
follow_logs("/path/to/logs/*.log", num_lines=50)
```

## License

MIT License