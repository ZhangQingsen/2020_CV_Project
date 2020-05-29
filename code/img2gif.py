# -*- coding: UTF-8 -*-
 
import os
import imageio
 
def create_gif(image_list, gif_name):
 
    frames = []
    # for image_name in image_list:
    #     if image_name.endswith('.png'):
    #         print(image_name)
    #         frames.append(imageio.imread(image_name))
    for i in range(101):
        img_name = f"./images/seq_{i}.png"
        print(img_name)
        frames.append(imageio.imread(img_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.02)
 
    return
 
def main():
 
    path=r'./images/'
    image_list=[ path+img for img in  os.listdir(path)]
    gif_name = 'facemorph.gif'
    create_gif(image_list, gif_name)
 
if __name__ == "__main__":
    main()