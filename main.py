# from PIL import Image, ImageOps, ImageEnhance 

# with Image.open('images.jfif') as picture:
#     print('Размер:', picture.size)
#     print('Формат:', picture.format)
#     print('Режим:', picture.mode)

#     gray = ImageOps.grayscale(picture)
#     gray.save('gray.jpg')    
#     print('Размер:', gray.size)
#     print('Формат:', gray.format)
#     print('Режим:', gray.mode)

#     up = gray.rotate(180)
#     up.save('up.jpg')

#     image = ImageEnhance.Contrast(picture)
#     image = image.enhance(50)
#     image.save('image.jpg')

#     mirror_pic = ImageOps.mirror(picture)
#     mirror_pic.save('mirror_pic.jpg')

#     cut_pic = picture.crop([138, 0, 275, 92])
#     cut_pic.save('cut_pic.jpg')


#def mult(a):
#    return int(a) ** 2

#a = "12345"
# for i in range(len(a)):
#     a[i] = mult(a[i])
# print(a)
#print(list(map(mult, a)))

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageEnhance
import os


class ImageRuler:
    def __init__(self):
        self.image = None
        self.filename = None
        self.story = []

    def load_image(self, filename):
        self.filename = filename
        path = os.path.join(directory, filename)
        self.image = Image.open(path)
    
    def save_image(self):
        path = os.path.join(directory, 'modified')
        if not os.path.exists(path):
            os.mkdir(path) # создаем папку
        
        index = self.filename.rfind('.') # наоброт справа налево
        image_name = self.filename[:index] + '-new' + self.filename[index:]
        filename = os.path.join(path, image_name)
        self.image.save(os.path.join(path, image_name))
        set_picture(filename)

    def rotate_left(self):
        if self.image is None:
            return
        self.image = self.image.rotate(90)
        self.save_image()

    def rotate_right(self):
        if self.image is None:
            return
        self.image = self.image.rotate(-90)
        self.save_image()

    def do_black_white(self):
        if self.image is None:
            return
        self.image =self.image.convert('L')
        self.save_image()
    
    def do_contract(self):
        ...


image_ruler = ImageRuler()
directory = None


def chooseWorkDirectory():
    global directory

    directory = QFileDialog.getExistingDirectory(window, 'Выберите папку', os.getcwd()) # getcwd = get current work directory
    exts = ('.png', '.jpg', '.jpeg', '.jfif', '.webp', '.gif','.bmp' )  #расширения (extentions)
    files = os.listdir(directory)
    images = list(filter(lambda file: file.endswith(exts), files))
#                        функция                           список
    pic_list.addItems(images)

def show_image():
    if directory is None:
        return
    
    filename = pic_list.selectedItems()[0].text()
    set_picture(filename)

    image_ruler.load_image(filename)

def set_picture(filename):
    path = os.path.join(directory, filename)
    piximage = QPixmap(path)
    w, h = label.width(), label.height()
    piximage = piximage.scaled(w, h, Qt.KeepAspectRatio) # Qt.KeepAspectRatio - сохранять отношение сторон
    label.setPixmap(piximage)

app = QApplication([])
window = QWidget()
window.resize(800,600)    
window.setWindowTitle('Image Editor')

pic_list = QListWidget()
pic_list.itemClicked.connect(show_image)
label = QLabel('Картинка')

b_left = QPushButton('Лево')
b_left.clicked.connect(image_ruler.rotate_left)
b_right = QPushButton('Право')
b_right.clicked.connect(image_ruler.rotate_right)
b_mirror = QPushButton('Зеркало')
b_contrast = QPushButton('Резкость')
b_contrast.clicked.connect(image_ruler.do_contract)
b_black_white = QPushButton('Ч/Б')
b_black_white.clicked.connect(image_ruler.do_black_white)

b_file = QPushButton('Папка')
b_file.clicked.connect(chooseWorkDirectory)

main_line = QHBoxLayout()
line_button = QHBoxLayout()
vline1 = QVBoxLayout()
vline2 = QVBoxLayout()

line_button.addWidget(b_left)
line_button.addWidget(b_right)
line_button.addWidget(b_mirror)
line_button.addWidget(b_contrast)
line_button.addWidget(b_black_white)


vline1.addWidget(b_file)
vline1.addWidget(pic_list)

vline2.addWidget(label)
vline2.addLayout(line_button)

main_line.addLayout(vline1, 20)
main_line.addLayout(vline2, 80)

window.setLayout(main_line)



window.show()
app.exec()
