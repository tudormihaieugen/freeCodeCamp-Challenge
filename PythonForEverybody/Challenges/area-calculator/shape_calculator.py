class Rectangle:
    def __init__(self, width, height):
        # initialise width and height
        self.width = width
        self.height = height

    def set_width(self, width):
        # set the width
        self.width = width

    def set_height(self, height):
        # set the height
        self.height = height

    def get_area(self):
        # calculate the area
        area = self.width * self.height
        return area

    def get_perimeter(self):
        # calculate the perimeter
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        # calculate the diagonal
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        picture = ""
        # return error if too big
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        for line in range(self.height):
            for column in range(self.width):
                picture += "*"
            picture += "\n"
        return picture

    def get_amount_inside(self, shape):
        area = self.get_area()
        shape.area = shape.get_area()
        # calculate how many times the area of the given shape can fit
        return int(area / shape.area)

    def __str__(self):
        output = f"Rectangle(width={self.width}, height={self.height})"
        return output

class Square(Rectangle):
    def __init__(self, length):
        # get the init from Rectangle width = height = length
        Rectangle.__init__(self, length, length)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        output = f"Square(side={self.width})"
        return output
