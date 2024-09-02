# YouTube Transcript API

This project provides a simple API to retrieve transcripts/subtitles for YouTube videos. It's built with Flask and hosted on Heroku.

## Features

- Retrieve transcripts for any YouTube video
- Secure API key authentication
- Easy to integrate with any application

## Live Demo

The API is hosted at: `https://your-app-name.herokuapp.com`

Replace `your-app-name` with your actual Heroku app name.

## Installation

To set up this project locally:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   export API_KEY=your-secret-api-key
   ```

5. Run the Flask app:
   ```
   python app.py
   ```

## Heroku Deployment

To deploy this application on Heroku:

1. Sign up for a Heroku account at https://signup.heroku.com/ if you haven't already.

2. Install the Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli

3. Login to Heroku via CLI:
   ```
   heroku login
   ```

4. Create a new Heroku app (or use an existing one):
   ```
   heroku create your-app-name
   ```
   Or if you've already created an app on the Heroku website:
   ```
   heroku git:remote -a your-app-name
   ```

5. Set up your API key as a config var:
   ```
   heroku config:set API_KEY=your-secret-api-key
   ```

6. Deploy your app to Heroku:
   ```
   git push heroku master
   ```

7. Ensure at least one instance of the app is running:
   ```
   heroku ps:scale web=1
   ```

8. You can now open your app in the browser:
   ```
   heroku open
   ```

Remember to replace `your-app-name` and `your-secret-api-key` with your actual Heroku app name and chosen API key.

## Usage

To use the API, make a GET request to the `/get_transcript` endpoint with the following parameters:

- `video_id`: The ID of the YouTube video
- `X-API-Key`: Your API key (sent as a header)

### Example using curl:

```bash
curl -H "X-API-Key: your-api-key" "https://your-app-name.herokuapp.com/get_transcript?video_id=VIDEO_ID"
```

Replace `your-api-key`, `your-app-name`, and `VIDEO_ID` with your actual values.

### Example using JavaScript fetch:

```javascript
const API_KEY = 'your-api-key';
const VIDEO_ID = 'VIDEO_ID';

fetch(`https://your-app-name.herokuapp.com/get_transcript?video_id=${VIDEO_ID}`, {
  headers: {
    'X-API-Key': API_KEY
  }
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## API Response

The API returns a JSON array of transcript segments. Each segment contains:

- `text`: The transcribed text
- `start`: The start time of the segment in seconds
- `duration`: The duration of the segment in seconds

## Error Handling

The API will return appropriate error messages and status codes for common issues:

- 400: Missing video_id parameter
- 401: Invalid or missing API key
- 500: Server error or issue with retrieving the transcript

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgements

This project uses the [youtube_transcript_api](https://pypi.org/project/youtube-transcript-api/) package to retrieve YouTube video transcripts.