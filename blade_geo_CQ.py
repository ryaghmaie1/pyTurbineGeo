import cadquery as cq

# z axis line length 100.0
path = cq.Workplane("XZ").moveTo(0, 0).lineTo(0, 30)

# read airfoil data into float
with open("D:\Rutgers\F-ARPA-software\CAD\CQ-editor\WindTurbine\s814825_50_x.dat", "r") as AFfile_x:
    AFdata_x = [float(i) for line in AFfile_x for i in line.split(',') if i.strip()]
with open("D:\Rutgers\F-ARPA-software\CAD\CQ-editor\WindTurbine\s814825_50_y.dat", "r") as AFfile_y:
    AFdata_y = [float(i) for line in AFfile_y for i in line.split(',') if i.strip()]

AFdata_x1=[0]*65
AFdata_y1=[0]*65
AFdata_x2=[0]*65
AFdata_y2=[0]*65
AFdata_x3=[0]*65
AFdata_y3=[0]*65
AFdata_x4=[0]*65
AFdata_y4=[0]*65

for i in range(0,len(AFdata_x)):
    AFdata_x1[i]=3*(AFdata_x[i]-1.0/3)
    AFdata_x2[i]=2*(AFdata_x[i]-1.0/3)
    AFdata_x3[i]=1*(AFdata_x[i]-1.0/3)
    AFdata_x4[i]=0.5*(AFdata_x[i]-1.0/3)

for i in range(0,len(AFdata_y)):
    AFdata_y1[i]=3*AFdata_y[i]
    AFdata_y2[i]=2*AFdata_y[i]
    AFdata_y3[i]=1*AFdata_y[i]
    AFdata_y4[i]=0.5*AFdata_y[i]


#print(AFdata_x1)


