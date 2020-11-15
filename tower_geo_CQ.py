import cadquery as cq

# z axis line length 100.0
path = cq.Workplane("XZ").moveTo(0, 0).lineTo(0, 100)

# Sweep a circle from diameter 2.0 to diameter 1.0 to diameter 2.0 along X axis length 10.0 + 10.0
Tower_Sweep = (
    cq.Workplane("XY")
    .workplane(offset=0.0)
    .circle(2.5)
    .workplane(offset=100.0)
    .circle(1.75)
    .sweep(path, multisection=True, makeSolid=False)
)

# Translate the resulting solids so that they do not overlap and display them left to right
#show_object(Tower_Sweep)

# Export
cq.exporters.export(Tower_Sweep,'Tower.stl')
cq.exporters.export(Tower_Sweep.section(),'Tower.dxf')
cq.exporters.export(Tower_Sweep,'Tower.step')
