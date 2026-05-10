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


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageOps
import os


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
    path = os.path.join(directory, filename)
    piximage = QPixmap(path)
    w, h = label.width(), label.height()
    piximage = piximage.scaled(w, h)
    label.setPixmap(piximage)
 

app = QApplication([])
window = QWidget()
window.resize(800,600)    
window.setWindowTitle('Image Editor')

pic_list = QListWidget()
pic_list.itemClicked.connect(show_image)
label = QLabel('Картинка')

b_left = QPushButton('Лево')
b_right = QPushButton('Право')
b_mirror = QPushButton('Зеркало')
b_contrast = QPushButton('Резкость')
b_black_white = QPushButton('Ч/Б')

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