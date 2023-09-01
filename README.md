# badAppleSlidy
my old script that generates sliding puzzle scrambles out of images for simple bad Apple fun project

It's really old by now. From what I can understand, to run this script you have to specify the puzzle size in the code, the amount of frames (i extracted them using ffmpeg), and also width and height in pixels, that probably should be consistent with a puzzle size. I really don't know why it's not calculated automatically, but anyway, i just upload it here to possible improve the code in the future. 

Also, in the current version the path for frame names is hardcoded, keep that in mind. 

Also, another note, the swapping alg is questionable, and i never actually checked two things: 
  1) resulting scrambles are all solvable
  2) i have to swap any tiles at all, because it probably should be even anyway?
