from naverimagejson import NaverImage

image_object = NaverImage()
search = input('검색할 이미지 : ')
image_object.setQuery(search)
image_object.getImage()
