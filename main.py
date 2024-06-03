import os
import rawpy
import imageio

def convert_cr2_to_png(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.cr2'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}.png')
            
            with rawpy.imread(input_path) as raw:
                rgb_image = raw.postprocess()
                imageio.imsave(output_path, rgb_image)
                print(f'Converted {input_path} to {output_path}')


convert_cr2_to_png('dracena', 'dracena\png')