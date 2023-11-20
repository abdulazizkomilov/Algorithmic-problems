import base64

class Image:
    def __init__(self, image):
        self.image: base64 = image
    
    def __repr__(self) -> str:
        return f"image: {self.image}"


class Text:
    def __init__(self, text):
        self.text = text

    def __repr__(self) -> str:
        return f"text: {self.text}"


class Comment(Text):
    def __init__(self, author, text):
        self.author = author
        self.text = text

    def __repr__(self) -> str:
        return f"comment: {self.author} - {self.text}"


class File:
    def __init__(self, file):
        self.file: base64 = file

    def __repr__(self) -> str:
        return f"file: {self.file}"


# class Page:
#     def __init__(self, image=None, text=None, comment=None, file=None):
#         self.image = image
#         self.text = text
#         self.comment = comment
#         self.file = file

#     def __str__(self) -> str:
#         return f"page: {self.image} {self.text} {self.comment} {self.file}"

class Page:
    def __init__(self, *args):
        self.obj_on_page = [*args]

    def add_obj(self, obj):
        self.obj_on_page.append(obj)

    def __repr__(self) -> str:
        return f"page: {[obj for obj in self.obj_on_page]}"



img = Image('test image')
txt = Text('text')
com = Comment('abdulaziz', 'commment txt')
fle = File('file')

page = Page()

page.add_obj(img)
page.add_obj(txt)
page.add_obj(com)
page.add_obj(fle)

if __name__ == '__main__':
    print(page)
    print(page.obj_on_page[0])