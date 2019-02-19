from big_ol_pile_of_manim_imports import *


def Celular():
    pad = SVGMobject(
        file_name = "mobile",
        fill_opacity = 1,
        stroke_width = 1,
        height = 8,
        stroke_color = WHITE,
    )
    pad[0].set_fill(WHITE)
    pad[1].set_fill(BLACK)
    pad[2].set_fill(None,0)
    pad[2].set_stroke(WHITE,0.5)
    pad[3].set_fill(BLACK)
    pad[4].set_fill(BLACK)
    pad[5].set_fill(BLACK)
    return pad

def Tu():
    dedo = SVGMobject(
            file_name = "tu",
            fill_opacity = 0,
            stroke_width = 0.2,
            height = 4,
            stroke_color = WHITE,
        )
    dedo[0].set_fill("#F4D7AB",1).set_stroke(None,3)
    dedo[1:].set_stroke(None,0.1)
    dedo[4:].set_fill("#EDCE9F",1)
    dedo[11:15].set_fill(WHITE,1)
    dedo[7].set_fill(BLACK,1)
    dedo[10].set_fill(BLACK,1)
    dedo[12:14].set_fill("#EDCE9F",1)
    return dedo


def MeGusta():
    MeGusta = SVGMobject(
    file_name = "like",
    fill_opacity = 1,
    stroke_width = 0,
    height = 3,
    stroke_color = WHITE,
    ).scale(0.8)
    MeGusta[0].set_fill("#0277bd",1)
    MeGusta[1].set_fill("#01579b",1)
    MeGusta[2].set_fill(WHITE,1)
    MeGusta[3].set_fill("#01579b",1)
    return MeGusta

def NoMeGusta():
    NoMeGusta=MeGusta().flip().rotate(np.pi)
    return NoMeGusta

def Dedo1():
    dedo=SVGMobject(
    file_name = "dedo",
    fill_opacity = 1,
    stroke_width = 0,
    height = 1,
    stroke_color = WHITE,
    )
    return dedo

def Dedo2():
    dedo=SVGMobject(
    file_name = "dedo2",
    fill_opacity = 1,
    stroke_width = 0,
    height = 1.3,
    stroke_color = WHITE,
    )
    return dedo


def Pin():
    pin=SVGMobject(
    file_name = "pin",
    fill_opacity = 1,
    stroke_width = 0,
    height = 3,
    stroke_color = WHITE,
    )
    pin[0].set_fill(RED_E,1)
    pin[1].set_fill(GRAY,1)
    pin[2].set_fill(RED,1)
    pin[3].set_fill(RED_E,1)
    pin[4].set_fill(RED_E,1)
    pin[5].set_fill(RED,1)
    pin.rotate(np.pi*0.1)
    return pin

def MP3():
    mp3=SVGMobject(file_name="mp3").scale(3)
    mp3[0].set_fill(RED,1)
    mp3[1].set_fill(BLUE,1)
    mp3[2].set_fill(WHITE,1)
    mp3[3].set_fill(WHITE,1)
    mp3[4:].set_fill(GRAY,1)
    return mp3
    
def TVA():
    return ImageMobject("tele1").scale(3)

def Cinta1():
    return ImageMobject("cinta1")


def Nota1():
    return ImageMobject("nota1")

def Audifonos():
    return SVGMobject(file_name="headphones").set_fill("#d1d5d5",1).scale(0.5)

def Avion():
    svg = SVGMobject(
            file_name = "avion1",
            fill_opacity = 1,
            stroke_width = 1.5,
            height = 1,
            stroke_color = TT_TEXTO,
        ).scale(2).set_fill(TT_TEXTO)
    return svg