# Sweep a circle from diameter 2.0 to diameter 1.0 to diameter 2.0 along X axis length 10.0 + 10.0
Blade_Sweep = (
    cq.Workplane("XY")
    .workplane(offset=0.0)
    .circle(1.0)
    
    .workplane(offset=10.0)
    .moveTo(AFdata_x1[0],AFdata_y1[0])
    .moveTo(AFdata_x1[1],AFdata_y1[1])
    .moveTo(AFdata_x1[2],AFdata_y1[2])
#    .lineTo(AFdata_x1[3],AFdata_y1[3])
    .moveTo(AFdata_x1[4],AFdata_y1[4])
    .moveTo(AFdata_x1[5],AFdata_y1[5])
    .lineTo(AFdata_x1[6],AFdata_y1[6])
    .lineTo(AFdata_x1[9],AFdata_y1[9])
    .lineTo(AFdata_x1[12],AFdata_y1[12])
    .lineTo(AFdata_x1[15],AFdata_y1[15])
    .lineTo(AFdata_x1[18],AFdata_y1[18])
    .lineTo(AFdata_x1[21],AFdata_y1[21])
    .lineTo(AFdata_x1[22],AFdata_y1[22])
    .lineTo(AFdata_x1[23],AFdata_y1[23])
    .lineTo(AFdata_x1[24],AFdata_y1[24])
    .lineTo(AFdata_x1[25],AFdata_y1[25])
    .lineTo(AFdata_x1[26],AFdata_y1[26])
    .lineTo(AFdata_x1[27],AFdata_y1[27])
    .lineTo(AFdata_x1[28],AFdata_y1[28])
    .lineTo(AFdata_x1[29],AFdata_y1[29])
    .lineTo(AFdata_x1[30],AFdata_y1[30])
    .lineTo(AFdata_x1[31],AFdata_y1[31])
    .lineTo(AFdata_x1[32],AFdata_y1[32])
    .lineTo(AFdata_x1[33],AFdata_y1[33])
    .lineTo(AFdata_x1[34],AFdata_y1[34])
    .lineTo(AFdata_x1[35],AFdata_y1[35])
    .lineTo(AFdata_x1[36],AFdata_y1[36])
    .lineTo(AFdata_x1[37],AFdata_y1[37])
    .lineTo(AFdata_x1[38],AFdata_y1[38])
    .lineTo(AFdata_x1[39],AFdata_y1[39])
    .lineTo(AFdata_x1[40],AFdata_y1[40])
    .lineTo(AFdata_x1[41],AFdata_y1[41])
    .lineTo(AFdata_x1[42],AFdata_y1[42])
    .lineTo(AFdata_x1[43],AFdata_y1[43])
    .lineTo(AFdata_x1[44],AFdata_y1[44])
    .lineTo(AFdata_x1[45],AFdata_y1[45])
    .lineTo(AFdata_x1[46],AFdata_y1[46])
    .lineTo(AFdata_x1[47],AFdata_y1[47])
    .lineTo(AFdata_x1[48],AFdata_y1[48])
    .lineTo(AFdata_x1[49],AFdata_y1[49])
    .lineTo(AFdata_x1[50],AFdata_y1[50])
    .lineTo(AFdata_x1[51],AFdata_y1[51])
    .lineTo(AFdata_x1[52],AFdata_y1[52])
    .lineTo(AFdata_x1[53],AFdata_y1[53])
    .lineTo(AFdata_x1[54],AFdata_y1[54])
    .lineTo(AFdata_x1[55],AFdata_y1[55])
    .lineTo(AFdata_x1[56],AFdata_y1[56])
    .lineTo(AFdata_x1[57],AFdata_y1[57])
#    .lineTo(AFdata_x1[60],AFdata_y1[60])
#    .lineTo(AFdata_x1[63],AFdata_y1[63])
    .close()
    
    .workplane(offset=10.0)
    .moveTo(AFdata_x2[0],AFdata_y2[0])
    .moveTo(AFdata_x2[1],AFdata_y2[1])
    .moveTo(AFdata_x2[2],AFdata_y2[2])
#    .lineTo(AFdata_x2[3],AFdata_y2[3])
    .moveTo(AFdata_x2[4],AFdata_y2[4])
    .moveTo(AFdata_x2[5],AFdata_y2[5])
    .lineTo(AFdata_x2[6],AFdata_y2[6])
    .lineTo(AFdata_x2[9],AFdata_y2[9])
    .lineTo(AFdata_x2[12],AFdata_y2[12])
    .lineTo(AFdata_x2[15],AFdata_y2[15])
    .lineTo(AFdata_x2[18],AFdata_y2[18])
    .lineTo(AFdata_x2[21],AFdata_y2[21])
    .lineTo(AFdata_x2[22],AFdata_y2[22])
    .lineTo(AFdata_x2[23],AFdata_y2[23])
    .lineTo(AFdata_x2[24],AFdata_y2[24])
    .lineTo(AFdata_x2[25],AFdata_y2[25])
    .lineTo(AFdata_x2[26],AFdata_y2[26])
    .lineTo(AFdata_x2[27],AFdata_y2[27])
    .lineTo(AFdata_x2[28],AFdata_y2[28])
    .lineTo(AFdata_x2[29],AFdata_y2[29])
    .lineTo(AFdata_x2[30],AFdata_y2[30])
    .lineTo(AFdata_x2[31],AFdata_y2[31])
    .lineTo(AFdata_x2[32],AFdata_y2[32])
    .lineTo(AFdata_x2[33],AFdata_y2[33])
    .lineTo(AFdata_x2[34],AFdata_y2[34])
    .lineTo(AFdata_x2[35],AFdata_y2[35])
    .lineTo(AFdata_x2[36],AFdata_y2[36])
    .lineTo(AFdata_x2[37],AFdata_y2[37])
    .lineTo(AFdata_x2[38],AFdata_y2[38])
    .lineTo(AFdata_x2[39],AFdata_y2[39])
    .lineTo(AFdata_x2[40],AFdata_y2[40])
    .lineTo(AFdata_x2[41],AFdata_y2[41])
    .lineTo(AFdata_x2[42],AFdata_y2[42])
    .lineTo(AFdata_x2[43],AFdata_y2[43])
    .lineTo(AFdata_x2[44],AFdata_y2[44])
    .lineTo(AFdata_x2[45],AFdata_y2[45])
    .lineTo(AFdata_x2[46],AFdata_y2[46])
    .lineTo(AFdata_x2[47],AFdata_y2[47])
    .lineTo(AFdata_x2[48],AFdata_y2[48])
    .lineTo(AFdata_x2[49],AFdata_y2[49])
    .lineTo(AFdata_x2[50],AFdata_y2[50])
    .lineTo(AFdata_x2[51],AFdata_y2[51])
    .lineTo(AFdata_x2[52],AFdata_y2[52])
    .lineTo(AFdata_x2[53],AFdata_y2[53])
    .lineTo(AFdata_x2[54],AFdata_y2[54])
    .lineTo(AFdata_x2[55],AFdata_y2[55])
    .lineTo(AFdata_x2[56],AFdata_y2[56])
    .lineTo(AFdata_x2[57],AFdata_y2[57])
#    .lineTo(AFdata_x2[60],AFdata_y2[60])
#    .lineTo(AFdata_x2[63],AFdata_y2[63])
    .close()
    
    .workplane(offset=10.0)
    .moveTo(AFdata_x3[0],AFdata_y3[0])
    .moveTo(AFdata_x3[1],AFdata_y3[1])
    .moveTo(AFdata_x3[2],AFdata_y3[2])
#    .lineTo(AFdata_x3[3],AFdata_y3[3])
    .moveTo(AFdata_x3[4],AFdata_y3[4])
    .moveTo(AFdata_x3[5],AFdata_y3[5])
    .lineTo(AFdata_x3[6],AFdata_y3[6])
    .lineTo(AFdata_x3[9],AFdata_y3[9])
    .lineTo(AFdata_x3[12],AFdata_y3[12])
    .lineTo(AFdata_x3[15],AFdata_y3[15])
    .lineTo(AFdata_x3[18],AFdata_y3[18])
    .lineTo(AFdata_x3[21],AFdata_y3[21])
    .lineTo(AFdata_x3[22],AFdata_y3[22])
    .lineTo(AFdata_x3[23],AFdata_y3[23])
    .lineTo(AFdata_x3[24],AFdata_y3[24])
    .lineTo(AFdata_x3[25],AFdata_y3[25])
    .lineTo(AFdata_x3[26],AFdata_y3[26])
    .lineTo(AFdata_x3[27],AFdata_y3[27])
    .lineTo(AFdata_x3[28],AFdata_y3[28])
    .lineTo(AFdata_x3[29],AFdata_y3[29])
    .lineTo(AFdata_x3[30],AFdata_y3[30])
    .lineTo(AFdata_x3[31],AFdata_y3[31])
    .lineTo(AFdata_x3[32],AFdata_y3[32])
    .lineTo(AFdata_x3[33],AFdata_y3[33])
    .lineTo(AFdata_x3[34],AFdata_y3[34])
    .lineTo(AFdata_x3[35],AFdata_y3[35])
    .lineTo(AFdata_x3[36],AFdata_y3[36])
    .lineTo(AFdata_x3[37],AFdata_y3[37])
    .lineTo(AFdata_x3[38],AFdata_y3[38])
    .lineTo(AFdata_x3[39],AFdata_y3[39])
    .lineTo(AFdata_x3[40],AFdata_y3[40])
    .lineTo(AFdata_x3[41],AFdata_y3[41])
    .lineTo(AFdata_x3[42],AFdata_y3[42])
    .lineTo(AFdata_x3[43],AFdata_y3[43])
    .lineTo(AFdata_x3[44],AFdata_y3[44])
    .lineTo(AFdata_x3[45],AFdata_y3[45])
    .lineTo(AFdata_x3[46],AFdata_y3[46])
    .lineTo(AFdata_x3[47],AFdata_y3[47])
    .lineTo(AFdata_x3[48],AFdata_y3[48])
    .lineTo(AFdata_x3[49],AFdata_y3[49])
    .lineTo(AFdata_x3[50],AFdata_y3[50])
    .lineTo(AFdata_x3[51],AFdata_y3[51])
    .lineTo(AFdata_x3[52],AFdata_y3[52])
    .lineTo(AFdata_x3[53],AFdata_y3[53])
    .lineTo(AFdata_x3[54],AFdata_y3[54])
    .lineTo(AFdata_x3[55],AFdata_y3[55])
    .lineTo(AFdata_x3[56],AFdata_y3[56])
    .lineTo(AFdata_x3[57],AFdata_y3[57])
#    .lineTo(AFdata_x3[60],AFdata_y3[60])
#    .lineTo(AFdata_x3[63],AFdata_y3[63])
    .close()
    .sweep(path, multisection=True, makeSolid=False)
)

# Translate the resulting solids so that they do not overlap and display them left to right
#show_object(Blade_Sweep)



# Export
cq.exporters.export(Blade_Sweep,'Blade.stl')
cq.exporters.export(Blade_Sweep.section(),'Blade.dxf')
cq.exporters.export(Blade_Sweep,'Blade.step')


