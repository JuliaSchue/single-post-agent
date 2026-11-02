# Single Post Agent

The Content Agent for Instagram from the Claude Bootcamp. One finished Instagram post every morning, in your voice and your brand design. A free Claude Code plugin for coaches and creators by Julia Schürer.

**Every morning the agent:** scans your Instagram niche, picks the best topic and keeps five in reserve, writes the post in your voice and puts your hook on one of your own photos.

**You decide:** "I like it", your feedback, or "Give me a new topic". Then you post it yourself or schedule it. The agent never posts anything by itself.

## What you need

- A paid Claude plan (Pro or higher) and the Claude desktop app
- Google Chrome (it creates the images)
- A free Apify account (Claude shows you how, in step 6)
- Three or four of your own photos, and three or four texts you wrote

## Install

Open the Claude desktop app, click **Code** on the left, open a session and paste this:

```
Please install the Single Post Agent plugin for me.
1. Run: claude plugin marketplace add JuliaSchue/single-post-agent
2. Run: claude plugin install single-post-agent@single-post-agent-marketplace
3. Show me that it worked, then tell me to quit the Claude app and open it again.
```

## Start

After restarting the app, open a Code session and type:

```
/single-post-agent:post-setup
```

Claude guides you step by step and saves your progress in `ROADMAP.md`. Next time, just say "continue the post setup". `/single-post-agent:post-status` shows where you are.

## Good to know

- Your computer has to be on and the Claude app open when the morning run starts.
- The run uses your Claude plan and a little of your Apify credit. Claude shows you the cost per run in step 7.
- Your photos, texts and key stay in your own folder. Apify reads public Instagram posts. Fonts for the images are loaded from Bunny Fonts.
- Check what the agent writes before you post it. You are responsible for what you publish.

## More

Want more agents? The carousel agent and everything else are in the [Coach Code Club](https://coachcodeclub.com).

Built by Julia Schürer with Claude Code.
