An intro to CS course I'm starting uses this site the first week, asking that we make art with the individual pixels: <https://studio.code.org/courses/pixelation/units/1/lessons/2/levels/1> . I thought it would be a good opportunity to reacquaint myself with Python to automate the process a bit (and seem like a better artist than I actually am)!

You can use any image type used by the PIL library (to varying degrees of success) and it will scale it down to be the 255x255 maximum size allowed for the site, convert it to a black and white image, then output the binary values into a designated file. The scaling is destructive as it overwrites the original image, so do keep that in mind.  

I'm sure there is a lot I could do to optimize it (say, only opening the file once for example), but this was more of an exercise to get back into programming with a specific use case in mind. 
