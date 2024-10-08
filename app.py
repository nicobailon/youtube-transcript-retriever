import os
from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from youtube_transcript_api.formatters import JSONFormatter
from functools import wraps
import logging

app = Flask(__name__)

API_KEY = os.environ.get('API_KEY', 'default-dev-key')

def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        provided_key = request.headers.get('X-API-Key')
        if provided_key and provided_key == API_KEY:
            return view_function(*args, **kwargs)
        else:
            return jsonify({"error": "Invalid or missing API key"}), 401
    return decorated_function

@app.route('/get_transcript', methods=['GET'])
@require_api_key
def get_transcript():
    video_id = request.args.get('video_id')
    
    if not video_id:
        return jsonify({"error": "Missing video_id parameter"}), 400
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = JSONFormatter()
        json_formatted = formatter.format_transcript(transcript)
        return json_formatted, 200, {'Content-Type': 'application/json'}
    except TranscriptsDisabled:
        return jsonify({"error": "Transcripts are disabled for this video"}), 404
    except NoTranscriptFound:
        return jsonify({"error": "No transcript found for this video"}), 404
    except Exception as e:
        app.logger.error(f"Error retrieving transcript for video {video_id}: {str(e)}")
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    app.run(host='0.0.0.0', port=port)