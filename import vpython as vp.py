import vpython as vp
vp.scene.userzoom=False
#######
#set the launch velocity (change this)
v0=4000
#######

Me = 5.972e24 #kg
Re=6.371e6 #m
G=6.67e-11


earth=vp.sphere(pos=vp.vector(0,0,0), radius=Re, texture=vp.textures.earth)
mtnewton=vp.pyramid(pos=Re*vp.norm(vp.vector(.143,1.18,0)), size=vp.vector(.19*Re,.19*Re,.486*Re),axis=vp.norm(vp.vector(.143,1.18,0)))

balla=vp.sphere(pos=Re*vp.vector(.143,1.18,0),radius=Re/20, color=vp.color.yellow, make_trail=True)

balla.v=v0*vp.norm(vp.cross(balla.pos,vp.vector(0,0,1)))
m=1
balla.p=m*balla.v

vp.scene.camera.pos=vp.scene.camera.pos+vp.vector(0,3e6,0)


t=0
dt=1
while vp.mag(balla.pos)>Re:
  vp.rate(1000)
  ra=balla.pos-earth.pos
  Fa=-G*Me*m*ra/vp.mag(ra)**3
  balla.p=balla.p+Fa*dt
  balla.pos=balla.pos+balla.p*dt/m
  theta=vp.atan(ra.y/ra.x)
  
  t=t+dt
print("Final Theta = ",theta," rad")



