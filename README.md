# Brinox × WTF AI Engine

Sitio de muestra con el template de `pr.wtf-agency.works`, 60 piezas del run
`outputs/static/brinox-engine-demo/`.

- `/01 Anúncios estáticos` — 13 piezas de marca
- `/02 Filme de produto` — 7 films con capa gráfica de HyperFrames (`filme-grafica/`)
- `/03 Ponto de venda` — 11 piezas en medida real (6 gráficas + 5 lifestyle)
- `/04 PDV na gôndola` — las mismas 6 artes montadas en retail
- `/05 E-commerce` — 5 afiches de performance con botón de compra
- `/06 UGC de criador` — 4 fotos + 4 videos talking head
- `/07 Feed simulado` — 9 piezas 1:1 + el perfil completo 3×3

## Rebuild

```
python3 build.py
```

Lee del run, optimiza los assets (JPG 1400px, MP4 720p) y reescribe `index.html`
a partir de `template.html`. Editá `template.html` para el copy y `build.py`
para qué piezas entran y en qué orden.

Las piezas de proporción extrema (testeira, faixa, totem) se encajan enteras
sobre el fondo oscuro, nunca se recortan: cortarlas se comería el claim o el
logo.

## Idioma

Todo en pt-BR, incluido el marco de presentación, porque el cliente es
brasileño y las piezas ya están en portugués.

## Deploy

No está deployado. Cuando se pida: `subir-on-line` desde esta carpeta.
