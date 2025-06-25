from ultralytics import YOLO

model = YOLO(r'C:\Users\guill\OneDrive\Escritorio\Universidad\TFM\Models\best.pt')

results = model.predict(r'C:\Users\guill\OneDrive\Escritorio\Universidad\TFM\test (1).mp4', save = True) ## Con esto lo que hacemos es darle el path del video y que nos guarde el video con la inferencia del modelo (En ese comando no está puesto el path)
print(results[0]) ## Nos muestra el primer frame

for box in results[0].boxes: ## Esta función lo que hace es printear las cajas que marcan a las personas
    print(box)
