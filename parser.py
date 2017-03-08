from display import *
from matrix import *
from draw import *
from time import sleep

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 yrotate: create an y-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 zrotate: create an z-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""

hasNumericArgs = ["line", "scale", "move", "rotate"]

def parse_file( fname, points, transform, screen, color ):
    f = open(fname)
    cmd = f.readline().strip()
    args = ""

    while cmd: #file not empty
        if cmd in hasNumericArgs:
            args = f.readline()
            args = processArgLine(args)
        if cmd == "line":
             add_edge(points, args[0], args[1], args[2], args[3], args[4], args[5])
        elif cmd == "scale":
            mat = make_scale(args[0], args[1], args[2])
            matrix_mult(mat, transform)
        elif cmd == "move":
            mat = make_translate(args[0], args[1], args[2])
            matrix_mult(mat, transform)
        elif cmd == "rotate":
            if args[0] == "x":
                mat = make_rotX(args[1])
            elif args[0] == "y":
                mat = make_rotY(args[1])
            else:
                mat = make_rotZ(args[1])
            matrix_mult(mat, transform)
        elif cmd == "ident":
            ident(transform)
        elif cmd == "apply":
            matrix_mult(transform, points)
        elif cmd == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            sleep(1)
        elif cmd == "save":
            args = f.readline().strip()
            save_extension( screen, args )
        cmd = f.readline().strip()
        args = ""


def processArgLine(args):
    args = args.strip().split(" ")
    i = 0
    while i < len(args):
        try:
            args[i] = int(args[i])
        except:
            pass
        i += 1
    return args
