from PIL import Image, ImageDraw, ImageColor
from random import randint
import sys

# Open palette and image

palette = open(sys.argv[1], "r")
palette_list = []
for line in palette:
	this_color = line.split(",")
	if this_color[-1:] == "\n":
		this_color[2] = this_color[2][:-1]
	palette_list.append(this_color)

in_pic = open(sys.argv[2], "rb")
im = Image.open(in_pic)
im = im.resize((120,120))
px = im.load()
print(im.format, im.size, im.mode)

# Set up canvas

working_image = Image.new('RGBA', im.size, (255,255,255,0))
working_pixels = working_image.load()
drawer = ImageDraw.Draw(working_image)

passes = 0
accuracy = 85
not_over = True
last_sim = 0

# Determine and place highest average color in each pass by relying on provided palette

while passes < 25 and not_over:
	colors_processed = 0
	success_list = []
	for color in palette_list:
		overall_similarity = 0
		temp_working_image = working_image.copy()
		temp_working_pixels = temp_working_image.load()
		temp_drawer = ImageDraw.Draw(temp_working_image)
		for vert_coord in range(0, working_image.size[1]):
			for horiz_coord in range(0, working_image.size[0]):			
				#print(passes, similarity)
				#print(passes, original_pixel, working_pixel, similarity);
				
				if passes == 0 or this_similarity > similarity:
					temp_drawer.point((horiz_coord, vert_coord), fill=(int(color[0]), int(color[1]), int(color[2])))
				
				original_pixel = px[horiz_coord, vert_coord]
				working_pixel = temp_working_pixels[horiz_coord, vert_coord]
				r_close = abs((original_pixel[0] - working_pixel[0])/255)
				g_close = abs((original_pixel[1] - working_pixel[1])/255)
				b_close = abs((original_pixel[2] - working_pixel[2])/255)
				similarity = (1 - ((r_close + g_close + b_close)/3)) * 100
				
				this_r_close = abs((original_pixel[0] - int(color[0]))/255)
				this_g_close = abs((original_pixel[1] - int(color[1]))/255)
				this_b_close = abs((original_pixel[2] - int(color[2]))/255)
				this_similarity = (1 - ((this_r_close + this_g_close + this_b_close)/3)) * 100
				
				overall_similarity += similarity
		overall_similarity = round(overall_similarity/(working_image.size[0]*working_image.size[1]), 3)
		success_list.append(overall_similarity)
		colors_processed += 1
		print("Colors done: ", colors_processed, " of ", len(palette_list), "\nSimilarity: ", overall_similarity)
	
	max_index = success_list.index(max(success_list))
	this_color = palette_list[max_index]
	#print(max_index)
	#print("Decided on: ", palette_list[max_index])
	
	for vert_coord in range(0, working_image.size[1]):
		for horiz_coord in range(0, working_image.size[0]):	
			original_pixel = px[horiz_coord, vert_coord]
			working_pixel = working_pixels[horiz_coord, vert_coord]
			r_close = abs((original_pixel[0] - working_pixel[0])/255)
			g_close = abs((original_pixel[1] - working_pixel[1])/255)
			b_close = abs((original_pixel[2] - working_pixel[2])/255)
			similarity = (1 - ((r_close + g_close + b_close)/3)) * 100
			
			this_r_close = abs((original_pixel[0] - int(this_color[0]))/255)
			this_g_close = abs((original_pixel[1] - int(this_color[1]))/255)
			this_b_close = abs((original_pixel[2] - int(this_color[2]))/255)
			this_similarity = (1 - ((this_r_close + this_g_close + this_b_close)/3)) * 100
			
			if passes == 0 or this_similarity > similarity:
				drawer.point((horiz_coord, vert_coord), fill=(int(this_color[0]), int(this_color[1]), int(this_color[2])))
	
	del palette_list[max_index]
	working_image.save("testImage_" + str(passes) + ".png")
	passes += 1
	print(success_list)
	print("Last Sim: ", last_sim, "\nPasses: ", passes, "\nSimilarity: ", success_list[max_index], "\n")
	if last_sim == success_list[max_index]:
		not_over = False
	last_sim = success_list[max_index]