def Palomitas():
    svg = SVGMobject(
            file_name = "palomitas",
            fill_opacity = 1,
            stroke_width = 0,
            height = 1,
            stroke_color = TT_TEXTO,
        ).scale(2)
    svg[0].set_fill("#efd35b")
    svg[1].set_fill("#f9e595")
    svg[2].set_fill("#f9e595").shift(RIGHT)
    svg[3:7].set_fill("#e2ba13")
    svg[7:11].set_fill("#f9e595")
    svg[15:23].set_fill(RED)
    svg[23].set_fill("#52a2e7")
    svg[24].set_fill("#ff6243")
    svg[25].set_fill("#3c66b1")
    svg[26].set_fill("#c6c3cb")
    svg[27].set_fill("#3c66b1",0.6)
    svg[28].set_fill("#9b2b00")
    return svg

def Luna():
    svg = SVGMobject(
            file_name = "moon",
            fill_opacity = 1,
            stroke_width = 0,
            height = 1,
            stroke_color = TT_TEXTO,
        ).scale(5)
    svg[3:6].set_fill("#999999")
    svg[6].set_fill("#ececec")
    svg[2].set_fill("#cccccc")
    return svg

def Planeta():
    svg = SVGMobject(
            file_name = "planeta1",
            fill_opacity = 1,
            stroke_width = 0,
            height = 1,
            stroke_color = TT_TEXTO,
        ).scale(5)
    svg[0].set_fill(BLUE)
    svg[1:].set_fill(GREEN)
    return svg

def Pad():
    svg = SVGMobject(
            file_name = "pad",
            fill_opacity = 1,
            stroke_width = 1.5,
            height = 1,
            color=TT_TEXTO,
            stroke_color = TT_TEXTO,
        ).scale(11)
    svg[1].set_fill(BLACK)
    return svg


def Pila():
    svg = SVGMobject(
            file_name = "battery",
            fill_opacity = 1,
            stroke_width = 1,
            height = 4,
            stroke_color = WHITE,
        )
    return svg

def Camara():
    svg = SVGMobject(
            file_name = "camera",
            fill_opacity = 1,
            stroke_width = 1,
            height = 4,
            stroke_color = WHITE,
        )
    return svg

def Reloj():
    svg = SVGMobject(
            file_name = "clock",
            fill_opacity = 1,
            stroke_width = 1,
            height = 4,
            stroke_color = WHITE,
        )
    return svg

def Cursor():
    svg = SVGMobject(
            file_name = "cursor",
            fill_opacity = 1,
            stroke_width = 1,
            height = 4,
            stroke_color = WHITE,
        )
    return svg

def Facebook():
    svg = SVGMobject(
            file_name = "facebook",
            fill_opacity = 1,
            stroke_width = 1,
            height = 4,
            stroke_color = WHITE,
        )
    return svg

def Ubicacion():
    svg = SVGMobject(
            file_name = "placeholder",
            fill_opacity = 1,
            stroke_width = 1,
            height = 4,
            stroke_color = WHITE,
        )
    return svg

def Twitter():
    svg = SVGMobject(
            file_name = "twitter",
            fill_opacity = 1,
            stroke_width = 1,
            height = 4,
            stroke_color = WHITE,
        )
    return svg

def YouTube():
    svg = SVGMobject(
            file_name = "youtube",
            fill_opacity = 1,
            stroke_width = 1,
            height = 4,
            stroke_color = WHITE,
        )
    return svg

def Basura():
    svg = SVGMobject(
            file_name = "trash",
            fill_opacity = 1,
            stroke_width = 1,
            height = 4,
            stroke_color = WHITE,
        )
    return svg

def GitHub():
    svg = SVGMobject(
            file_name = "github",
            fill_opacity = 1,
            stroke_width = 1,
            height = 4,
            stroke_color = WHITE,
        )
    return svg


def tecla_blanca():
    svg = SVGMobject(
            file_name = "tecla_blanca",
            fill_opacity = 1,
            stroke_width = 4,
            height = 1.37,
            stroke_color = BLACK,
        )
    svg.set_fill(WHITE,1)
    return svg

