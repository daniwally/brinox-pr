#!/usr/bin/env python3
"""Arma el sitio Brinox con el template de pr.wtf-agency.works.

Copia y optimiza los assets del run outputs/static/brinox-engine-demo/
y escribe index.html con los tres drops: estáticos, video y PDV.
"""
import json
import shutil
import subprocess
from pathlib import Path

from PIL import Image

Image.MAX_IMAGE_PIXELS = None

ROOT = Path(__file__).parent
RUN = ROOT.parent / "outputs/static/brinox-engine-demo"

DROPS = [
    dict(
        n="01", titulo="ANÚNCIOS ESTÁTICOS",
        desc="Dez peças, dez produtos, dez templates. Cada uma com um único argumento, "
             "o packshot oficial do SKU e o copy em português.",
        dest="estaticos",
        items=[
            ("images/4x5/template-01-headline.png", "Nada gruda. Nem o ovo."),
            ("images/4x5/template-07-us-vs-them.png", "Até 70% menos espaço"),
            ("images/1x1/template-12-lifestyle-colorway.png", "Bonita demais pra guardar"),
            ("images/1x1/template-13-stat-surround-hero.png", "O feijão em menos tempo"),
            ("images/4x5/template-10-press-editorial.png", "A mesa posta diz muito"),
            ("images/4x5/template-04-features-benefits.png", "Corte que dura"),
            ("images/4x5/template-05-bullet-points.png", "Lixo fora da vista"),
            ("images/1x1/template-22-flavor-story.png", "O almoço de domingo"),
            ("images/48x85/template-02-offer-promotion.png", "O chá das 5"),
            ("images/1x1/template-35-hero-product-stat-bar.png", "O bolo merece palco"),
            ("eletrica/pecas/01-hero-programa.png", "Você programa. Ela cuida."),
            ("eletrica/pecas/02-stats-ficha.png", "A cozinha inteira num botão"),
            ("eletrica/pecas/04-seguranca.png", "Pressão sem susto"),
        ],
    ),
    dict(
        n="02", titulo="FILME DE PRODUTO",
        desc="A imagem em movimento sai do motor de vídeo; a tipografia entra depois, "
             "composta sobre o material, para que o claim e a marca fiquem exatos e nunca "
             "se deformem. Vertical, pronto para stories.",
        dest="video",
        items=[
            ("filme-grafica/out/m01-fit-armario.mp4", "Até 70% menos espaço"),
            ("filme-grafica/out/m02-smart-ovo.mp4", "Nada gruda. Nem o ovo."),
            ("filme-grafica/out/m03-loft-cozinha.mp4", "Bonita demais pra guardar"),
            ("filme-grafica/out/m04-facas-corte.mp4", "Corte limpo, todo dia"),
            ("filme-grafica/out/assadeira-domingo.mp4", "O almoço de domingo"),
            ("filme-grafica/out/pressure-feijao.mp4", "O feijão em menos tempo"),
            ("filme-grafica/out/faqueiro-mesa.mp4", "A mesa posta diz muito"),
        ],
    ),
    dict(
        n="03", titulo="PONTO DE VENDA",
        desc="Onze peças em medida real de impressão, com tipografia viva e PDF vetorial pronto "
             "para a gráfica. Seis em versão gráfica e cinco em versão lifestyle, com a cena "
             "dentro da peça.",
        dest="pdv",
        items=[
            ("pdv/artes/testeira.png", "Testeira de gôndola · 900×250 mm"),
            ("pdv/artes/cartaz.png", "Cartaz A3 · 297×420 mm"),
            ("pdv/artes/totem.png", "Totem de chão · 600×1600 mm"),
            ("pdv/artes/chao.png", "Adesivo de chão · Ø600 mm"),
            ("pdv/artes/faixa.png", "Faixa de gôndola · 1000×80 mm"),
            ("pdv/artes/wobbler.png", "Wobbler · Ø100 mm"),
            ("pdv/artes-lifestyle/l-testeira.png", "Lifestyle · Testeira 900×250 mm"),
            ("pdv/artes-lifestyle/l-cartaz.png", "Lifestyle · Cartaz A3"),
            ("pdv/artes-lifestyle/l-totem.png", "Lifestyle · Totem 600×1600 mm"),
            ("pdv/artes-lifestyle/l-balcao.png", "Lifestyle · Display de balcão A4"),
            ("pdv/artes-lifestyle/l-chao.png", "Lifestyle · Adesivo de chão Ø600 mm"),
        ],
    ),
    dict(
        n="04", titulo="PDV NA GÔNDOLA",
        desc="As mesmas seis artes montadas no varejo: testeira no topo da gôndola, totem "
             "no corredor, adesivo no chão, wobbler na prateleira, faixa no trilho e cartaz "
             "no display de parede.",
        dest="mockups",
        items=[
            ("pdv/mockups/01-testeira-gondola.png", "Testeira no topo da gôndola"),
            ("pdv/mockups/02-totem-corredor.png", "Totem no corredor"),
            ("pdv/mockups/03-adesivo-chao.png", "Adesivo no chão"),
            ("pdv/mockups/04-wobbler-prateleira.png", "Wobbler na prateleira"),
            ("pdv/mockups/05-faixa-gondola.png", "Faixa no trilho"),
            ("pdv/mockups/06-cartaz-parede.png", "Cartaz no display"),
        ],
    ),
    dict(
        n="05", titulo="E-COMMERCE",
        desc="Formato de performance: a cena manda e o produto vive dentro dela. Grande "
             "angular de cozinha real, a pia em destaque, alguém usando o produto de verdade "
             "e o botão de compra.",
        dest="ecommerce",
        items=[
            ("ecommerce/posters/01-smart-lava-facil.png", "Lava fácil. Não gruda."),
            ("ecommerce/posters/02-fit-cozinha-em-ordem.png", "Cozinha em ordem, sem esforço"),
            ("ecommerce/posters/03-facas-corte-limpo.png", "Corte limpo, todo dia"),
            ("ecommerce/posters/04-lixeira-sem-tocar.png", "Cozinha limpa, sem tocar"),
            ("eletrica/pecas/03-ecommerce-bancada.png", "O jantar pronto sem você olhar"),
        ],
    ),
    dict(
        n="07", titulo="FEED SIMULADO",
        desc="Nove peças replicando o @brinoxoficial real: 601 mil seguidores, o claim de bio "
             "\"Especial é estar presente\", a comunidade BrinoxLovers e os pilares que a "
             "própria conta mantém nos destaques. Alternadas para que a grade funcione como "
             "conjunto.",
        dest="feed",
        items=[
            ("feed/perfil.png", "O perfil inteiro, 3×3"),
            ("feed/posts/01-receita-carne.png", "Receita · Sela por fora"),
            ("feed/posts/02-produto-primea.png", "Produto · Ceramic Life"),
            ("feed/posts/03-comunidade-600k.png", "Comunidade · 600 mil BrinoxLovers"),
            ("feed/posts/04-quando-trocar.png", "Educativo · Quando trocar"),
            ("feed/posts/05-receita-pao.png", "Receita · Pão caseiro"),
            ("feed/posts/06-utilidade-organizacao.png", "Utilidade · Cabe tudo"),
            ("feed/posts/07-criadora.png", "Criador · O feijão de terça"),
            ("feed/posts/08-frase-presente.png", "Marca · Especial é estar presente"),
            ("feed/posts/09-onde-comprar.png", "Conversão · Onde comprar"),
        ],
    ),
    dict(
        n="06", titulo="UGC DE CRIADOR",
        desc="Gravado como quem grava em casa com o celular: cozinha real, luz da janela, "
             "sem produção. As fotos servem como anúncio nativo e são também o primeiro "
             "quadro dos vídeos falados.",
        dest="ugc",
        items=[
            ("ugc/clips/01-eletrica-descoberta.mp4", "Falando da panela elétrica"),
            ("ugc/clips/02-fit-armario.mp4", "Falando do jogo empilhável"),
            ("ugc/clips/03-facas-corte.mp4", "Falando das facas"),
            ("ugc/clips/04-smart-ovo.mp4", "Falando do antiaderente"),
            ("ugc/fotos/01-eletrica-descoberta.png", "Criadora · panela elétrica"),
            ("ugc/fotos/02-fit-armario.png", "Criadora · jogo Fit"),
            ("ugc/fotos/03-facas-corte.png", "Criador · facas Infinity"),
            ("ugc/fotos/04-smart-ovo.png", "Criadora · Smart Plus"),
        ],
    ),
]

