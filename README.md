# DSGE Landing Page Streamlit Bundle

This bundle lets you upload the project to GitHub and deploy it on Streamlit while keeping the landing page looking and working like the HTML version.

## Files
- `app.py` — Streamlit wrapper
- `landing.html` — your landing page
- `requirements.txt` — Python dependency

## Run locally
1. Open the folder in VS Code
2. Open terminal
3. Install requirements:
   `pip install -r requirements.txt`
4. Start the app:
   `streamlit run app.py`

## Upload to GitHub
1. Create a new GitHub repo
2. Upload all files from this folder
3. Commit and push

## Deploy on Streamlit Community Cloud
1. Sign in to Streamlit Community Cloud
2. Click **Create app**
3. Choose your GitHub repo
4. Set the main file path to `app.py`
5. Deploy

## Notes
- The page is rendered from `landing.html` inside Streamlit.
- If the page gets longer, increase the `height=` value in `app.py`.
- Email buttons and anchor links remain in the HTML.
- If you later want forms, analytics, or dashboards connected to Python, the HTML can be converted into a fully native Streamlit app.

## Recommended repo structure
```text
your-repo/
├── app.py
├── landing.html
├── requirements.txt
└── README.md
```
