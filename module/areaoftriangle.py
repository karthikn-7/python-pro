class triangle():
    def __init__(self,triangle_no,b,h):
        self.b = b
        self.h = h
        self.triangle_no = triangle_no
        self.t = "Triangle"
    
    def area_Of_triangle(self):
        area = self.b * self.h * 1/2
        print(self.t,self.triangle_no,":",area)
    

triangle1 = triangle(1,11, 10)
triangle1.area_Of_triangle()

triangle2 = triangle(2,21, 20)
triangle2.area_Of_triangle()

triangle3 = triangle(3, 31, 30)
triangle3.area_Of_triangle()