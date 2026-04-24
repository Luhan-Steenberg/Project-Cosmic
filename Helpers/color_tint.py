from picture import Picture
from color import Color
import stddraw

def tint(picture: Picture,
         r_offset: int,
         g_offset: int,
         b_offset: int) -> Picture:
    temp_pic = Picture(picture.width(), picture.height())

    for i in range(picture.height()):
        for j in range(picture.width()):
            pix = picture.get(j, i)

            if pix.getRed() == 0 and pix.getGreen() == 0 and pix.getBlue() == 0:
            # Copy the background exactly as-is and skip to the next pixel
                temp_pic.set(j, i, pix)
                continue
            if pix.getRed() == 255 and pix.getGreen() == 255 and pix.getBlue() == 255:
            # Copy the background exactly as-is and skip to the next pixel
                temp_pic.set(j, i, pix)
                continue

            r = min(pix.getRed()   + r_offset, 255)
            g = min(pix.getGreen() + g_offset, 255)
            b = min(pix.getBlue()  + b_offset, 255)

            new_pix = Color(r,g,b)
            temp_pic.set(j, i, new_pix)

    return temp_pic

def main() -> None:
    picture = Picture("alien.png")
    stddraw.picture(picture)
    stddraw.show(2000)
    picture = tint(picture, 100, 0, 0)
    stddraw.picture(picture)
    stddraw.show()


if __name__ == "__main__": main()
