import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import urllib

# Carregar as imagens
img1 = np.array(Image.open(urllib.request.urlopen("https://heltonmaia.com/computervision/_downloads/27015188a65ad16fa2070d389007d463/tropical1.png")))

img2 = np.array(Image.open(urllib.request.urlopen("https://heltonmaia.com/computervision/_downloads/e2513971dd417c6bb717797a348ae452/tropical2.png")))

# Verificar se as imagens têm o mesmo tamanho
if img1.shape != img2.shape:
    raise ValueError("As imagens devem ter o mesmo tamanho para adição.")

# Adicionar as imagens
mask = img2 < 255
added_img = np.copy(img1)
added_img[mask] = img2[mask] * 0.5

# Exibir as imagens lado a lado
fig, axs = plt.subplots(1, 3, figsize=(10, 5))

# Exibir a primeira imagem
axs[0].imshow(img1)
axs[0].set_title('Imagem 1')
axs[0].axis('off')

# Exibir a segunda imagem
axs[1].imshow(img2)
axs[1].set_title('Imagem 2')
axs[1].axis('off')

# Exibir a imagem resultante da adição
axs[2].imshow(added_img)
axs[2].set_title('Imagem Resultante')
axs[2].axis('off')
plt.show()