def tecla_negra():
    svg = SVGMobject(
            file_name = "tecla_negra",
            fill_opacity = 1,
            stroke_width = 4,
            height = 0.87,
            stroke_color = BLACK,
        )
    svg.set_fill(BLACK,1)
    return svg

class Caja(VMobject):
    def __init__(self,ancho=3,alto=2,tapas=0.95,grosor_tapas=11,**kwargs):
        digest_config(self, kwargs)
        VMobject.__init__(self, **kwargs)
        self.set_anchor_points([UP*alto+LEFT*ancho/2,
                                LEFT*ancho/2,
                                RIGHT*ancho/2,
                                UP*alto+RIGHT*ancho/2],mode="corners")
        self.set_stroke(width=6)
        tapaI=VMobject().set_anchor_points([self.points[0],self.points[0]+RIGHT*ancho*tapas/2],mode="corners").set_stroke(width=grosor_tapas)
        tapaD=VMobject().set_anchor_points([self.points[-1],self.points[-1]+LEFT*ancho*tapas/2],mode="corners").set_stroke(width=grosor_tapas)
        self.add(tapaI,tapaD)
        self.set_stroke("#D2B48C")
        self.set_fill("#D2B48C",0)

    def tapa_derecha(self):
        return self[2]

    def tapa_izquierda(self):
        return self[1]

class abrir_caja(Rotating):
    CONFIG={
        "run_time":0.75,
        "rate_func":smooth
    }    
    def update_mobject(self, alpha):
        Animation.update_mobject(self, alpha)
        sobre_izq=self.mobject.points[0]
        sobre_der=self.mobject.points[-1]
        self.mobject[1].rotate(
            alpha * PI*2.3/2,
            about_point=sobre_izq,
            about_edge=sobre_izq,
        )
        self.mobject[2].rotate(
            -alpha * PI*2.3/2,
            about_point=sobre_der,
            about_edge=sobre_der,
        )

class cerrar_caja(Rotating):
    CONFIG={
        "run_time":0.75,
        "rate_func":smooth
    }    
    def update_mobject(self, alpha):
        Animation.update_mobject(self, alpha)
        sobre_izq=self.mobject.points[0]
        sobre_der=self.mobject.points[-1]
        self.mobject[1].rotate(
            -alpha * PI*2.3/2,
            about_point=sobre_izq,
            about_edge=sobre_izq,
        )
        self.mobject[2].rotate(
            alpha * PI*2.3/2,
            about_point=sobre_der,
            about_edge=sobre_der,
        )
        
class Soporte(VGroup):
    def __init__(self,width,height,separacion=0.2,color=GREEN,agregar_base=False,direccion="R",grosor=1,stroke_width=2,**kwargs):
        digest_config(self, kwargs)
        VGroup.__init__(self, **kwargs)
        W=width
        H=height
        b=separacion
        if H>=W:
            n=0
            while n*b<W:
                x_i=W/2-n*b
                x_f=W/2
                pat=FunctionGraph(lambda x : x-W/2+n*b-H/2, 
                                    color = color,
                                    stroke_width = stroke_width,
                                    x_min = x_i,
                                    x_max = x_f
                                    )
                self.add(pat)
                n=n+1
            n=0
            while n*b<=H-W:
                x_f=W/2
                x_i=-W/2
                pat=FunctionGraph(lambda x : x-x_i+n*b-H/2, 
                                    color = color,
                                    stroke_width = stroke_width,
                                    x_min = x_i,
                                    x_max = x_f
                                    )
                self.add(pat)
                n=n+1
            while n*b-H/2<H/2:
                x_f=H-n*b+x_i
                x_i=-W/2
                pat=FunctionGraph(lambda x : x-x_i+n*b-H/2, 
                                    color = color,
                                    stroke_width = stroke_width,
                                    x_min = x_i,
                                    x_max = x_f
                                    )
                self.add(pat)
                n=n+1
        else:
            n=0
            while n*b-H/2<W+H/2:
                if n*b-H/2<H/2:
                    x_i=W/2-n*b
                    x_f=W/2
                if H/2<=n*b-H/2 and n*b-H/2<W-H/2:
                    x_i=W/2-n*b
                    x_f=H+W/2-n*b
                if W-H/2<=n*b-H/2 and n*b-H/2<W+H/2:
                    x_i=-W/2
                    x_f=H+W/2-n*b
                pat=FunctionGraph(lambda x : x-W/2+n*b-H/2, 
                                    color = color,
                                    stroke_width = stroke_width,
                                    x_min = x_i,
                                    x_max = x_f
                                    )
                self.add(pat)
                n=n+1
        if agregar_base==True:
            if direccion=="L":
                orientacion=LEFT
            elif direccion=="R":
                orientacion=RIGHT
            elif direccion=="U":
                orientacion=UP
            elif direccion=="D":
                orientacion=DOWN
            if direccion=="L" or direccion=="R":
                grosor=Rectangle(height=H,width=grosor).set_fill(color,1).set_stroke(None,0)
                grosor.shift(orientacion*W/2-orientacion*grosor.get_width()/2)
            else:
                grosor=Rectangle(height=grosor,width=W).set_fill(GREEN,1).set_stroke(None,0)
                grosor.shift(orientacion*H/2-orientacion*grosor.get_height()/2)
            self.add(grosor)
        
