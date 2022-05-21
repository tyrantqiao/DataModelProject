from pylab import *

# The new public science museum has an exhibition called "Plastic: A Cautionary Tale" in St Lucia.
# Now the museum will let visitors explore the potential interactions between plastics and the marine environment.
# So we welcome every visitors.
print("Welcome to public science museum!")
print("Don't forget to input your identity!")

# Introduction of plastic and patron type below:
type = float(input("Dear Sir or Madam,\n\nThis exhibition is suitable for two patron types and further introduction depends on different types. So please input the number to get corresponding instructions.\
\n\nIf you're Science Rookie that not familiar with scientific terminology, notation and graph,\
\n please enter 0.\
\n\nIf you are Science Enthusiast that Familiar with common scientific terminology, notation and graph,\
\n please enter 1.\
\n\n partron type: "))

# Here is type of input:
if type == 0:
    print(
        "Plastics as synthetic polymers that are widely used in modern times. So the museum will introduce the plastic production as well as the influence of marine environment by plastic.")
elif type == 1:
    print(
        "Plastics are a broad range of synthetic polymers that are suitable for use in products including packaging, consumer goods, textiles, transportation, construction and electronics due to their low cost and wide range of uses. print. Plastic products are very common in modern times. So we have to look at the scale of plastic production and the impact this could have on the marine environment.")

# Statement about the scale of plastic production and its changed:
# Data of plastic production:
type = float(input("Plastic productivity continued to increase from 1975 to 2014, and at this rate, it will continue to increase in the future.\
\n\nMake sure your type then get garph and relevant data of future years. Or you can also change your type\
\n\nScience Rookie: 0, Science Enthusiast: 1.\
\n\n make sure your type: "))


# Here is the plastic_production function
def Y(t):
    plastic_production = (2 * (10 ** -37)) * (e ** (0.0518 * t))
    return (plastic_production)


if type == 0:
    plastic_production = float(input("Please input a year number between 1975 to 2050\
\n\n Year: "))
plastic_production = Y(plastic_production) / 1000000
print(plastic_production, "million tonnes")

if type == 1:
    print("222")

print("Thank you for coming. Welcome to here next time! Goodbye!")
