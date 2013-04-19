from random import randint
#could be divided into two in each axis
class cartor(object):
    def __init__(self , xs, ys, rs):
        self.res = rs
        self.xsz = xs#+100 #this way we dont go out of array
        self.ysz = ys#+100
        self.mulx = xs/rs
        self.muly = ys/rs
        self.cart = [[0 for i in range(rs+1)] for j in range(rs+1)]        

    def posr(self,px,py):
        xl = px/self.mulx
        yl = py/self.muly
        #xl = xl % self.res
        #yl = yl % self.res
        return [xl,yl]

    def look(self,px,py,act):
        loc = self.posr(px,py)
        if act == 1:
            print "I poked at %d %d" % (loc[0],loc[1])
            self.cart[loc[0]][loc[1]] += 1
        return self.cart[loc[0]][loc[1]]
    

    def nocks(self,px,py):
        print "where are your knocks? Gaaabe"
        loc = self.posr(px,py)
        x = loc[0]
        y = loc[1]

        cross = [0,0,0,0]
        # a little bad...
        if x-1 < 0:
            cross[0]=-1
        elif x >= self.res:
            cross[1]=-1
        else:
            cross[0] = self.cart[x+1][y]
            cross[1] = self.cart[x-1][y]

        if y-1 < 0:
            cross[2]=-1
        elif y >= self.res:
            cross[3]=-1
        else:
            cross[2] = self.cart[x][y+1]
            cross[3] = self.cart[x][y-1]
        
        return cross
    
    def revpos(self):
        return False


    def rantest(self, it):
        for i in range(0,it):
            self.look(randint(0,self.xsz),randint(0,self.ysz),1)
        print "random map"


    def sumer(self):
        return sum(sum(x) for x in self.cart)
