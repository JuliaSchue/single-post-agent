# Step 2: Brand

**Goal:** `brand/brand.json` makes the image look like the person.

## What you do

1. Most people have no brand book. Ask how they want to show you their look and offer these three ways (any one is enough, they can also combine them):
   - **Their website:** you look at it and take the colours and fonts from it.
   - **Colours and fonts as text:** hex codes (like `#EC7531`) and font names, for example copied from Canva (Brand Kit, or click a text box and read the font name).
   - **A screenshot:** of their Canva Brand Kit, a Canva design they like, their Instagram grid or anything that shows their look. They drag the image into this chat. Read the colours and fonts from it, then say what you found in plain words ("dark green, light beige, a round sans-serif") and ask if that's right.

   If they have nothing yet, suggest a simple look (one dark colour, one light colour, one accent) and let them say yes or change it. Ask only what you can't see, one question at a time.
2. Write `brand/brand.json`:

   ```json
   {"paper":"#ffffff","ink":"#111111","accent":"#ffd400","headline_font":"Oswald","label_font":"Courier Prime","eyebrow":"For busy coaches","handle":"@name"}
   ```

   This is only the format. Use the person’s own colours and fonts, never these values. `paper` = light colour, `ink` = dark colour, `accent` = the marked part of the hook. Fonts must exist on Bunny Fonts (fonts.bunny.net). If a brand font isn't there, agree on a free look-alike. The accent needs enough contrast with `ink`, because the marked text is `ink` on `accent`.
3. Build a test image with a sample hook. The script is in the `post-daily` skill of this plugin, in `scripts/render_post.py`:

   `python3 <path>/render_post.py --brand brand/brand.json --photo my-photos/<photo> --hook "Three posts a week" --highlight "without the blank screen." --placement bottom --out posts/test/image.png`

   If no browser is found, explain that the image needs Google Chrome and ask whether they want to install it. Use `top` instead of `bottom` if `INDEX.md` says the text belongs at the top of this photo. Show the image. Change `brand.json` until the user likes it.

## Done when

- `brand/brand.json` exists and the user approved the test image in words

**STOP:** tick, ask about step 3.
