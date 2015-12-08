name = 'Petr Tikilyaynen'
age = 23 # not a lie
height = 70 # inches
height_in_cms = 2.54 * height
weight = 150 # lbs
weight_in_kg = weight * 0.45

eyes = 'blueish' 
teeth = 'white'
hair = 'blonde'

print "Let's talk about %s, who is %d years old." % (name, age)
print "He's %d inches tall, which is about %d cms." % (height, height_in_cms)
print "He weighs %d lbs, which is about %d kg." % (weight, weight_in_kg)
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth 

# this line is tricky, try to get it exactly right

print "If I add %d, %d and %d I get %d." % (
age, height, weight, age + height + weight)




