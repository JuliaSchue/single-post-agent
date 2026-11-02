# Step 7: Morning run

**Goal:** every morning one finished post is waiting in `posts/`.

## Ask first

Which time? Suggest a time shortly before they usually start. **The computer has to be on and the Claude app open at that time.** If it was off, the run happens when the app opens again. So they can turn on the computer, get a coffee and come back to a finished post. Each run also uses their Claude plan, so suggest a time when no other scheduled task runs, and don't start it right before they need Claude for other work.

## Create the scheduled task

Name: `single-post-morning`, daily at the agreed time. Use this Claude's scheduled-task tool. The folder is in the prompt below, because the tool may have no field for it. If there is none, tell the user honestly and stop. Don't build a workaround without asking.

Task prompt (fill in the folder):

```
Use the skill single-post-agent:post-daily in the folder <FOLDER> and do today's morning run. Work fully on your own and ask no questions. Never post, publish, send or delete anything. Spend at most $0.30 on Apify.
```

**Permission mode:** the task has to run on **Auto**. On Manual it stops and waits for an approval while nobody is there. The tool may take the mode from this session, so don't assume it worked: read the saved mode back if the tool shows it, and otherwise ask the user to open the task in the app and check it, with the exact names you see. A test run that stops to ask for approval means it isn't on Auto.

## Test

Run the task once now. It runs in its own session, so nothing comes back to this chat by itself. When it is finished, read the newest folder in `posts/` and `topics/<today>.md` yourself, then show the image and caption, the five reserve topics, the Apify cost and how long the run took. Take the user's approval or feedback here in this chat, and write feedback to `brand/feedback.md`.

## Done when

- the task exists on Auto at the agreed time
- one test run produced a post, and the user approved it in words
- the cost is in the log, and you did the sum: cost per run x 30 against the monthly credit. If it doesn't fit, lower the number of accounts or suggest a scan every few days.

**STOP:** tick. The required setup is complete: show "Your morning" from ROADMAP.md, then ask whether they want step 8 now, later or never.
