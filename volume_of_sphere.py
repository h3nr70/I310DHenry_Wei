def compute_area_of_circle(radius):
	pi = 3.14
	volume = 4/3 * pi * radius ** 3
	return volume

radius1 = 30
volume1 = compute_area_of_circle(radius1)
print(f"the volume of the sphere is {volume1}")
radius2 = 40

volume2 = compute_area_of_circle(radius2)
print(f"the volume of the sphere is {volume2}")
