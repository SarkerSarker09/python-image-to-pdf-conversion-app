from PIL import Image
import os



def makePdf(filename):	
	try:
			im = Image.open(filename)
			if im.mode == "RGBA":
    				im = im.convert("RGB")

			new_filename = r"/home/khokon/Pictures/sample001.pdf"
			if not os.path.exists(new_filename):
					try:
    						im.save(new_filename,"PDF",resolution=100.0)
    						print('pdf generated')
					except:
							print('pdf generation error')


	except:
				print('file is not opening')								

filename = r"/home/khokon/Pictures/23569861-sample-grunge-red-round-stamp.jpg" 
makePdf(filename)
   	


