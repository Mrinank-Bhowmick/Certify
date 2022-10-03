from PIL import Image, ImageDraw, ImageFont
import os
import csv

def generate_certificate(name, course, date, certificate_number):
    certificate = Image.open('certificate_template.png')
    draw = ImageDraw.Draw(certificate)
    font = ImageFont.truetype('arial.ttf', size=50)
    date_font = ImageFont.truetype('arial.ttf', size=30)
    certificate_number_font = ImageFont.truetype('arial.ttf', size=30)

    width, height = certificate.size

    name_width, name_height = draw.textsize(name, font=font)

    date_width, date_height = draw.textsize(date, font=date_font)

    certificate_number_width, certificate_number_height = draw.textsize(certificate_number, font=certificate_number_font)

    course_width, course_height = draw.textsize(course, font=font)

    name_x = (width - name_width) / 2
    name_y = (height - name_height) / 2

    date_x = (width - date_width) / 2
    date_y = (height - date_height) / 2 + 100

    certificate_number_x = (width - certificate_number_width) / 2
    certificate_number_y = (height - certificate_number_height) / 2 + 150

    course_x = (width - course_width) / 2
    course_y = (height - course_height) / 2 + 50

    draw.text((name_x, name_y), name, fill='rgb(0, 0, 0)', font=font)

    draw.text((date_x, date_y), date, fill='rgb(0, 0, 0)', font=date_font)

    draw.text((certificate_number_x, certificate_number_y), certificate_number, fill='rgb(0, 0, 0)', font=certificate_number_font)

    draw.text((course_x, course_y), course, fill='rgb(0, 0, 0)', font=font)

    certificate.save('certificate.png')

def read_csv():
    with open('data.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            name, course, date, certificate_number = row
            generate_certificate(name, course, date, certificate_number)

def create_directory():
    os.mkdir('certificates')

def move_certificate():
    os.rename('certificate.png', 'certificates/certificate.png')

def run():
    create_directory()
    read_csv()
    move_certificate()

if __name__ == '__main__':
    run()