# An image is a grid of coloured squares
# A color of each pair (i,j) of indices
# A discretization

# First Lecture: working with an image

# Execute 'download_image.jl' script first

using Images

dog = load("perrito.jpg")
typeof(dog)

# size(height, width)
# it starts from the up left to bottom rigth
# to save an image you can make in the repl : save("name.png", rgbxImage)

red = RGB(1.0,0,0)

red_path_image = dog[1000:3500, 1:2800]

for i in 1:100
  for j in 1:100
    red_path_image[i,j] = red
  end
end

green_path_image = dog[1000:3500, 1:2800]
# This syntax applies the right command to all the elements of the array in the left
# broadcasting
green_path_image[50:500, 200:400] .= RGB(0,1.0,0)

# decimate can transform the image to be of poorer quality and smaller
