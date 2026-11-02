# Step 7: Morning run

**Goal:** every morning one finished post is waiting in `posts/`.

## Ask first

Which time? Suggest a time shortly before they usually start. **The computer has to be on and the Claude app open at that time.** If it was off, the run happens when the app opens again. So they can turn on the computer, get a coffee and come back to a finished post.

## Create the scheduled task

Name: `single-post-morning`, daily at the agreed time, working folder: their folder. Use this Claude's scheduled-task tool. If there is none, tell the user honestly and stop. Don't build a workaround without asking.

Task prompt (fill in the folder):

```
Use the skill single-post-agent:post-daily in the folder <FOLDER> and do today's morning run. Work fully on your own and ask no questions. Never post, publish, send or delete anything. Spend at most $0.30 on Apify.
```

**Permission mode:** the task has to run on **Auto**. On Manual it stops and waits for an approval while nobody is there. Tell the user where to set this in the task's settings, with the exact button names you see.

## Test

Run the task once now. Show the image and caption, the five reserve topics and the Apify cost.

## Done when

- the task exists on Auto at the agreed time
- one test run produced a post, and the user approved it in words
- the cost is in the log, and you did the sum: cost per run x 30 against the monthly credit. If it doesn't fit, lower the number of accounts or suggest a scan every few days.

**STOP:** tick. The required setup is complete: show "Your morning" from ROADMAP.md, then ask whether they want step 8 now, later or never.
