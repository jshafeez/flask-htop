from flask import Flask
import os
import time

app = Flask(__name__)

# Route for /htop endpoint
@app.route('/htop')
def htop():
    # Your full name
    name = "JS Mohammed Hafeez"  # Replace with your actual name

    # System username
    username = os.getenv("jshafeez")  # Get system username

    # Server time in IST (Indian Standard Time, UTC+5:30)
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 19800))  # Convert UTC to IST

    # Placeholder for 'top' command output (you can add real output if desired)
    top_output = """
    PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND
    1 root      20   0  169520  10636   8312 S  0.0  0.1   0:01.01 systemd
    2 root      20   0  169520  10636   8312 S  0.0  0.1   0:01.01 systemd
    """  # You can simulate the output or run the 'top' command and capture it dynamically

    # Return HTML response
    return f"""
    <html>
        <head><title>HTop Output</title></head>
        <body>
            <h1>Server Info</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h3>Top Output:</h3>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

# Main entry point for Flask app
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)  # Expose on port 5000
