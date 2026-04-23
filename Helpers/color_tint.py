from picture import Picture

def tint(picture: Picture, r_offset: int, g_offset: int, b_offset: int) -> Picture:
    temp_pic = Picture(picture.width(), picture.height())

    for i in range(picture.height()):
        for j in range(picture.width()):
            pix = picture.get(j, i)
            r,g,b = pix.getRed() + r_offset, pix.getGreen() + g_offset, pix.getBlue() + b_offset
            new_pix = Color(r,g,b)
            temp_pic.set(j, i, new_pix)

def main() -> None:


if __name__ == "__main__": main()
