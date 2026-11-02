---
name: post-status
description: Shows in a few lines where the Single Post Agent stands - setup progress from ROADMAP.md, and once it runs, whether today's post was made. Read-only. Use when the user asks "post status", "where are we", "did today's post run".
---

# Single Post Agent: status

Read-only. Change nothing and start nothing. Use the user's language and plain words, max 8 lines.

1. Find `ROADMAP.md` in the current folder, else `~/Documents/my-post-agent/`. If there is none, suggest `/single-post-agent:post-setup`.
2. **Setup not finished:** how many of steps 0 to 7 are done, the next step and what the user needs for it.
3. **Setup finished:** does `posts/<today>_*` exist, with an image? How many reserve topics are left? If nothing is there, the likely reason is that the computer was off or the Claude app was closed at the run time. Offer to run it now.
