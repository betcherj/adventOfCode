from matplotlib import pyplot as plt
dimensions = [25,6]

def color_image(layers, num_layers):
    temp = [0 for x in range(dimensions[0])]
    final_image = []
    for m in range(dimensions[1]):
        final_image.append(temp.copy())
    for p in range(num_layers):
        layer = layers[p]
        all_colored = True
        for i in range(dimensions[1]):
            for j in range(dimensions[0]):
                if final_image[i][j] == 2 * p:
                    if int(layer[i][j]) == 1 or int(layer[i][j]) == 0:
                        final_image[i][j] = int(layer[i][j])
                    else:
                        all_colored = False
                        final_image[i][j] = final_image[i][j]+2
        if all_colored == True:
           break
    return final_image

def multiply_layer(layer):
    one_ctr = 0
    two_ctr = 0
    for i in range(dimensions[1]):
        for j in range(dimensions[0]):
            if int(layer[i][j]) == 1:
                one_ctr +=1
            elif int(layer[i][j]) == 2:
                two_ctr += 1
    return one_ctr*two_ctr

def find_fewest_zero_layer(layers, num_layers):
    res = [100, 100]
    for p in range(num_layers):
        l_ctr = 0
        for i in range(dimensions[1]):
            for j in range(dimensions[0]):
                if int(layers[p][i][j]) == 0:
                        l_ctr += 1
        if l_ctr<=res[1]:
            res = [p, l_ctr]
    return res[0]

def image_decode(pixels):
    layer_size = dimensions[0] * dimensions[1]
    num_layers = int(len(pixels)/layer_size)
    layers =[]
    pos = 0
    for i in range(num_layers):
        layer = []
        for j in range(dimensions[1]):
            offset = i*layer_size + j*dimensions[0]
            layer.append(pixels[pos+offset:pos+dimensions[0]+offset])
        layers.append(layer)
    index = find_fewest_zero_layer(layers, num_layers)
    res = multiply_layer(layers[index])
    final_image = color_image(layers, num_layers)
    return final_image

if __name__ == "__main__":
    image = open('day8.txt').read().strip(' ')
    final_image = image_decode(image)
    plt.imshow(final_image, interpolation='nearest')
    plt.show()


