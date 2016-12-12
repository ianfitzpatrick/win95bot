# Win95 Promises

@win95promises is a bot that posts screenshots from the Windows 95 install process, but tweaks some of the promises of benefit made by your new life with Windows 95.

## Method

### The Screens

First job was to get screenshots of all the Windows 95 install screens.

That was easy enough, I installed a copy of Windows 95 in Virtual Box (with the CPU set to 1% to avoid crashing), and fired up Quicktime Player to record my screen. Screenshoting by hand wasn't practical as the installer progresses *really* fast.

### The Font

This seriously 90%+ of the work. If the new benefit font looked off, it ruins the effect to me. I really wanted something that looks very convincing.

Unfortunately I couldn't even find a .fon file for whatever system font the installer uses. So I resorted to typing every character on the keyboard into the cd-key input box, screenshotting that, and then creating a sprite map of the results. 

This was a pain because the font is variable width, so I had to measure and hand sort each character in the sprite map. You can see the results in `spritesheet.png`.

Then in `generate_iamge.py` you can see the `sprite_map_rows` dictionary, which maps each character in the sprite sheet.

I also had to deal with line wrapping and some other little things with text, but this font was the biggest time sink.

### Text Generation

The formula I am using to generate new benefits is to start with a "daily affirmation" sentence, lop off the start of the sentence, and replace it with a feature of Windows 95 + some glue words to make the sentence hang together. 

For instance:

    I feel basically worthy as a person.

Becomes:

    Recylce Bin makes me basically worthy as a person.

I found affirmations that start with the word "I am" or "I" work the best. I replaced the word "you" with "I" in a lot of cases.

I just found random 175 affirmations on the web, which I am a little uncomfortable with. I'd like to try re-generating them in the future using a recurrent neutral network if practical.
