#coding: utf-8

class AllwinnerSoC_Logo():
    def __init__(self, template_path):
        self.template_svg = ""
        self.load_template_svg(template_path)
    
    def load_template_svg(self, template_path):
        self.template_svg = open(template_path, "r").read()
    
    def calculate_text_y_position(self, chip_soc_name):
        if(chip_soc_name <= 4):
            return 75
        elif(chip_soc_name <= 5):
            return 69
        elif(chip_soc_name <= 7):
            return 68
    
    def calculate_text_px(self, chip_soc_name):
        if(chip_soc_name <= 4):
            return 32
        elif(chip_soc_name <= 5):
            return 22
        elif(chip_soc_name <= 6):
            return 20
        elif(chip_soc_name <= 7):
            return 18
    
    def generate(self, chip_soc_name):
        generate = self.template_svg.replace("{{{CHIPNAME_HERE}}}", chip_soc_name)
        generate = generate.replace("{{{TEXT_Y_POSITION_HERE}}}", str(self.calculate_text_y_position(len(chip_soc_name))))
        generate = generate.replace("{{{TEXT_PX_HERE}}}", str(self.calculate_text_px(len(chip_soc_name))))
        return generate
    
    def generate_to_file(self, chip_soc_name, output_svg_path):
        generate = self.generate(chip_soc_name)
        open(output_svg_path, "w").write(generate)

if __name__ == "__main__":
    # Usage: python allwinnersoclogo.py <output_svg_path> <chip_soc_name>
    # Example: python allwinnersoclogo.py output.svg "A64"
    import sys

    if len(sys.argv) != 3:
        print("Usage: python allwinnersoclogo.py <output_svg_path> <chip_soc_name>")
        print("Example: python allwinnersoclogo.py output.svg \"A64\"")
        sys.exit(1)
    
    output_svg_path = sys.argv[1]
    chip_soc_name = sys.argv[2]

    allwinner_soc_logo = AllwinnerSoC_Logo("template.svg")
    allwinner_soc_logo.generate_to_file(chip_soc_name, output_svg_path)
