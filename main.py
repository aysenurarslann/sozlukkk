meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "Kahkaha ile yere yuvarlanmak (Rolling On the Floor Laughing)",
    "SHEESH": "Şaşkınlık veya hayranlık ifadesi",
    "SMH": "Başını sallayarak hayret etmek (Shaking My Head)",
    "ICYMI": "Gözden kaçtıysa diye (In Case You Missed It)",
    "TL;DR": "Çok uzun, okumadım (Too Long; Didn't Read)"
}

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict:
    print(word + ": " + meme_dict[word])
else:
    print("Bu kelimeyi henüz bilmiyoruz. Belki de çok yenidir!")
