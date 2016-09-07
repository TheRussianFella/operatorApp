#import sys
#if sys.platfrom == 'win32':
#	import win32api
#	import win32print

from PIL import Image, ImageChops

def make_background(size, colorspace='RGBA'):
	return Image.new(colorspace, size) #, 'white')

def render(
	images,
	size=(8.27, 11.69),
	max_width=2.5,
	offset=0.393701,
	dpi=72,
	rotate_angle=180):

	# also rotate image for convenience
	h, w = size
	sz = (int(w * dpi), int(h * dpi))
	pix_offset = int(offset * dpi)

	pix_mw = int(max_width * dpi)

	width = (sz[0] - ((len(images) + 1) * pix_offset)) // len(images)
	height = (sz[1] - (pix_offset * 2)) // 2

	if pix_mw < width:
		width = pix_mw

	imageSize = (width, height)

	if not ((width and height) and (sz[0] and sz[0])):
		return None

	bg = make_background(size=sz)

	for idx, imgs in enumerate(images):
		xoffset = pix_offset + width * idx + pix_offset * idx

		for img_idx, img_path in enumerate(imgs):
			yoffset = pix_offset + img_idx * height
			point = (xoffset, yoffset)

			img = _aspectFit(
					Image.open(img_path), imageSize)
			if img_idx != 0:
				img = img.rotate(rotate_angle * img_idx)

			bg.paste(img, point)

	return bg.rotate(90, expand=True)

def _aspectFit(image, size, colorspace='RGBA', color=(255, 255, 255, 0)):
	image = image.copy()
	image.thumbnail(size, Image.ANTIALIAS)
	background = Image.new(colorspace, size, color)
	point = (
		(size[0] - image.size[0]) // 2,
		(size[1] - image.size[1]) // 2)
	background.paste(image, point)

	return background

def _render(bg, img, x_offset=0, y_offset=0):
	point = (x_offset, y_offset)
	bg.paste(img, point)

# vim:set noet ts=2 sw=2:
