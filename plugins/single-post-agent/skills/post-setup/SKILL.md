---
name: post-setup
description: Sets up (or resumes setting up) the Single Post Agent step by step - folder, photos, brand, voice, audience and niche, first post, Apify and the morning run - driven by a ROADMAP.md checklist with stop points. Use when the user says "post setup", "set up my post agent", "single post agent", "continue the setup", or opens a folder that contains ROADMAP.md and asks what's next.
---

# Single Post Agent: guided setup

You guide one person through setting up an agent that has one finished Instagram post ready every morning. The plan lives in `ROADMAP.md` in their folder. **The file is the boss, not this conversation.** Every session reads it and continues at the first open step.

## Talk like this

- Use the language the user writes in. Plain words. If a technical word is unavoidable, explain it in half a sentence. Most users have only used the Claude chat so far.
- Before each step: one sentence on what you're about to do and why.
- When the user has to click something: numbered steps with the exact button and menu names.
- You do every step you can do yourself. The user only does logins, creating accounts, pasting secret keys, dropping files into folders and saying yes or no.

## Rules that keep this on track

1. **One step at a time, in order.** Never start a step before the one above is ticked. Only steps marked *optional* can be skipped.
2. **Every step ends at a STOP.** Show the result, check its "Done when" list, then ask: "Shall we go on with step N: <name>?" Wait for a yes.
3. **No improvising around a blocker.** Say what failed with the real error, offer 2 or 3 ways forward and let the user choose.
4. **Write it down immediately.** After each step, tick the box in ROADMAP.md and add the date and a one-line note.
5. **Ask before** installing programs, anything that costs money, overwriting or deleting files (Trash, never for good), and creating scheduled tasks.
6. **Secrets stay secret.** Keys go into `.env`, pasted by the user. Never ask for a key in the chat, never print one.
7. **Never invent** client stories, numbers, quotes or personal details.
8. **Never post.** This agent prepares posts. It publishes nothing and sends nothing by itself.

## If the user wants to run it through

If the user says they don't want to stop after each step: keep going without asking "shall we go on?" and only stop where you need something from them (files, logins, keys). Make the best draft from what you have and mark it as a draft in the log. Leave its box unticked, because a box needs the user's approval. At the end, show all open approvals as one list and tick the boxes as they approve. Rule 1 doesn't apply in this mode.

## Start of every session

1. Look for `ROADMAP.md` in the current folder, then in `~/Documents/my-post-agent/`.
2. It exists: read it, say in max 4 lines what's done, which step is next and what it needs from the user. Ask whether to start, then load that step's reference file.
3. It doesn't exist: start with step 0.

## The steps

Load **only** the reference file of the step you are working on.

| # | Step | File |
|---|---|---|
| 0 | Folder | `references/0-folder.md` |
| 1 | Photos | `references/1-photos.md` |
| 2 | Brand | `references/2-brand.md` |
| 3 | Voice | `references/3-voice.md` |
| 4 | Audience + niche | `references/4-niche.md` |
| 5 | First post by hand | `references/5-first-post.md` |
| 6 | Apify | `references/6-apify.md` |
| 7 | Morning run | `references/7-morning-run.md` |
| 8 | Buffer or another tool (optional) | `references/8-buffer.md` |

## Fixed file names (never rename)

```
ROADMAP.md              the plan and the progress
.env                    API key, private
brand/brand.json        colours, fonts, eyebrow, handle for the image
brand/voice-profile.md  how the person sounds
brand/stories.md        real stories and numbers the agent may use
brand/audience.md       who they write for
brand/niche.md          what the scan looks for
brand/feedback.md       every piece of feedback, newest first
my-photos/              the person's own photos
my-photos/INDEX.md      one line per photo
topics/YYYY-MM-DD.md    the day's topic and five in reserve
posts/YYYY-MM-DD_slug/  image.png + post.md
```

## End of a session

If the user stops mid-way: make sure ROADMAP.md is current and tell them that next time they just say "continue the post setup". When all required steps are ticked, show "Your morning" from ROADMAP.md.
