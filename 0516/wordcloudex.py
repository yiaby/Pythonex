from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 텍스트 파일 열기
text = open('/0516/data/usa_president_message.txt', encoding='UTF-8').read()

# 워드 클라우드 이미지 생성
wordcloud = WordCloud(background_color='white',width=1920,height=1080).generate(text)

# 화면에 출력
fig = plt.figure()
plt.imshow(wordcloud,interpolation='bilinear',cmap='YlOrBr')
plt.axis('off')

# SVG 객체로 이미지 저장
plt.savefig('./output/usa_president_message_wordcloud.svg')