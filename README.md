# badAppleSlidy

**Description:**
This project is a relic from my past, conceived for the sole purpose of generating sliding puzzle scrambles from images.

**Status:**
This script is quite dated now, but I've decided to share it, even though it might need some refurbishment in the future.

**Usage:**
To run this script, you'll need to make a few manual adjustments in the code, such as specifying the puzzle size, the number of frames (assuming you've extracted them using ffmpeg), and the width and height in pixels. Oddly enough, these dimensions aren't automatically computed, but they should ideally match your puzzle size.

**Image Handling:**
Please note that this script doesn't handle image resizing or frame extraction; you'll have to handle that separately. The image sizes must align with the width and height values specified in the code, though I can't explain why this isn't calculated automatically.

**Code Quality:**
I'll be the first to admit that the code quality here is far from perfect. It may look so bad that one might consider making it private, but for now, I'm leaving it open for potential future improvements.

**Frame Path:** 
One important detail to remember is that the frame path is hardcoded in the current version. Keep this in mind when working with the script.

**Algorithm Questions:**
I must confess that the swapping algorithm used here is questionable, and there are two significant doubts that I haven't addressed:
1. Whether the resulting scrambles are all solvable.
2. Whether it's even necessary to swap any tiles at all, as it might be perfectly fine as is.

Feel free to explore and experiment with this quirky script.
