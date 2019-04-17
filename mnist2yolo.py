import os
import scipy.misc
import numpy as np

def get_images(imgf, n):
    f = open(imgf, "rb")
    f.read(16)
    images = []

    for i in range(n):
        image = []
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)
    return images

def get_labels(labelf, n):
    l = open(labelf, "rb")
    l.read(8)
    labels = []
    for i in range(n):
        labels.append(ord(l.read(1)))
    return labels

def output_txt(outf, label):
    o = open(outf, "w")
    o.write(str(label) + " 0.5 0.5 1 1\n")
    o.close()

def output_png(images, labels, prefix):
    for i in range(len(images)):
        out = os.path.join(prefix, "%06d-num%d.png"%(i,labels[i]))
        txt = os.path.join(prefix, "%06d-num%d.txt"%(i,labels[i]))
        scipy.misc.imsave(out, np.array(images[i]).reshape(28,28))
        output_txt(txt, labels[i])

def mnist_png(imgf, labelf, prefix, n):
    images = get_images(imgf, n)
    labels = get_labels(labelf, n)
    output_png(images, labels, prefix)

mnist_png("train-images-idx3-ubyte", "train-labels-idx1-ubyte", "train", 60000)
mnist_png("t10k-images-idx3-ubyte",  "t10k-labels-idx1-ubyte",  "test",  10000)