MAX_W = 1400


def prep_image(src: Path, dest: Path):
    im = Image.open(src)
    if im.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGB", im.size, (10, 10, 11))
        im = im.convert("RGBA")
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    if im.width > MAX_W:
        im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
    # Las piezas de proporcion extrema (testeira, faixa, totem) no se recortan:
    # cortarlas se comeria el claim o el logo. Se encajan enteras sobre el fondo
    # oscuro del sitio, que ademas las lee como "pieza larga mostrada completa".
    ratio = im.width / im.height
    target = None
    if ratio > 2.2:
        target = (im.width, round(im.width / 1.55))
    elif ratio < 0.62:
        target = (round(im.height * 0.72), im.height)
    if target:
        canvas = Image.new("RGB", target, (10, 10, 11))
        canvas.paste(im, ((target[0] - im.width) // 2, (target[1] - im.height) // 2))
        im = canvas
    im.save(dest, quality=88, optimize=True)
    return dest


def prep_video(src: Path, dest: Path):
    subprocess.run([
        "ffmpeg", "-y", "-v", "error", "-i", str(src),
        "-vf", "scale=720:-2", "-c:v", "libx264", "-crf", "26",
        "-preset", "slow", "-an", "-movflags", "+faststart", str(dest),
    ], check=True)
    return dest


def main():
    items_json = []
    drops_html = []
    idx = 0
    total_img = total_vid = 0

    for d in DROPS:
        out_dir = ROOT / d["dest"]
        if out_dir.exists():
            shutil.rmtree(out_dir)
        out_dir.mkdir(parents=True)
        cards = []
        for rel, tag in d["items"]:
            src = RUN / rel
            if not src.exists():
                print(f"  FALTA {rel}")
                continue
            is_vid = src.suffix == ".mp4"
            name = src.stem + (".mp4" if is_vid else ".jpg")
            dest = out_dir / name
            (prep_video if is_vid else prep_image)(src, dest)
            web = f"{d['dest']}/{name}"
            items_json.append({"src": web, "type": "video" if is_vid else "image", "tag": tag})
            kind = "VID" if is_vid else "IMG"
            media = (f'<video muted loop playsinline preload="metadata" src="{web}"></video>'
                     f'<span class="play">▶</span>') if is_vid else \
                    f'<img loading="lazy" src="{web}" alt="">'
            cards.append(
                f'<button class="card" data-i="{idx}">{media}'
                f'<span class="tag">{d["n"]} · {kind} · {tag}</span></button>'
            )
            idx += 1
            total_vid += is_vid
            total_img += not is_vid
            print(f"  {web}")

        drops_html.append(
            f'<section class="drop"><div class="dhead"><div class="dl">'
            f'<span class="dn">/{d["n"]}</span><h2>{d["titulo"]}</h2></div>'
            f'<p class="ds">{d["desc"]}</p>'
            f'<span class="dc">{len(cards)} peças</span></div>'
            f'<div class="grid">{"".join(cards)}</div></section>'
        )

    tpl = (ROOT / "template.html").read_text(encoding="utf-8")
    html = (tpl
            .replace("{{DROPS}}", "".join(drops_html))
            .replace("{{ITEMS}}", json.dumps(items_json, ensure_ascii=False))
            .replace("{{TOTAL}}", str(idx))
            .replace("{{IMGS}}", str(total_img))
            .replace("{{VIDS}}", str(total_vid)))
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"\nindex.html · {idx} peças ({total_img} img · {total_vid} vid)")


if __name__ == "__main__":
    main()
