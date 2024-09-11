elephant = loadImage("elephant.png")
mustache = loadImage("mustache-161330_1280.png")
top_hat = loadImage("top_hat_2.png")
tusk = loadImage("tusk.png")
size(966, 693)

elephant_width = 966
elephant_height = 693
mustache_width = 1280/7
mustache_height = 640/7
top_hat_width = 880/4
top_hat_height = 720/4

fill(255, 255, 255)
image(elephant, 0, 0, elephant_width, elephant_height)
image(mustache, elephant_width/5-25, elephant_height/3+25, mustache_width, mustache_height)
image(top_hat, elephant_width/4+10, -20, top_hat_width, top_hat_height)
image(tusk, 0, 0, elephant_width, elephant_height)
