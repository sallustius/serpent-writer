set title "input"

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%			 GEOMETRY
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%--- Pins
pin ff 
fuel   0.4100 
water   0.4750 
clad  

%--- Assemblies
lat a1 1 0.0 0.0 17 17 1.26
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 

lat a2 1 0.0 0.0 17 17 1.26
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 

%--- Super-Cell
lat Super 1 0.0 0.0 2 2 21.42
a1 a2 a1 a2 
a1 a2 a2 a2 
a1 a2 a2 a2 
a1 a2 a2 a2 

surf 5 cuboid -42.84 42.84 -42.84 42.84 -10.71 10.71 
cell 98  0 fill Super   -5
cell 99  0 outside   5
set bc 1 1 2
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%			 MATERIALS
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

mat fuel -10.9
92235.09c 1.0
92238.09c 1.0
92239.09c 1.0

mat water -0.700452 moder lwtr 1001
1001.06c 0.6666667
8016.06c 0.3333333

mat clad -6.5
40000.06c 1.0

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%			 SETTINGS
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

set pop 100000 100 50 1.0 
% -- Cross-sections
set acelib "/nv/hp22/dkotlyar6/data/Codes/DATA/sss_endfb7u.xsdata"
set ures 1 3 92238.09c 
set nfg 1
ene ciao 1 0 20

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%			 FISSION MATRIX
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

set fmtx 4 -21.42 21.42 17 -21.42 21.42 17 -1.00e+37 1.00e+37 1
