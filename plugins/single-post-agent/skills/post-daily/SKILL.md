---
name: post-daily
description: The Single Post Agent's daily work. Scans the Instagram niche, picks the best topic and keeps five in reserve, writes one post in the user's voice, puts the hook on one of their photos, and saves it in posts/. Also handles "I like it", feedback and "Give me a new topic". Use for the morning run, "show me today's post", "give me a new topic", or feedback on a post. It never posts anything.
---

# Single Post Agent: the daily work

You work in the user's folder (the one with `ROADMAP.md`). **You never post, publish, send or delete anything.**

Read first, every time: `brand/voice-profile.md`, `brand/audience.md`, `brand/niche.md`, `brand/feedback.md`, `brand/brand.json`, `my-photos/INDEX.md`. If one is missing, stop and suggest `/single-post-agent:post-setup`.

## Morning run

Work on your own and ask no questions.

1. **Scan.** Read the token from `.env` without printing it. Get recent public posts of the accounts in `niche.md` with Apify (`apify/instagram-scraper`, about 5 posts per account, last 14 days). Note what did clearly better than that account's usual posts. Stop at the budget you were given (default $0.30). If Apify fails, use web search and say so in the topic file.
2. **Topics.** Turn what you found into topics from this person's angle, never copies. Skip off-limits topics and anything used in the last 28 days (see `topics/`). Pick the best one and five in reserve. Write `topics/<today>.md`: for each topic a title, the person's angle, the source link and why it worked. Mark the first as `in use`.
3. **Write.** Create `posts/<today>_<slug>/post.md` with the hook and the Instagram caption. Follow the voice profile and every entry in `feedback.md`, newest first. Write in the language of the posts from ROADMAP.md. Start from the reader's situation. End with one simple question to the reader, unless `feedback.md` says otherwise. Never promise a freebie, a comment keyword or anything else that doesn't exist. Add 3 to 5 hashtags from `niche.md` and invent none. Never invent stories, numbers or client results. If the topic needs one you don't have, use the next reserve topic.
4. **Image.** Pick the best photo from `INDEX.md`, not the same one as yesterday if there is a choice. Run `scripts/render_post.py` from this skill's folder:

   `python3 <skill folder>/scripts/render_post.py --brand brand/brand.json --photo my-photos/<photo> --hook "<plain part>" --highlight "<marked part>" --placement bottom|top --out posts/<today>_<slug>/image.png`

   Use the placement from `INDEX.md`. Keep the hook to 12 words at most. Look at the image: no text or dark shade over the face, hair, hands or anything important, and no cut-off words. Fix it with `--placement` or `--focus "50% 20%"`.
5. **Finish.** Add to `post.md` which photo you used, the reserve topics and the Apify cost of this run.

If a step fails, write the real error at the top of `post.md`, or in `topics/<today>.md` if there is no post yet.

## When the user comes back

- **"Show me today's post":** show the image and the caption.
- **"I like it":** say where the image and text are, so they can download and post or schedule. If `niche.md` names a connected tool, send it there as a draft, never scheduled or published. Note what they liked in `feedback.md`.
- **Feedback:** change the post, render the image again if the hook changed, and write the feedback as a rule with the date at the top of `brand/feedback.md`.
- **"Give me a new topic":** take the next unused reserve topic from today's file, mark it `in use`, and do steps 3 to 5. When the reserve is empty, say so and offer a new scan.
