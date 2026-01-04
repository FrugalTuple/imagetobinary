from PIL import Image

# remember: 0 = black, white = 1 in the pixelation workspace

class Conversion:

    def blackAndWhite(self,rawImagePath): #convert image into only b&w values
        with Image.open(rawImagePath) as rawphoto:
            converted =rawphoto.convert('1',dither= Image.Dither.NONE) #creates a copy in absolute b&w w/o dithering
        return converted #output absolute b&w copy of image


    def binaryConversion(self,image):

        rawPixel= list(image.getdata()) #go through pixels sequentially, put values in a list
        for i in range(0,len(rawPixel)):
         if rawPixel[i] == 255:
             rawPixel[i] = 1
        return rawPixel

    def writeToFile(self,image, path): #write binary to file
        blackAndWhite = self.blackAndWhite(image)
        convertedImage = self.binaryConversion(blackAndWhite)
        with open(file=path, mode = 'w') as f:
            for i in range(len(convertedImage)):
                f.write(str(convertedImage[i]))


    def sizeCheck(self,image): #set size to be within site's limits
        with Image.open(image) as original:
            x,y = original.size
            if x >255 or y > 255:
                original.thumbnail((255,255)) #if over size, use built-in to scale while keeping aspect ratio
            original.save(image)
            original.close()
        return None #not sure if necessary? I wonder if I could just return the size to reference in the next method...

    def showSize(self,image):
        with Image.open(image) as reference:
            x,y = reference.size
        return f"Your image is {x} pixels wide and {y} pixels tall"


class Menu(Conversion):
    imageFilePath = ''
    endPath = ''

    def getImagePath(self):
        path = input("Please enter the path for the image file you'd like to convert: ").strip().replace('  ','')
        return path

    def getEndPath(self):
        userEndPath = input(r"Where would you like to save the converted file? Please include a name for the file such as 'C:\Desktop\output.txt'").strip().replace('  ','')
        return userEndPath

    def convert(self):

        while True:
            try:
                self.imageFilePath = self.getImagePath()
                self.endPath = self.getEndPath()
                self.sizeCheck(self.imageFilePath)
                self.writeToFile(self.imageFilePath,self.endPath)
                print(self.showSize(self.imageFilePath))
                break
            except FileNotFoundError:
                restart = input("It looks as though the image file location you've entered couldn't be found. To try again, press Enter. To exit, type 'exit': ").lower()
                if restart == 'exit':
                    break



menu = Menu()
print("Welcome to the binary conversion tool! Type 'Convert' to convert a file or 'quit' to exit")
menu.convert()


'''for column in range(photoSize):
        rawPixel.append(f"Column Value: {column}")
        for row in range(photoSize):
            rawPixel.append(f"row value{row}'''         #loop logic test



'''for column in range(photoSize):
        rawPixel.append(photo.getpixel((_,column)))
        for row in range(photoSize):
            rawPixel.append(photo.getpixel((row,_)))''' #nested for loop unnecessary; built in function for that..

# still not sure how I would approach getting pixel information with a nested for loop if the getdata() function wasn't there.