class Medicion(VGroup):
    CONFIG = {
        "color":RED_B,
        "buff":0.3,
        "laterales":0.3,
        "invertir":False,
        "dashed_segment_length":0.09,
        "dashed":True,
        "con_flechas":True,
        "ang_flechas":30*DEGREES,
        "tam_flechas":0.2,
    }
    def __init__(self,objeto,**kwargs):
        VGroup.__init__(self,**kwargs)
        if self.dashed==True:
            medicion=DashedLine(ORIGIN,objeto.get_length()*RIGHT,dashed_segment_length=self.dashed_segment_length)
        else:
            medicion=Line(ORIGIN,objeto.get_length()*RIGHT)

        pre_medicion=Line(ORIGIN,self.laterales*RIGHT).rotate(PI/2)
        pos_medicion=pre_medicion.copy()

        pre_medicion.move_to(medicion.get_start())
        pos_medicion.move_to(medicion.get_end())

        angulo=objeto.get_angle()
        matriz_rotacion=rotation_matrix(PI/2,OUT)
        vector_unitario=objeto.get_unit_vector()
        direccion=np.matmul(matriz_rotacion,vector_unitario)
        self.direccion=direccion

        self.add(medicion,pre_medicion,pos_medicion)
        self.rotate(angulo)
        self.move_to(objeto)
        if self.invertir==True:
            self.shift(-direccion*self.buff)
        else:
            self.shift(direccion*self.buff)
        self.set_color(self.color)
        

    def add_tips(self):
        linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
        vector_unitario=linea_referencia.get_unit_vector()

        punto_final1=self[0][-1].get_end()
        punto_inicial1=punto_final1-vector_unitario*self.tam_flechas

        punto_inicial2=self[0][0].get_start()
        punto_final2=punto_inicial2+vector_unitario*self.tam_flechas

        lin1_1=Line(punto_inicial1,punto_final1).set_color(self[0].get_color())
        lin1_2=lin1_1.copy()
        lin2_1=Line(punto_inicial2,punto_final2).set_color(self[0].get_color())
        lin2_2=lin2_1.copy()

        lin1_1.rotate(self.ang_flechas,about_point=punto_final1,about_edge=punto_final1)
        lin1_2.rotate(-self.ang_flechas,about_point=punto_final1,about_edge=punto_final1)

        lin2_1.rotate(self.ang_flechas,about_point=punto_inicial2,about_edge=punto_inicial2)
        lin2_2.rotate(-self.ang_flechas,about_point=punto_inicial2,about_edge=punto_inicial2)

        return self.add(lin1_1,lin1_2,lin2_1,lin2_2)

    def add_text(self,text,escala=1,buff=0.1,**moreargs):
        linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
        texto=TextMobject(text,**moreargs)
        ancho=texto.get_height()/2
        texto.rotate(linea_referencia.get_angle()).scale(escala).move_to(self)
        texto.shift(self.direccion*(buff+1)*ancho)
        return self.add(texto)

    def add_tex(self,texto,escala=1,buff=0.1,**moreargs):
        linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
        texto=TexMobject(text,**moreargs)
        ancho=texto.get_height()/2
        texto.rotate(linea_referencia.get_angle()).scale(escala).move_to(self)
        texto.shift(self.direccion*(buff+1)*ancho)
        return self.add(texto)

