from flask import Flask, request, send_file
import io

app = Flask(__name__)

@app.route('/api/tracker')  # Matches the Vercel route
def tracker():
    # Log the request
    print(f"Tracker hit: IP={request.remote_addr}, User-Agent={request.headers.get('User-Agent')}")

    # Return a 1x1 transparent PNG
    img = io.BytesIO(
        b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\xdac\xf8\xff\xff?\x00\x05\xfe\x02\xfe\xa7=\xea\xc1\x00\x00\x00\x00IEND\xaeB`\x82'
    )
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run()
