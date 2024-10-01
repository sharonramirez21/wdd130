import math

#definimos las funciones que vamos a usar volumen, area y eficiencia del  storage
def compute_volume(radious, height):
    volume = math.pi * (radious ** 2) * height
    return volume

def compute_surface_area(radious, height):
    surface = 2*math.pi * radious * (radious + height)
    return surface
    
def storage_efficiency(radious, height):
    volume = compute_volume(radious, height)
    surface = compute_surface_area(radious, height)
    total = volume / surface
    return total

#abrimos la funcion main para empezar el programa, usamos listas y el bulce for para recorreclas por i elemento.
def main():
   names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303" ]
   
   radious_va = [ 6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.4, 6.83, 15.72, 6.83, 7.62, 8.1]
   
   heights = [ 10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11 ]


   for i in range(len(names)):
       name = names[i]
       radious = radious_va[i]
       height = heights[i]
       
       storage_eff = storage_efficiency(radious, height)
       
       print(f"{name}  {storage_eff:.2f}")

#ponemos main para llamar al programa  
main()