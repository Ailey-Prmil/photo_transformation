import matplotlib.pyplot
from sklearn.cluster import KMeans
import os
import numpy
from PIL import Image
#os.chdir("../Learning Science") # change directory  -- edit dir here !
img = matplotlib.pyplot.imread("path.JPG") # read the data of an image --change the file name of the photo here!
# print (img.shape()) --> return a tuple (ngang, dọc, số màu<3>)#
width = img.shape[0]  # width of the image
height = img.shape[1] # height of the image
img = img.reshape(width*height,3) # dưỡi thành 1 chuỗi như list gồm mỗi element là 3 màu, list này gồm (ngang*dọc) element
kmeans = KMeans (n_clusters=2).fit(img) # đưa bức ảnh vào chuyển bức ảnh thành 5 màu
labels = kmeans.predict(img) # predict và đánh dấu tất cả các pixel theo 5 màu trung bình
clusters = kmeans.cluster_centers_ #chọn 5 màu Trung bình
###################################################
#new_img = numpy.zeros_like(img)
#for i in range (len(new_img)):
    #new_img[i] = clusters[labels[i]]
################################################### - another brief way 
index = 0
new_img = numpy.zeros((width, height,3),dtype=numpy.uint8)
for i in range (width):
    for j in range (height) :
        label_of_pixel = labels [index]
        new_img[i][j]= clusters[label_of_pixel]
        index +=1

new_img = new_img.reshape(width,height,3) # KHÔi phục ảnh như lúc đầu
matplotlib.pyplot.imshow(new_img)
matplotlib.pyplot.show()
im = Image.fromarray(new_img) # convert into an png image using module
im.save("hinh_file_1.jpg") # the file_name of the result