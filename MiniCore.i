set title "firstTrial"

%--- PINS DEFINITIONS
pin 1 
m1   1.0000 
m2   2.0000 
m3  

%--- ASSEMBLIES DEFINITIONS
lat assm1 1 0.0 0.0 3 3 1.30
1 1 1 
1 1 1 
1 1 1 

lat assm3 1 0.0 0.0 3 3 1.30
1 1 1 
1 1 1 
1 1 1 

%--- SUPER-CELL DEFINITION
lat sc 1 0.0 0.0 2 2 12.34
assm1 assm3 
assm3 assm1 

surf 5 cuboid -160.65 160.65 -160.65 160.65 -10.71 10.71 
cell 98  0 fill sc   -5
cell 99  0 outside   5
set bc 1 1 2
