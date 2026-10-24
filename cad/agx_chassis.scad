// AgriGuardian X parametric concept. Units mm. NOT as-built geometry.
$fn=44;
exploded = is_undef(exploded) ? 0 : exploded;
L=450; W=280; wheel_r=45; wheel_thick=24;
module tube_x(len){color([.18,.28,.35]) cube([len,20,20],center=true);}
module wheel(){color([.84,.64,.12]) rotate([90,0,0]) cylinder(h=wheel_thick,r=wheel_r,center=true); color([.12,.14,.17]) rotate([90,0,0]) cylinder(h=wheel_thick+1,r=13,center=true);}
module frame(){
 for(y=[-W/2+18,W/2-18]) for(z=[0,75]) translate([0,y,z]) tube_x(L);
 for(x=[-L/2+12,L/2-12]) for(z=[0,75]) translate([x,0,z]) rotate([0,0,90]) tube_x(W-16);
 color([.2,.35,.37]) translate([0,0,95]) cube([300,200,6],center=true);
}
module chassis(){frame();
 for(x=[-165,0,165])for(y=[-W/2-12,W/2+12]) translate([x,y,-35]) wheel();
 color([.12,.45,.32]) translate([-45,0,122+exploded*45]) cube([115,85,22],center=true);
 color([.12,.16,.18]) translate([88,0,122+exploded*90]) cube([100,70,36],center=true);
 color([.15,.22,.25]) translate([155,0,145+exploded*120]) cube([22,22,100],center=true);
 color([.06,.08,.09]) translate([155,0,203+exploded*120]) cube([42,38,30],center=true);
}
chassis();