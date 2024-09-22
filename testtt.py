import math
def area_triangle():
    b=float(input(' length of base'))
    h=float(input('Height'))
    final=1/2*float(h)*float(b)
def circle():
    if u_para=='area':
        r=float(input('Enter the radius'))
        final=math.pi*(float(r)**2)
    elif u_para=='circumference' or 'perimeter':
        r=float(input('Enter the radius'))
        final=math.tau*r
def area_square():
    float(s)=input('Enter the length of the side')
    final=math.pow(s,2)
def peri_square():
    float()=input('Enter the length of the side')
    final=4*s
def area_rec():
    float(l)=input('Length')
    float(b)=input('Breadth')
    final=l*b
def peri_rec():
    float(b)='Breadth'
    float(l)='length'
    final=2*(l+b)
def volume_sphere():
    float(r)=input('Enter the radius of the sphere')
    final=4/3*math.pi*(math.pow(r,3))
def tcsa_sphere():
    float(r)=input('Enter the radius of the sphere')
    final=4*math.pi*(r**2)
def volume_cylinder():
    float(r)=input('Enter the radius of the cylinder')
    float(h)=input('Height')
    final=math.pi*h*(r**2)
def tsa_cylinder():
    float(r)=input('Enter the radius of the cylinder')
    float(h)=input('Height')
    final=math.tau*r*(r+h)
def csa_cylinder():
    float(r)=input('Enter the radius of the cylinder')
    float(h)=input('Height')
    final=math.tau*r*h
def volume_cube():
    float(s)=input('Enter the length of the side')
    final=math.pow(s,3)
def csa_cube():
    float(s)=input('Enter the length of the side')
    final=4*math.pow(s,2)
def tsa_cube():
    float(s)=input('Enter the length of the side')
    final=6*math.pow(s,2)
def volume_cone():
        float(r)=input('Enter the radius of the cone')
        float(h)=input('Height')
        final=1/3*math.pi*(r**2)*h





























































#list of all shapes both 2d and 3d in seperate lists
d2_shapes=['triangle','circle','square','rectangle','rhombus']
d3_shapes=['sphere','cylinder','cube','cubiod','cone']
shapes=[d2_shapes,d3_shapes]
dimesnions=['2d','3d']
#The assessment criterion for the said shapes as per their dimension
d2_para=['area','circumference','perimeter']
d3_para=['suface area','volume','curved surfavce area','csa']
u_id=input("2d shape or 3d shape:")
u_id not in dimesnions:
    print("Not a viable dimension")
    u_id=input("2d shape or 3d shape:")
u_shape=input("Choose your shape:")
u_shape=u_shape.lower()
# Protection aginst any traceback if user inputs a value not in the list of shapes of  their respective dimnsion
if u_id== '2d'and u_shape not in d2_shapes:
        print("invalid shape!! Enter a valid shape for selected dimension")
elif u_id=='3d'and u_shape not in d3_shape:
        print("invalid shape!! Enter a valid shape for selected dimension")
elif not u_shape in shapes:
    print('invalid input!! PLease input a valid shape')
u_dimen=input("Which parameter would you like to assess:")
if u_id=='2d' and u_dimen not in d2_para:
        print("invalid parameter!! Enter a valid parameter. Area or circumference")
elif u_id=='3d' and u_dimen not in d3_para:
    print("invalid parameter!! Enter a valid parameter for 3d figures")
