import imageio.v3 as iio

# defines the paths of the pictures
filenames = ['assets/chicklet1.png', 'assets/chicklet2.png', 'assets/chicklet3.png', 'assets/chicklet4.png']
images =[]

# loops over and reads the images
for filename in filenames:
    images.append(iio.imread(filename))

# saves the gif to the current directory
iio.imwrite('./chicklet.gif', images, duratio = 500, loop = 0)