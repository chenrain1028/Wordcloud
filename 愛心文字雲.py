from PIL import Image
from wordcloud import WordCloud
import imageio

mk=imageio.imread('heart.png')  #設定遮罩，可以自行找有圖形白底的png檔
#設定參數
w=WordCloud(background_color='white',repeat=True,max_words=100,height=480,
            width=854,max_font_size=100,font_path='字型/kaiu.ttf',
            colormap='Reds',mask=mk)
#width : int (default=400) 輸出的畫布寬度，預設為400畫素
#height : int (default=200) 輸出的畫布高度，預設為200畫素
#font_path : 字型路徑，需要展現什麼字型就把該字型路徑+字尾名寫上，如：font_path = '黑體.ttf'
#background_color :color value (default=”black”) 背景顏色，如background_color='white',背景顏色為白色。
#colormap : string or matplotlib colormap, default=”viridis” 給每個單詞隨機分配顏色，若指定color_func，則忽略該方法。
#stopwords : set of strings or None 設定需要遮蔽的詞，如果為空，則使用內建的STOPWORDS
#max_words : number (default=200)要顯示的詞的最大個數

text="愛、cinta、love、amour、Liebe、liefde、láska、amore、mīlestība、sarang、aisuru、Aşk" #輸入文字，可以自行代換

w.generate(text)
w.to_image()
w.to_file('newheart.png') #存成想要的檔名
img=Image.open('newheart.png')

#顯示文字雲圖片參數
print(img.size)
print(img.mode)
print(img.format)

img.show()#展示圖片

#plt.imshow(w)
#plt.axis('off')
#plt.show() #其他秀圖方法

w.recolor()#重新分配顏色