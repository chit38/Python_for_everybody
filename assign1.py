text = "X-DSPAM-Confidence:    0.8475"
position = text.find('0')
temp = text[position:]
ans = float(temp)
print(ans)