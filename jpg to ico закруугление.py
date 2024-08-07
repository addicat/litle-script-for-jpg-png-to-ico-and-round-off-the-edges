from PIL import Image, ImageDraw
import sys

def convert_to_ico(input_path, output_path, size=256, radius_ratio=0.3):
    # Открываем изображение
    image = Image.open(input_path)
    
    # Преобразуем изображение в квадратное, если оно не является таковым
    size_min = min(image.size)
    image_cropped = image.crop(((image.width - size_min) // 2, (image.height - size_min) // 2, 
                                (image.width + size_min) // 2, (image.height + size_min) // 2))
    
    # Создаем маску для закругления краев с заданным радиусом
    radius = int(size * radius_ratio)  # Радиус закругления
    mask = Image.new('L', (size_min, size_min), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size_min, size_min), radius=radius, fill=255)
    
    # Применяем маску к изображению
    image_rounded = Image.new('RGBA', (size_min, size_min))
    image_rounded.paste(image_cropped, (0, 0), mask)
    
    # Увеличиваем изображение до нужного размера
    image_resized = image_rounded.resize((size, size), Image.LANCZOS)
    
    # Сохраняем изображение в формате ICO
    image_resized.save(output_path, format='ICO')
    print(f"Иконка сохранена по адресу: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(r"Использование: python convert_to_ico.py <путь_к_входному_файлу> <путь_к_выходному_файлу>")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        convert_to_ico(input_path, output_path)
