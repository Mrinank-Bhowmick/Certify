#!/usr/bin/env python
import os
import csv
import argparse
import pathlib
from PIL import Image, ImageDraw, ImageFont


class CertificateGenerator(object):
    def __init__(self, template_path, font_path, certificate_path):
        self.template_path = template_path
        self.font_path = font_path
        self.certificate_path = certificate_path

    def generate_certificate(self, name, course, date, certificate_number):
        if not os.path.isfile(self.template_path):
            raise FileNotFoundError('No template')
    
        certificate = Image.open(self.template_path)
        draw = ImageDraw.Draw(certificate)
        font = ImageFont.truetype(str(self.font_path), size=50)
        date_font = ImageFont.truetype(str(self.font_path), size=30)
        certificate_number_font = ImageFont.truetype(str(self.font_path), size=30)
    
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
    
        certificate.save(self.certificate_path)

def create_directory(path):
    if os.path.isdir(path):
        print(f"{path} directory exits")
    else:
        os.mkdir(path)

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--template_path', type=pathlib.Path, required=False, default='template/certificate_template.png')
    parser.add_argument('--font_path', type=pathlib.Path, default='font/arial.ttf')
    parser.add_argument('--certificate_path', type=pathlib.Path, default='certificates/certificate.png')
    parser.add_argument('--data_path', type=pathlib.Path, default='data/data.csv')

    args = parser.parse_args()

    certificates_directory = os.path.dirname(args.certificate_path)
    create_directory(certificates_directory)

    generator = CertificateGenerator(args.template_path, args.font_path, args.certificate_path)

    with open(args.data_path, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            name, course, date, certificate_number = row
            generator.generate_certificate(name, course, date, certificate_number)

    

    

if __name__ == '__main__':
    run()