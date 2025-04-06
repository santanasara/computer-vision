import cv2
from google.colab.patches import cv2_imshow
import requests
import numpy as np

url = 'https://heltonmaia.com/computervision/_images/cover.jpeg'

response = requests.get(url)
imagem = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)

imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.putText(
  img = imagem_rgb,
  text = "OpenCV Challenge",
  org = (50, 50),
  fontFace = cv2.FONT_HERSHEY_DUPLEX,
  fontScale = 2.0,
  color = (255, 0, 0),
  thickness = 3
)
cv2.imwrite('/content/drive/MyDrive/cover_nova.jpeg', imagem_rgb)
cv2_imshow(imagem_rgb)
