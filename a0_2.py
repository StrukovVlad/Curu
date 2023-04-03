"""Перевод pdf файла в аудио mp3"""
import pyttsx3
import pdfplumber as pp

engine = pyttsx3.init()

all_data = ''

with pp.open('example.pdf') as book:
    for page_no, page in enumerate(book.pages, start=1):
        data = page.extract.text()
        all_data += data

engine.save_to_file(all_data, 'audio_book.mp3')
engine.runAndWait()
engine.stop()
______________________________________________________________________________________
import click

def format_docstring(*args):
    def decorator(func):
        func.__doc__%=args
        return func
    return decorator


@click.command()
@format_docstring("world")
def hello():
    """Hello %s"""
    click.echo("Htllo who?")

if __name__ == '__main__':
    hello()

from rembg import remove
from PIL import Image
from pathlib import Path


def remove_bg():
    list_of_extensions = ['*.png', '*.jpg']
    all_files = []

    for ext in list_of_extensions:
        all_files.extend(Path('input_imgs').glob(ext))

    for index, item in enumerate(all_files):
        input_path = Path(item)
        file_name = input_path.stem

        output_path = f'output_imgs/{file_name}_output.png'

        input_img = Image.open(input_path)
        output_img = remove(input_img)
        output_img.save(output_path)

        print(f'Completed: {index + 1}/{len(all_files)}')


def main():
    remove_bg()


if __name__ == '__main__':
    main()

