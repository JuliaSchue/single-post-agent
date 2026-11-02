# Step 6: Apify

**Goal:** a working Apify token in `.env`, tested with a tiny request. Apify collects public posts from Instagram. The free plan comes with a small monthly credit.

## What the user does (give these as numbered steps)

1. Go to **apify.com**. Click **Sign up** and confirm the email, or **Log in** if they already have an account.
2. In the Apify Console, open **Settings**, then **API & Integrations**.
3. Copy the **Personal API token**.

## What you do

1. Add the line `APIFY_TOKEN=` to `.env` and open the file for the user (on a Mac: `open -e .env`). Ask them to paste the token right after the `=`, save and close, then say "done". **Never ask for the token in the chat.** Explain that `.env` is hidden in the Finder and that this is normal, so they should only use the window you opened.
2. Check it without showing it: `grep -c '^APIFY_TOKEN=.\+' .env` must print `1`.
3. Fetch 3 recent posts of one account from `niche.md` with the Actor `apify/instagram-scraper` (input: `directUrls` with the account URL, `resultsType: "posts"`, `resultsLimit: 3`), using the Apify tools if this Claude has them, otherwise the REST API with `curl`.
4. Show the first line of each post, the cost of the run (right after a run Apify may still show $0, so check again a moment later) and the remaining credit, which is the limit minus what is already used (`GET https://api.apify.com/v2/users/me/limits`). If they already used this account, warn them that other tasks share the same credit.

If the scraper is blocked or an account is private, try another account. If it keeps failing, note it. The morning run then uses web search and says so.

## Done when

- the token is in `.env`, the test returned posts and its cost is in the log

**STOP:** tick, ask about step 7.
