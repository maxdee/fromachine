
class cartor(object):
    def __init__(self , xs, ys, rs):
        self.res = rs
        self.xsz = xs
        self.ysz = ys
        self.cart = [[0 for i in range(rs)] for j in range(rs)]        

    def look(self,px,py,act):
        xl = int((px/self.xsz)*self.res)
        yl = int((px/self.ysz)*self.res)
        xl = xl % self.res
        yl = yl % self.res
        if act == 1:
            print "I poked at %d %d" % (xl,yl)
            self.cart[xl][yl] += 1
        return self.cart[xl][yl]