class Grilla(VGroup):
    CONFIG = {
        "rows":8,
        "columns":14,
        "height": FRAME_Y_RADIUS*2,
        "width": FRAME_X_RADIUS*2,
        "grid_stroke":0.5,
        "grid_color":WHITE,
        "axis_color":RED,
        "axis_stroke":2,
        "show_points":False,
        "point_radius":0,
        "labels_scale":0.5,
        "labels_buff":0,
        "number_decimals":2
    }

    def __init__(self,**kwargs):
        VGroup.__init__(self,**kwargs)
        rows=self.rows
        columns=self.columns
        grilla=Grid(width=self.width,height=self.height,rows=rows,columns=columns).set_stroke(self.grid_color,self.grid_stroke)

        vector_ii=ORIGIN+np.array((-FRAME_X_RADIUS,-FRAME_Y_RADIUS,0))
        vector_id=ORIGIN+np.array((FRAME_X_RADIUS,-FRAME_Y_RADIUS,0))
        vector_si=ORIGIN+np.array((-FRAME_X_RADIUS,FRAME_Y_RADIUS,0))
        vector_sd=ORIGIN+np.array((FRAME_X_RADIUS,FRAME_Y_RADIUS,0))

        ejes_x=Line(LEFT*FRAME_X_RADIUS,RIGHT*FRAME_X_RADIUS)
        ejes_y=Line(DOWN*FRAME_Y_RADIUS,UP*FRAME_Y_RADIUS)

        ejes=VGroup(ejes_x,ejes_y).set_stroke(self.axis_color,self.axis_stroke)

        divisiones_x=FRAME_X_RADIUS*2/columns
        divisiones_y=FRAME_Y_RADIUS*2/rows

        direcciones_buff_x=[UP,DOWN]
        direcciones_buff_y=[RIGHT,LEFT]
        dd_buff=[direcciones_buff_x,direcciones_buff_y]
        vectores_inicio_x=[vector_ii,vector_si]
        vectores_inicio_y=[vector_si,vector_sd]
        vectores_inicio=[vectores_inicio_x,vectores_inicio_y]
        tam_buff=[0,0]
        divisiones=[divisiones_x,divisiones_y]
        orientaciones=[RIGHT,DOWN]
        puntos=VGroup()
        leyendas=VGroup()


        for tipo,division,orientacion,coordenada,vi_c,d_buff in zip([columns,rows],divisiones,orientaciones,[0,1],vectores_inicio,dd_buff):
            for i in range(1,tipo):
                for v_i,direcciones_buff in zip(vi_c,d_buff):
                    ubicacion=v_i+orientacion*division*i
                    punto=Dot(ubicacion,radius=self.point_radius)
                    coord=round(punto.get_center()[coordenada],self.number_decimals)
                    leyenda=TextMobject("%s"%coord).scale(self.labels_scale)
                    leyenda.next_to(punto,direcciones_buff,buff=self.labels_buff)
                    puntos.add(punto)
                    leyendas.add(leyenda)

        self.add(grilla,ejes,leyendas)
        if self.show_points==True:
            self.add(puntos)
