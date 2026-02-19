# ChatGPT Integration with GitHub

This repository demonstrates how to integrate OpenAI's ChatGPT API with GitHub Actions.

## Setup Instructions

### 1. Get Your OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Create a new API key
4. Copy the key

### 2. Add GitHub Secret
1. Go to your repository: https://github.com/mmaherdodo-collab/chatgpt-integration
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `OPENAI_API_KEY`
5. Value: Paste your OpenAI API key
6. Click **Add secret**

### 3. Files in This Repository

- **`.github/workflows/chatgpt-example.yml`** - GitHub Actions workflow that runs on push and pull requests
- **`script.py`** - Python script that uses the ChatGPT API

### 4. How It Works

When you push code or create a pull request, the GitHub Actions workflow will:
1. Check out your code
2. Set up Python 3.11
3. Install the OpenAI library
4. Run `script.py` which sends a request to ChatGPT

### 5. Customize

Edit `script.py` to:
- Change the message sent to ChatGPT
- Use different models (gpt-3.5-turbo, gpt-4, etc.)
- Add more complex logic

## Security Notes

⚠️ **Never commit your API key to GitHub!** Always use GitHub Secrets.

## Learn More

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)