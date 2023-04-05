class MyType:
    def encode(self, image):
        ...
    def decode(self, bytes_):
        ...

collection.create_type('image', MyType())
collection.insert_many([{'im': im} for im in my_png_images])