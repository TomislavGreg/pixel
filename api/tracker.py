from flask import Flask, request, send_file
import requests
import io

app = Flask(__name__)

# Your Discord webhook URL (keep this secure!)
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1316467496169242694/1xB8mtqfK090OcVUigEW8FAKeZYs0bWyC-p2XpgN4lt2XDOSxUyUvWrcQXluQjk3MKMP"

def send_discord_notification(ip_address, user_agent):
    """Send a notification to Discord."""
    data = {
        "content": f"📩 Email opened!\n\n**IP Address**: {ip_address}\n**User-Agent**: {user_agent}",
        "username": "Email Tracker Bot"
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print("Discord notification sent successfully!")
        else:
            print(f"Failed to send Discord notification: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"An error occurred while sending the Discord notification: {e}")

@app.route('/api/tracker')
def tracker():
    """Endpoint for the tracking pixel."""
    # Get client information
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Unknown')
    
    # Log the access
    print(f"Tracker hit: IP={ip_address}, User-Agent={user_agent}")
    
    # Send a Discord notification
    send_discord_notification(ip_address, user_agent)
    
    # Return a 1x1 transparent PNG
    img = io.BytesIO(
        b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\xdac\xf8\xff\xff?\x00\x05\xfe\x02\xfe\xa7=\xea\xc1\x00\x00\x00\x00IEND\xaeB`\x82'
    )
    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
