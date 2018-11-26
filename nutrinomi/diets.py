from os import listdir
import sys
from nutri.models import Diet
from django.db import IntegrityError

print('Insert diets')
Diet.objects.create(name="Dieta mediterranea", description="Dieta baja en sodio, para el tratamiento de la hipertensión arterial: se elimina el agregado de sal en las comidas, evitando también alimentos ricos en sodio, como fiambres, embutidos, alimentos enlatados, etc", quantity_cal=1200)

Diet.objects.create(name="Dieta baja en hidratos de carbono", description="se basa en la reducción del consumo de carbohidratos en la alimentación como arroz blanco, pasta y pan. Por lo que para compensar la reducción de carbohidratos se debe: aumentar el consumo de proteínas como carnes y huevos; aumentar el consumo de grasas buenas, que están presentes en los alimentos como por ejemplo aguacate, frutos secos, semillas de chía, semillas de linaza, coco, aceite de oliva y pescados como sardina y salmón", quantity_cal="1470")

Diet.objects.create(name="Dietas bajas en grasas", description="Una dieta baja en grasas es una dieta que restringe la ingesta de grasa y, a menudo, también de grasa saturada y colesterol. Las dietas bajas en grasa tienen el propósito de reducir enfermedades tales como enfermedades del corazón y la obesidad. La reducción de grasa en la dieta puede hacer que sea más fácil reducir la cantidad de calorías consumidas.", quantity_cal="1200")

Diet.objects.create(name="Dietas bajas en calorías", description="perder grasa corporal en poco tiempo y ser un útil aliado para un cambio de alimentación de carácter duradero. Una dieta baja en carbohidratos es adecuada para cualquier persona que quiera perder grasa corporal y definir los músculos. Con una dieta baja en carbohidratos se puede conseguir tanto perder peso como ganar masa muscular.", quantity_cal="1000")

Diet.objects.create(name="Dietas proteicas, bajas en hidratos de carbono",description=" El exceso de proteína en el cuerpo se convierte en carbohidratos).Antes solíamos llamarla “comida baja en carbohidratos de forma estricta”, pero como la palabra “keto” o “cetogénico” ahora se usa de forma frecuente, usamos este término para simplificar.", quantity_cal="1750")

Diet.objects.create(name="Dieta vegetariana",description="Las dietas vegetarianas se enfocan principalmente en el consumo de productos de origen vegetal (frutas, verduras, legumbres, hortalizas, semillas, granos, etc.). Existen tres variantes: la dieta vegetariana estricta, la dieta lacto-vegetariana y la ovo-lacto-vegetariana.", quantity_cal="1000")
