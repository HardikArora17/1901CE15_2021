from fpdf import FPDF

path_to_logo=r'C:\Users\Dell\Desktop\1901CE15_2021\proj2\download.png'
path_to_text=r'C:\Users\Dell\Desktop\1901CE15_2021\proj2\19-iitpatna.jpg'
path_to_stamp=r"C:\Users\Dell\Desktop\1901CE15_2021\proj2\stamp.png"
path_to_sign=r"C:\Users\Dell\Desktop\1901CE15_2021\proj2\sign.png"

class PDF_MINER(FPDF):
    
    def rectangle(self,x1,y1,x2,y2):
        self.rect(x1,y1,x2,y2)
        
    def lines(self,x1,y1,x2,y2):
        self.set_line_width(0.0)
        self.line(x1,y1,x2,y2)
        
    def imagex_logo(self,o_x,o_y,w,h):
        self.set_xy(o_x,o_y)
        self.image(path_to_logo,  link='', type='', w=w-10, h=h-10)
        
    def stamp(self,o_x,o_y,w,h):
        self.set_xy(o_x,o_y)
        self.image(path_to_stamp,  link='', type='', w=w-10, h=h-10)
    
    def sign(self,o_x,o_y,w,h):
        self.set_xy(o_x,o_y)
        self.image(path_to_sign,  link='', type='', w=w-10, h=h-10)
        
    def imagex_main_text(self,o_x,o_y,w,h):
        self.set_xy(o_x,o_y)
        self.image(path_to_text,  link='', type='', w=w-15, h=h-10)
    
    def imagex_table(self,o_x,o_y,path_to_table,width=90,height=60):
        self.set_xy(o_x,o_y)
        self.image(path_to_table,  link='', type='', w=90, h=height)
    
    