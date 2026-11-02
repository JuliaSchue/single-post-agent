# Step 0: Folder

**Goal:** one permanent folder for the agent. Temporary folders get cleaned up by the computer, so they are a trap.

## What you do

1. Check the current folder. If its path contains `tmp`, `temp`, `scratch` or `Downloads`, or it is the home folder or a cloud sync folder, suggest `~/Documents/my-post-agent/` and ask.
2. If the folder already holds files, list them and ask before you use or move anything.
3. Create `brand/`, `my-photos/`, `topics/`, `posts/`, an empty `brand/feedback.md` and `.env`. Make `.env` private (on a Mac: `chmod 600 .env`). If the folder is under git, add `.env` and `my-photos/` to `.gitignore`.
4. Copy `roadmap-template.md` to `ROADMAP.md` and fill in the header. Ask for the name, the Instagram handle and the language of the posts, which can differ from the language of this chat.

## Done when

- the folder is permanent, the structure exists, ROADMAP.md is filled in

**STOP:** tick, ask about step 1.
