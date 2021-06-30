from store import Store
from product import Product

producto1 = Product(1001,"té negro",500,"Infusión")
producto2 = Product(1002,"café",1500,"Infusión")
producto3 = Product(1003,"fideos",700,"Alimento")
producto4 = Product(1004,"arroz", 1000, "Alimento")
producto5 = Product(1005,"leche", 900, "Bebestible")

tienda1 = Store("Donde Jose")
tienda1.add_product(producto1)
tienda1.add_product(producto2)
tienda1.add_product(producto3)
tienda1.add_product(producto4)
tienda1.add_product(producto5)

print(f"Listado de Productos de la tienda {tienda1.name}")
for i in tienda1.products:
    print(i.print_info())

print("*"*50)
print("Vendiendo un producto...")
tienda1.sell_product(1002)

print("*"*50)
print("Listado de productos que quedan disponibles")
for i in tienda1.products:
    print(i.print_info())

print("*"*50)
print("Actualizaremos el precio de todos los productos en 20%")
tienda1.inflation(20)
print("Listado de productos con precios actualizados")
for i in tienda1.products:
    print(i.print_info())

print("*"*50)
print("Actualizaremos el precio de todos los alimento entregando un descuento del 40%")
tienda1.set_clearance("Alimento", 40)
print("Listado de productos con precios actualizados")
for i in tienda1.products:
    print(i.print_info())






