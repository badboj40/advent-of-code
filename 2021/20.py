from copy import deepcopy

with open("input/20", "r") as f:
    indata = f.read().split('\n')[:-1]

algo = ['1' if x=='#' else '0' for x in indata[0]]
image_indata = [['1'  if x=='#' else '0' for x in row] for row in indata[2:]]


def create_image(image_input, margin):
    image = []
    width = len(image_input[0]) + 2 * margin
    for i in range(margin):
        image.append(['0'] * width)
    for row in image_input:
        image.append(['0']*margin + row + ['0']*margin)
    for i in range(margin):
        image.append(['0'] * width)
    return image


def enhance_image(algo, image):
    enhanced = [['0' for x in row] for row in image]
    for y in range(1, len(image)-1):
        for x in range(1, len(image[0])-1):
            index_list = image[y-1][x-1:x+2] + image[y][x-1:x+2] + image[y+1][x-1:x+2]
            index_str = ''.join(index_list)
            index = int(index_str, 2)
            enhanced[y][x] = algo[index]
    return enhanced


def show_image(image):
    visual_image = [['#' if x=='1' else '.' for x in row] for row in image]
    for row in visual_image:
        print(''.join(row))
    print()


def count_pixels(image):
    pixel_sum = 0
    for row in image:
        pixel_sum += row.count('1')
    return pixel_sum


def crop_image(image):
    cropped = []
    for row in image[1:-1]:
        cropped.append(row[1:-1])
    return cropped


def part1():
    image = create_image(image_indata, 2*2)
    for i in range(2):
        image = enhance_image(algo, image)
        image = crop_image(image)
    return count_pixels(image)


def part2():
    margin = 100
    image = create_image(image_indata, 50*2)
    for i in range(50):
        image = enhance_image(algo, image)
        image = crop_image(image)
    return count_pixels(image)


if __name__ == "__main__":
    print("part1:", part1())
    print("part2:", part2())
