# mz-sample

First of all, export your credentials.
```bash
export TWITTER_CONSUMER_KEY=YOUR_TWITTER_CONSUMER_KEY
export TWITTER_CONSUMER_SECRET=YOUR_TWITTER_CONSUMER_SECRET
export TWITTER_ACCESS_TOKEN=YOUR_TWITTER_ACCESS_TOKEN
export TWITTER_ACCESS_TOKEN_SECRET=YOUR_TWITTER_ACCESS_TOKEN_SECRET
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Download followers
It takes very time.

```bash
python download_followers.py > download_followers.log 2>&1 &
```
