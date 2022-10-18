# Assembler - Grupo Numero º2
---
---
### Integrantes:
- Samuel Aliaga
- Jose Muñoz
- Matias Toro

---
---

## Información de desarrollo y compilado
- Código desarrollado en python 3.9.7
- Uso de librería "re" 
  - se puede usar `$ pip install regex` en caso de no tenerlo.
- Uso de librería "os"

---
---
## Información de uso
1. Ejecutar main.py
2. Ingresar posterior a `$ ingrese archivo: ` el nombre del archivo (o dirección del archivo)
   - Recomendación: colocar el archivo en el directorio _/test_
3. Revisar los archivos en .out y .mem en _/out_, estos tendrán el mismo nombre que el fichero original pero con un _\_men_ o _\_out_ respectivamente

---
---
## Información de relevante
- Los archivos en _/dat_ y _/temp_ no se recomienda modificarlos ya que son parte del funcionamiento
- En el caso de que tenga problemas el nombre del archivo modifique la variables `file_name` a un _string_ deseado

---
---
## Información sobre archivos _/test_
A continuación se explicara que son cada unos de los ficheros dentro de la carpeta _/test_
`./test/error_example.ass`
- Fichero de ejemplo con errores 

---
`./test/example.ass`
- Fichero de ejemplo sin errores (original)

---
`./test/example2.ass`
- Fichero de ejemplo sin errores (alternativo)

---
`./test/p1_1.ass`
- Problema solicitado de los números impares
---
`./test/p1_2.ass`
- Problema solicitado de los palindromes
---
`./test/p2.ass`
- Problema solicitado de los pixeles saturados
---
`./test/p3.ass`
- Problema solicitado ordenar binarios