import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy

cube = ""
class Cube:
    x = 0
    y = 0
    z = 0
    vertices = [
        [0,0,0],
        [0,0,1],
        [0,1,0],
        [0,1,1],
        [1,0,0],
        [1,0,1],
        [1,1,0],
        [1,1,1]
        ]

    edges = (
        (0,1),
        (0,2),
        (0,4),
        (1,3),
        (1,5),
        (2,3),
        (2,6),
        (3,7),
        (4,5),
        (4,6),
        (5,7),
        (6,7)
    )

    surfaces = (
        (0,1,5,4),
        (0,1,3,2),
        (0,2,6,4),
        (4,5,7,6),
        (1,3,7,5),
        (2,3,7,6)
    )

    g = (0,1,0)
    b = (0,0,1)
    r = (1,0,0)
    w = (1,1,1)


    colors = [g,g,g,g,g,g]

    def __init__(self, mul=1, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.edges = Cube.edges
        self.vertices = list(numpy.multiply(numpy.array(Cube.vertices), mul))
        self.vertices = list(map(lambda vert: (vert[0] + x, vert[1] + y, vert[2] + z), self.vertices))
        self.surfaces = Cube.surfaces

    def draw(self):
        self.draw_sides()
        glLineWidth(3)
        glBegin(GL_LINES)
        #glPushMatrix()
        #glRotatef(45, 0, 0, 0)
        
        for edge in self.edges:
            for vertex in edge:
                glColor3f(0,0,0)
                glVertex3fv(self.vertices[vertex])
    
        #glPopMatrix()
        glEnd()

    def draw_sides(self):
        glBegin(GL_QUADS)
        i = 0
        for surface in self.surfaces:
            for vertex in surface:
                glColor3f(self.colors[i][0],self.colors[i][1],self.colors[i][2])
                glVertex3fv(self.vertices[vertex])
            i += 1

        glEnd()

    def move(self, x, y, z):
        self.vertices = list(map(lambda vert: (vert[0] + x, vert[1] + y, vert[2] + z), self.vertices))


def main():
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    glTranslatef(0,0,-20)
    glEnable(GL_DEPTH_TEST)

    p = []

#makes all of the smaller cubes
    for i in range(3):
        for j in range(3):
            for k in range(3):
                p.append(Cube(1,(i+1),(j+1),(k+1)))

#trying to make the colors only on the sides when solved
    # for c in p:
    #     if c.x == 3:
    #         print(True)
    #         c.colors = (p[0].b,p[0].w,p[0].w,p[0].w,p[0].w,p[0].w,p[0].w)
    p[26].colors = (p[0].w,p[0].w,p[0].w,p[0].w,p[0].w,p[0].w,p[0].w)
    #p[1].colors[1] = p[0].w

    vel = 0.1
    clock = pygame.time.Clock()
    x = 0
    viewAngle = 0
    glTranslate(-2.5, -2.5, 7)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            glTranslatef(-vel, 0, 0)
        if keys[pygame.K_RIGHT]:
            glTranslatef(vel, 0, 0)
        if keys[pygame.K_UP]:
            glTranslatef(0, vel, 0)
        if keys[pygame.K_DOWN]:
            glTranslatef(0, -vel, 0)
        if keys[pygame.K_t]:
            glTranslatef(0, 0, vel)
        if keys[pygame.K_g]:
            glTranslatef(0, 0, -vel)
        if keys[pygame.K_d]:
            glTranslate(2.5, 2.5, 2.5)
            glRotatef(1, 0,1,0)
            glTranslate(-2.5, -2.5, -2.5)
        if keys[pygame.K_a]:
            glTranslate(2.5, 2.5, 2.5)
            glRotatef(-1, 0,1,0)
            glTranslate(-2.5, -2.5, -2.5)
        if keys[pygame.K_w]:
            glTranslate(2.5, 2.5, 2.5)
            glRotatef(-1, 1,0,0)
            glTranslate(-2.5, -2.5, -2.5)
        if keys[pygame.K_s]:
            glTranslate(2.5, 2.5, 2.5)
            glRotatef(1, 1,0,0)
            glTranslate(-2.5, -2.5, -2.5)
        if keys[pygame.K_q]:
            glTranslate(2.5, 2.5, 2.5)
            glRotatef(1, 0,0,1)
            glTranslate(-2.5, -2.5, -2.5)
        if keys[pygame.K_e]:
            glTranslate(2.5, 2.5, 2.5)
            glRotatef(-1, 0,0,1)
            glTranslate(-2.5, -2.5, -2.5)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #x = 0
        #glRotatef(x, 1.0, 0.0, 1.0)
        y = 0
        for c in p:
            if c.x == 3 and x <= 90:
                glPushMatrix()
                glTranslate(0, 2.5, 2.5)
                glRotatef(x, 1, 0, 0)
                glTranslate(0, -2.5, -2.5)
                c.draw()
                glPopMatrix()
            else:
                c.draw()
            #c.draw()
            y+=1
        x += 1
        pygame.display.flip()


main()
