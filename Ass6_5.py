text = "X-DSPAM-Confidence:    0.8475"
start = text.find('0')
result = text[start :]
ans = float(result)
print(ans)
